from flask import Flask, render_template,redirect
from todo_app.data.trello_items import createcard, getcards
from todo_app.flask_config import Config
import requests
import os
from todo_app.ViewModel import ViewModel,Item

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/' , methods=['GET'])
    def alltodoitems():
        response = getcards()
        cards=response.json() #changing the python objects to json
        Allitems=[]
        for card in cards:
            if card['idList'] == os.getenv('TRELLO_LISTID1'):
                status = 'To Do'
            else:
                status = 'Done'

            item=Item(card['id'],card['name'],status)
            Allitems.append(item)

        todo_view_model = ViewModel(Allitems)
        return render_template("index.html", view_model = todo_view_model)


    @app.route('/createnewcard' , methods=['POST'] )
    def createnewcard (name):
        response = createcard(name)
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

    return app
    