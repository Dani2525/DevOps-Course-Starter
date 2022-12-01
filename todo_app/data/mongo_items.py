import os
import pymongo
import requests
from flask import request
from bson.objectid import ObjectId
from todo_app.ViewModel import Item

def getitems():
    allitems = []
    client = pymongo.MongoClient(os.getenv("mongo_client"))
    db = client.todo_db
    alltodoitems = db.todo_collection
    for todo in alltodoitems.find():
        item=Item(todo['_id'],todo['name'],todo['status'])
        allitems.append(item)

    return allitems

def createitem(name):
    client = pymongo.MongoClient(os.getenv("mongo_client"))
    db = client.todo_db
    todoitems = db.todo_collection
    item = {"name": name, "status": "To Do"}
    todoitems.insert_one(item)

def changestatus(id,status):
    client = pymongo.MongoClient(os.getenv("mongo_client"))
    db = client.todo_db
    todoitems = db.todo_collection
    filter = { '_id': ObjectId(id) }
    newvalues = { "$set": { 'status': status } }
    response = todoitems.update_one(filter,newvalues)
    return response
    