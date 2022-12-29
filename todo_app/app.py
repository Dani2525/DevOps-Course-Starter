import os

import requests
from flask import Flask, redirect, render_template, request
from flask_login import LoginManager, UserMixin, login_required, login_user, current_user

import todo_app.data.mongo_items as mongo
from todo_app.flask_config import Config
from todo_app.ViewModel import Item, ViewModel

from loggly.handlers import HTTPSHandler
from logging import Formatter
class User(UserMixin):
    def __init__(self, id):
        self.id = id
        if id == "94120348":
            self.role = "writer"
        else:
            self.role = "reader"        
    
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    app.logger.setLevel(os.getenv('LOG_LEVEL'))

    app.config['LOGIN_DISABLED'] = os.getenv('LOGIN_DISABLED') == 'True'

    @app.route('/' , methods=['GET'])
    @login_required 
    def alltodoitems():    
        allitems = mongo.getitems()
        todo_view_model = ViewModel(allitems)
        return render_template("index.html", view_model = todo_view_model)


    @app.route('/createnewcard' , methods=['POST'] )
    @login_required 
    def createnewcard ():
        if app.config['LOGGLY_TOKEN'] is not None:
         handler = HTTPSHandler(f'https://logs-01.loggly.com/inputs/{app.config["LOGGLY_TOKEN"]}/tag/todo-app')
        handler.setFormatter(
        Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")
        )
        app.logger.addHandler(handler)
        app.logger.info("You have successfully logged in")    
        if current_user.role != "writer":
            app.logger.warn(f"user {current_user.id} tried to create a card without permissions")
            return 'sorry, you cannot create a todo card'
        name = request.form["title"]
        mongo.createitem(name)
        return redirect('/')

    @app.route('/complete_item/<id>', methods=['POST'])
    @login_required 
    def complete_item(id):
        if current_user.role != "writer":
            app.logger.warn(f"user {current_user.id} tried to create a card without permissions")    
            return 'sorry, you cannot set a todo card to done'
        mongo.changestatus(id,'Done')
        app.logger.info(f"user  {current_user.id} has set a card to done")
        return redirect('/')

    @app.route('/login/callback')
    def callback():
        authorisation_code = request.args.get('code')

        data = {
            'client_id': os.getenv('client_id'),
            'client_secret': os.getenv('client_secret'),
            'code': authorisation_code
        }
        url = 'https://github.com/login/oauth/access_token'
        headers = {'Accept': 'application/json'
        }
        
        access_token_response = requests.post(url, data=data, headers= headers)
        access_token_response.raise_for_status()
        access_token = access_token_response.json()['access_token']

        url = "https://api.github.com/user"
        headers = {
            'Authorization': f"Bearer {access_token}"
        }

        user_response = requests.get(url, headers = headers)

        user_id = user_response.json()['id']

        user = User(user_id)

        login_user(user)

        return redirect('/')
    
    # then use "requests" to make the call to GitHub and swap the code for a token    

    login_manager = LoginManager()

    @login_manager.unauthorized_handler
    def unauthenticated():
        client_id = os.getenv('client_id')
        return redirect(f'https://github.com/login/oauth/authorize?client_id={client_id}')
        
        
        pass  # Add logic to redirect to the GitHub OAuth flow when unauthenticated

    @login_manager.user_loader
    def load_user(user_id):
        return User(user_id)
    
    login_manager.init_app(app)
    
    return app