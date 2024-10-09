from todo_app.data.helpers.trello.map_list_name_to_item_status import map_list_name_to_item_status

class Item:
    """
    A to-do item in the app.

    Properties:
        id: The item id.
        status: The status of the to-do item (one of 'Not Started', 'Doing', or 'Done').
        title: The task that the to-do item represents.
    """
    def __init__(self, id, title, status = 'Not Started'):
        self.id = id
        self.status = status
        self.title = title

    @classmethod
    def from_trello_card(cls, trello_card, list):
        """
        Returns a new Item from a Trello card
        and the list it belongs to.

        Args:
            cls: The Item class.
            trello_card: The Trello card.
            list: The list that the Trello card belongs to.

        Returns:
            item: The new Item.
        """
        item = cls(
            trello_card['id'], 
            trello_card['name'], 
            map_list_name_to_item_status(list['name'])
        )

        return item
    
    @classmethod
    def from_db_item(cls, db_item):
        """
        Returns a new Item from an item document from the database.

        Args:
            cls: The Item class.
            db_item: The item document from the database.

        Returns:
            item: The new Item.
        """
        item = cls(
            str(db_item['_id']), 
            db_item['title'], 
            db_item['status']
        )

        return item