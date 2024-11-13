import os
import pytest
from dotenv import load_dotenv, find_dotenv
import mongomock
import pymongo

# SETUP

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    
    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        from todo_app import app
        test_app = app.create_app()
        insert_mock_data()
        with test_app.test_client() as client:
            yield client

def insert_mock_data():
    cosmos_db_connection_string = os.environ.get('COSMOS_DB_CONNECTION_STRING')
    mongo_client = pymongo.MongoClient(cosmos_db_connection_string)

    db_name = os.environ.get('DB_NAME')
    db = mongo_client[db_name]
    db_items = db.items

    items_to_insert = [
        {
            'title': 'Test card 1',
            'status': 'Not Started'
        },
        {
            'title': 'Test card 2',
            'status': 'Not Started'
        },
        {
            'title': 'Test card 3',
            'status': 'Done'
        }
    ]

    db_items.insert_many(items_to_insert)



# TESTS

def test_index_page(client):
    response = client.get('/')

    assert response.status_code == 200
    assert 'Mark as Done' in response.data.decode()
    assert 'Test card 1' in response.data.decode()
    assert 'Test card 2' in response.data.decode()
    assert 'Mark as Not Started' in response.data.decode()
    assert 'Test card 3' in response.data.decode()
