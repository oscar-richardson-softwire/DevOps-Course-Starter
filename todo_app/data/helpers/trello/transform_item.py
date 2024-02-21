

from todo_app.data.helpers.trello.get_status_for_item import get_status_for_item

def transform_item(untransformed_item):
    """
    Transforms an item from the format returned by the Trello REST API 
    to the format expected by the app.

    Args:
        untransformed_item: A saved item in the format returned by the Trello API.

    Returns:
        items: A saved item in the format expected by the app.
    """

    id = untransformed_item['id']
    status = get_status_for_item(untransformed_item)
    title = untransformed_item['name']
    

    item = {
        'id': id,
        'status': status,
        'title': title
    }

    return item
