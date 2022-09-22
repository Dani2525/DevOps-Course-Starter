import os
import pymongo
import requests
from flask import request
def getcards():
    boardid = os.getenv('TRELLO_BOARDID')
    url = f"https://api.trello.com/1/boards/{boardid}/cards"

    response = requests.request(
     "GET",
      url,     
      params = {
          'key':os.getenv('TRELLO_KEY'),
          'token':os.getenv('TRELLO_TOKEN'),
          'cards':'open'
      }
     )
    return response   


def createcard(name):
    client = pymongo.MongoClient("mongodb://module10:ulH6uBzQRqsLbVIWVR44Cil6nOwb6AML7ykXzCCBygQI4uvkn2Ok8yK1B3GjrhzCgjOE3LdGHJhkUObXOtpXaw==@module10.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@module10@")
    db = client.todo_db
    todocards = db.todo_collection
    card = {"name": name, "status": "To Do"}
    todocards.insert_one(card).inserted_id