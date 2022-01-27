import os
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

def createcard():
     url = "https://api.trello.com/1/cards"

     headers = {
        "Accept": "application/json"
	}

     query = {
        'idList':os.getenv('TRELLO_LISTID1'),
        'key':os.getenv('TRELLO_KEY'),
        'token':os.getenv('TRELLO_TOKEN'),
        'name': request.form["title"] 
	}

     response = requests.request(
        "POST",
         url,
         headers=headers,
         params=query
	)
     return response
