import os
from todo_app.data.classes.Item import Item
import pymongo
from bson.objectid import ObjectId

cosmos_db_connection_string = os.getenv('COSMOS_DB_CONNECTION_STRING')
client = pymongo.MongoClient(cosmos_db_connection_string)

db_name = os.getenv('DB_NAME')
db = client[db_name]
db_items = db.items

def get_items():
    """
    Fetches all saved to-do items from the CosmosDB database.

    Returns:
        items: The list of saved Items.
    """

    items = []

    for db_item in db_items.find():
        item = Item.from_db_item(db_item)
        items.append(item)

    return items

def add_item(title):
    """
    Adds a new Item to the CosmosDB database
    and returns this new Item.

    Args:
        title: The title of the Item.

    Returns:
        item: The new Item.
    """

    db_item = {
        'title': title,
        'status': 'Not Started'
    }

    db_items.insert_one(db_item) # This adds the inserted _id field to the db_item dictionary!

    item = Item.from_db_item(db_item)
    
    return item

def update_item_status(id, new_status):
    """
    Changes the status of the item with the specified id
    to the specified status.

    Args:
        id: The (string) id of the item.
        new_status: The new status for the item.

    Returns:
        Void.
    """
    db_items.update_one({ '_id': ObjectId(id) }, { '$set': { 'status': new_status } })
