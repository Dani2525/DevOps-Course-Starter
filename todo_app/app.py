from flask import Flask, render_template, request,redirect
from todo_app.data.session_items import get_items
from todo_app.data.session_items import add_item
from todo_app.flask_config import Config
import requests

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/todo')
def todo():
     response = requests.get('https://trello.com/b/byjuj5uu/todo')
     trelloApi=response.json()

class Item:
 def __init__(self, id, name, status = 'To Do'):
 self.id = id
 self.name = name
 self.status = status
 @classmethod
 def from_trello_card(cls, card, list):
 return cls(card['id'], card['name'], list['name']) 

item = Item.from_trello_card(card, card_list) 