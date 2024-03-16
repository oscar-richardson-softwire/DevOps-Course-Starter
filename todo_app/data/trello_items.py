import os
from todo_app.data.helpers.trello.make_request import make_request
from todo_app.data.helpers.trello.map_list_name_to_item_status import map_list_name_to_item_status
from todo_app.data.helpers.trello.transform_item import transform_item

def get_items():
    """
    Fetches all saved items and their statuses from Trello using the Trello REST API
    and transforms them from the format returned by the Trello API to the format
    expected by the app.

    Returns:
        items: The list of saved items in the format expected by the app.
    """

    board_id = os.getenv('TRELLO_BOARD_ID')

    url = f'https://api.trello.com/1/boards/{board_id}/lists'

    query = {
        'cards': 'open',
        'card_fields': 'id,name'
    }

    lists = make_request(http_method='GET', url=url, query=query).json()

    items = []

    for list in lists:
        for card in list['cards']:
            item = {
                'id': card['id'],
                'status': map_list_name_to_item_status(list['name']),
                'title': card['name']
            }
            items.append(item)

    return items

def add_item(title):
    """
    Adds a new item with the specified title to Trello and
    returns this item in the format expected by the app.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item in the format expected by the app.
    """

    to_do_column_list_id = os.getenv('TRELLO_TO_DO_COLUMN_LIST_ID')

    url = 'https://api.trello.com/1/cards'

    query = {
        'idList': to_do_column_list_id,
        'name': title
    }

    untransformed_item = make_request(http_method='POST', url=url, query=query).json()

    item = transform_item(untransformed_item)

    return item

def update_item_status(id, new_status):
    """
    Changes the status of the item with the specified id 
    to the specified status and returns this item 
    in the format expected by the app.

    Args:
        id: The id of the item.
        new_status: The new status of the item.

    Returns:
        item: The item in the format expected by the app.
    """

    if new_status == 'Not Started':
        column_list_id = os.getenv('TRELLO_TO_DO_COLUMN_LIST_ID')
    else:
        column_list_id = os.getenv('TRELLO_DONE_COLUMN_LIST_ID')

    url = f'https://api.trello.com/1/cards/{id}'

    query = {
        'idList': column_list_id,
    }

    untransformed_item = make_request(http_method='PUT', url=url, query=query).json()

    item = transform_item(untransformed_item)

    return item
