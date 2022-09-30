import os
import pymongo
import requests
from flask import request
from bson.objectid import ObjectId

def getitems():
    allitems = []

    client = pymongo.MongoClient("mongodb://module10:ulH6uBzQRqsLbVIWVR44Cil6nOwb6AML7ykXzCCBygQI4uvkn2Ok8yK1B3GjrhzCgjOE3LdGHJhkUObXOtpXaw==@module10.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@module10@")
    db = client.todo_db
    alltodoitems = db.todo_collection
    for todo in alltodoitems.find():
        allitems.append(todo)

    return allitems

def createitem(name):
    client = pymongo.MongoClient("mongodb://module10:ulH6uBzQRqsLbVIWVR44Cil6nOwb6AML7ykXzCCBygQI4uvkn2Ok8yK1B3GjrhzCgjOE3LdGHJhkUObXOtpXaw==@module10.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@module10@")
    db = client.todo_db
    todoitems = db.todo_collection
    item = {"name": name, "status": "To Do"}
    todoitems.insert_one(item).inserted_id

def changestatus(id,status):
    client = pymongo.MongoClient("mongodb://module10:ulH6uBzQRqsLbVIWVR44Cil6nOwb6AML7ykXzCCBygQI4uvkn2Ok8yK1B3GjrhzCgjOE3LdGHJhkUObXOtpXaw==@module10.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@module10@")
    db = client.todo_db
    todoitems = db.todo_collection
    filter = { '_id': ObjectId(id) }
    newvalues = { "$set": { 'status': status } }
    response = todoitems.update_one(filter,newvalues)
    return response

# items=getitems() 
# print(items)
# createitem("nametest")
#changestatus("6332d43411c7531211302a71","done")
    