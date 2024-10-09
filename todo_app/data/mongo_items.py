import os
from todo_app.data.classes.Item import Item
import pymongo

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

# def add_item(title):
#     """
#     Adds a new Item to Trello (in the form of a Trello card)
#     and returns this new Item.

#     Args:
#         title: The title of the Item.

#     Returns:
#         item: The new Item.
#     """

#     to_do_column_list_id = os.getenv('TRELLO_TO_DO_COLUMN_LIST_ID')

#     url = 'https://api.trello.com/1/cards'

#     query = {
#         'idList': to_do_column_list_id,
#         'name': title
#     }

#     trello_card = make_request(http_method='POST', url=url, query=query).json()

#     list = get_list_for_trello_card(trello_card)

#     item = Item.from_trello_card(trello_card, list)

#     return item

# def update_item_status(id, new_status):
#     """
#     Changes the status of the Item with the specified id 
#     to the specified status (by updating the Trello card)
#     and returns this Item.

#     Args:
#         id: The id of the Item.
#         new_status: The new status for the Item.

#     Returns:
#         item: The updated Item.
#     """

#     if new_status == 'Not Started':
#         column_list_id = os.getenv('TRELLO_TO_DO_COLUMN_LIST_ID')
#     else:
#         column_list_id = os.getenv('TRELLO_DONE_COLUMN_LIST_ID')

#     url = f'https://api.trello.com/1/cards/{id}'

#     query = {
#         'idList': column_list_id,
#     }

#     trello_card = make_request(http_method='PUT', url=url, query=query).json()

#     list = get_list_for_trello_card(trello_card)

#     item = Item.from_trello_card(trello_card, list)

#     return item
