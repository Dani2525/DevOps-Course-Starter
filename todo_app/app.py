from flask import request
from flask import Flask, render_template,redirect
from todo_app.flask_config import Config
import os
from todo_app.ViewModel import ViewModel,Item
import todo_app.data.mongo_items as mongo


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/' , methods=['GET'])
    @login_required 
    def alltodoitems():    
        allitems = mongo.getitems()
        todo_view_model = ViewModel(allitems)
        return render_template("index.html", view_model = todo_view_model)


    @app.route('/createnewcard' , methods=['POST'] )
    @login_required 
    def createnewcard ():
        name = request.form["title"]
        mongo.createitem(name)
        return redirect('/')

    @app.route('/complete_item/<id>', methods=['POST'])
    @login_required 
    def complete_item(id):
        mongo.changestatus(mongo._id,mongo.status)
        return redirect('/')

    login_manager = LoginManager()

    @login_manager.unauthorized_handler
    def unauthenticated():
        
        pass  # Add logic to redirect to the GitHub OAuth flow when unauthenticated

    @login_manager.user_loader
    def load_user(user_id):
        pass   # We will return to this later  
    
    login_manager.init_app(app)
    
    return app    