from pymongo import MongoClient
import os

client = MongoClient("mongodb://localhost:27017/")
db = client["todo_database"]
todo_collection = db["todo_items"]

