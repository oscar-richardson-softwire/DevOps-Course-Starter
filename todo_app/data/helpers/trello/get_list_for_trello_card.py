from todo_app.data.helpers.trello.make_request import make_request

def get_list_for_trello_card(trello_card):
    """
    Fetches the list that a Trello card belongs to using the Trello REST API.

    Args:
        card: A Trello card.

    Returns:
        list: The list that the Trello card belongs to.
    """

    list_id = trello_card['idList']

    url = f'https://api.trello.com/1/lists/{list_id}'

    list = make_request(http_method='GET', url=url).json()

    return list
