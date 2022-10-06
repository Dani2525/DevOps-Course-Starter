from flask import request
from flask import Flask, render_template,redirect
from todo_app.flask_config import Config
import os
from todo_app.data.mongo_items import mongo, _id, status
from todo_app.ViewModel import ViewModel,Item


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/' , methods=['GET'])
    def alltodoitems():    
        allitems = mongo.getitems()
        todo_view_model = ViewModel(allitems)
        return render_template("index.html", view_model = todo_view_model)


    @app.route('/createnewcard' , methods=['POST'] )
    def createnewcard ():
        name = request.form["title"]
        mongo.createcard(name)
        return redirect('/')

    

    @app.route('/complete_item/<id>', methods=['POST'])
    def complete_item(id):
        mongo.changestatus(_id,status)
        return redirect('/')

    