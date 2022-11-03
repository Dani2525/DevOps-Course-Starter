from flask import request
from flask import Flask, render_template,redirect
from todo_app.flask_config import Config
import os
from todo_app.ViewModel import ViewModel,Item
import todo_app.data.mongo_items as mongo
from flask_login import login_required, LoginManager 
import requests


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
        mongo.changestatus(id,'Done')
        return redirect('/')

    @app.route('/login/callback')
    def callback():
     code = request.args.get('code')

    data = {
        'client_id': os.getenv('client_id'),
        'client_secret': os.getenv('client_secret')
    }
    url = 'https://github.com/login/oauth/access_token'
    headers = {'Accept': 'application/json'
    }
    
    response = requests.post(url, data=data, headers= headers) 
    access_token = response.json()['access_token']
    
    # then use "requests" to make the call to GitHub and swap the code for a token    

    login_manager = LoginManager()

    @login_manager.unauthorized_handler
    def unauthenticated():
        client_id = os.getenv('client_id')
        return redirect(f'https://github.com/login/oauth/authorize?client_id={client_id}')
        
        
        pass  # Add logic to redirect to the GitHub OAuth flow when unauthenticated

    @login_manager.user_loader
    def load_user(user_id):
        pass   # We will return to this later  
    
    login_manager.init_app(app)
    
    return app    