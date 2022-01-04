from flask import Flask, render_template, request,redirect
from todo_app.data.session_items import get_items
from todo_app.data.session_items import add_item
from todo_app.flask_config import Config
import requests

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
     allitems=get_items()
     return render_template("index.html",todo=allitems)
     trello = requests.get('https://trello.com/b/byjuj5uu/todo')
     trello.json()

@app.route('/newitem' , methods=['POST'])
def newitems():
    Mynewtitle = request.form["title"] 
    add_item(Mynewtitle)
    return redirect('/')
