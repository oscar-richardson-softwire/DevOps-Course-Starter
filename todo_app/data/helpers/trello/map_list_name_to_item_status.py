def map_list_name_to_item_status(list_name):
    """
    Maps the name of a list in Trello to the corresponding Item status.

    Args:
        list_name: The name of the list in Trello.

    Returns:
        item_status: The corresponding Item status.
    """

    if list_name == 'To Do':
        item_status = 'Not Started'
    else:
        item_status = list_name

    return item_status