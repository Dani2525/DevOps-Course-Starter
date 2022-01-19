from flask import Flask, render_template,redirect
from todo_app.data.trello_items import createcard, getcards
from todo_app.flask_config import Config
import requests
import json
import os

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/' , methods=['GET'])
def alltodoitems():
    response = getcards()
    cards=response.json() #changing the python objects to json
    Allitems=[]
    for card in cards:
        item=Item(card['id'],card['name'])
        Allitems.append(item)

    return render_template("index.html",todo=Allitems)


@app.route('/createnewcard' , methods=['POST'] )
def createnewcard ():
    response = createcard()
    print(response.text)
    return redirect('/')

    

@app.route('/complete_item/<id>', methods=['POST'])
def complete_item(id):
    url =f"https://api.trello.com/1/cards/{id}"
    params ={ 'key':os.getenv('TRELLO_KEY'),
             'token':os.getenv('TRELLO_TOKEN'),
            'idList':os.getenv('TRELLO_LISTID2')
    }

    headers = {
        "Accept": "application/json"
}

    response = requests.request(
        "PUT",
        url,
        headers=headers,
        params=params
    )
    print(response.text)
    return redirect('/')

class Item:
    def __init__(self, id, name, status = 'To Do'):
        self.id = id
        self.title= name
        self.status = status
    @classmethod
    def from_trello_card(cls, card, list):
        return cls(card['id'], card['name'], list['name']) 

#item = Item.from_trello_card(card, card_list) 