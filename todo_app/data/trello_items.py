import os
from todo_app.data.helpers.trello.get_untransformed_items import get_untransformed_items
from todo_app.data.helpers.trello.make_request import make_request
from todo_app.data.helpers.trello.transform_item import transform_item

def get_items():
    """
    Fetches all saved items and their statuses from Trello using the Trello REST API
    and transforms them from the format returned by the Trello API to the format
    expected by the app.

    Returns:
        items: The list of saved items in the format expected by the app.
    """

    untransformed_items = get_untransformed_items()

    items = list(map(transform_item, untransformed_items))

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
