import os
import pytest
import requests
from todo_app import app
from dotenv import load_dotenv, find_dotenv

# SETUP

@pytest.fixture
def client():
    dotenv_path = find_dotenv('.env.test')
    load_dotenv(dotenv_path, override=True)

    test_app = app.create_app()

    with test_app.test_client() as client:
        yield client

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data

# Stub replacement for requests.request(http_method, url, params, headers)
def stub(http_method, url, params, headers):
    fake_trello_board_id = os.environ.get('TRELLO_BOARD_ID')
    fake_response_data = None
    
    if http_method == 'GET':
        if url == f'https://api.trello.com/1/boards/{fake_trello_board_id}/lists':
            fake_response_data = [
                {
                    'id': '123abc',
                    'name': 'To Do',
                    'cards': [
                        {'id': '123', 'name': 'Test card 1'},
                        {'id': '456', 'name': 'Test card 2'}
                    ]
                },
                {
                    'id': '456def',
                    'name': 'Done',
                    'cards': [
                        {'id': '789', 'name': 'Test card 3'}
                    ]
                }
            ]
            return StubResponse(fake_response_data)

        raise Exception(f'Integration test did not expect URL "{url}"')
    raise Exception(f'Integration test did not expect HTTP method "{http_method}"')

# TESTS

def test_index_page(monkeypatch, client):
    monkeypatch.setattr(requests, 'request', stub)

    response = client.get('/')

    assert response.status_code == 200
    assert 'Mark as Done' in response.data.decode()
    assert 'Test card 1' in response.data.decode()
    assert '123' in response.data.decode()
    assert 'Test card 2' in response.data.decode()
    assert '456' in response.data.decode()
    assert 'Mark as Not Started' in response.data.decode()
    assert 'Test card 3' in response.data.decode()
    assert '789' in response.data.decode()
