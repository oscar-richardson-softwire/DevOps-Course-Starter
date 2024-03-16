def map_list_name_to_item_status(list_name):
    """
    Maps the name of a list in Trello to the corresponding item status
    expected by the app.

    Args:
        list_name: The name of a list in Trello.

    Returns:
        item_status: The corresponding item status.
    """
    
    match list_name:
        case 'To Do':
            item_status = 'Not Started'
        case _:
            item_status = list_name

    return item_status