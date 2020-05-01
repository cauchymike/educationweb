#this is the __init__ file underneath my website folder
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


login_manager= LoginManager() #we create an instance of the loginmanager
app = Flask(__name__) #we used this to create our app


#we setup some configurations.. app, basedir
app.config['SECRET_KEY']= 'mysecretkey'
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app) #we use this to create our database for the app
Migrate(app,db) #this will enable us perform migrate on the app and db


login_manager.init_app(app) #we pass in the app to our loginmanager, this will configure your app to have managerment of login
login_manager.login_view='login' #this tells your users what view they go to when they login, your view in app.py must have a login view