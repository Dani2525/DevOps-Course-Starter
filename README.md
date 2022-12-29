# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.


## new Environment variables

SECRET_KEY=secret-key
mongo_client=mongodb://module10:t0qwxU3V7MZ2Y55mhbnRAtefiGrwJTUHaTO6MhO0Kv8KTW3PX6GKvlon3LF1h8u29BCgQRYE41wgACDbSTzsgg==@module10.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@module10@
client_id=461640fd1000642d0462
client_secret=a1a2e8f1dc310351d18b4a3a36493c7edc9c0e22

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running tests

You should run the command "poetry run pytest" to run all the tests that are assocoiated with this todoapp.

## how to build and run development and production containers

build and run production containers by running these commands
docker build --target production --tag todo-app:prod .
docker run --env-file .env -p 5000:5000 todo-app:prod 

build and run development containers by running these commands
docker build --tag todo-app .  
docker run --env-file .env todo_app

## running test container 
test container run using CI pipeline in My-CI-Pipeline.yml file everytime you open or reopen a pull request or push to repository
can also be observed on GitHub workflows to see which ones pass and fail.

## Terraform
main.tf file uses declarative script to make Azure Infrastructure, where Todoapp is deployed to.
new variables added 
ARM_CLIENT_ID
ARM_CLIENT_SECRET
ARM_SUBSCRIPTION_ID
ARM_TENANT_ID
application can be seen on https://dani-m12-todoapp.azurewebsites.net

## lOGGING
loggly is used to add logs to the todoapp
env variable Called lOG_LEVEL, configurably set to DEBUG or ERROR 
LOGGLY_TOKEN used for authentication 



