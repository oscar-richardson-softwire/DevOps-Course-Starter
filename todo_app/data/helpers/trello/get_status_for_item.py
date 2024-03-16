from todo_app.data.helpers.trello.make_request import make_request
from todo_app.data.helpers.trello.map_list_name_to_item_status import map_list_name_to_item_status

def get_status_for_item(untransformed_item):
    """
    Fetches the status for an item from Trello using the Trello REST API.

    Args:
        untransformed_item: A saved item in the format returned by the Trello API.

    Returns:
        item_status: The item status.
    """

    list_id = untransformed_item['idList']

    url = f'https://api.trello.com/1/lists/{list_id}'

    list = make_request(http_method='GET', url=url).json()

    item_status = map_list_name_to_item_status(list['name'])

    return item_status
