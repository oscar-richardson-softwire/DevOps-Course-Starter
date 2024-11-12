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
    Fetches all items from the CosmosDB database 
    and returns them as Item objects.

    Returns:
        items: The list of all items as Item objects.
    """

    items = []

    for db_item in db_items.find():
        item = Item.from_db_item(db_item)
        items.append(item)

    return items

def add_item(title):
    """
    Adds a new item with the specified title to the CosmosDB database.

    Args:
        title: The title of the item.

    Returns:
        Void.
    """

    db_item = {
        'title': title,
        'status': 'Not Started'
    }

    db_items.insert_one(db_item)

def update_item_status(id, new_status):
    """
    Changes the status of the item with the specified id
    to the specified status, in the CosmosDB database.

    Args:
        id: The (string) id of the item.
        new_status: The new status for the item.

    Returns:
        Void.
    """

    db_items.update_one({ '_id': ObjectId(id) }, { '$set': { 'status': new_status } })
