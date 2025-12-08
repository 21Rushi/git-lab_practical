import uuid
import hashlib
from db import todo_collection

def create_todo_item(item_name, item_description):
    # Generate Item ID (Auto-increment)
    last_item = todo_collection.find_one(sort=[("_id", -1)])
    item_id = (last_item["itemID"] + 1) if last_item else 1

    # Generate UUID
    item_uuid = str(uuid.uuid4())

    # Create hash from name + description
    raw_string = item_name + item_description + item_uuid
    item_hash = hashlib.sha256(raw_string.encode()).hexdigest()

    todo_item = {
        "itemID": item_id,
        "itemUUID": item_uuid,
        "itemHash": item_hash,
        "itemName": item_name,
        "itemDescription": item_description
    }

    todo_collection.insert_one(todo_item)
    return todo_item

