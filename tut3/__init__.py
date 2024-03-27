from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate


import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '32350f84288e0445d47cb9e5d16e136e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_message_category = 'info'

migrate= Migrate(app,db)

from tut3 import routes
