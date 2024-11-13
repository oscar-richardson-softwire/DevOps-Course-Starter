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