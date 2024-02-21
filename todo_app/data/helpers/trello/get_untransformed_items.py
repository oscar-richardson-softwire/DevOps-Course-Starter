import os
from todo_app.data.helpers.trello.make_request import make_request

def get_untransformed_items():
    """
    Fetches all saved items from Trello using the Trello REST API,
    without performing any transformations on these items.

    Returns:
        untransformed_items: The list of saved items in the format returned by the Trello API.
    """

    board_id = os.getenv('TRELLO_BOARD_ID')

    url = f'https://api.trello.com/1/boards/{board_id}/cards'

    untransformed_items = make_request(http_method='GET', url=url).json()

    return untransformed_items
