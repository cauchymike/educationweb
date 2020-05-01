#create our model for users in models.py
from mywebsite import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash #gives the ability to generate and check password
from flask_login import  UserMixin #this will give us access to a lot of built in attributes


#this decorator will alow flask login to load the current user and grab their id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id) #this will enable us load and show information specific to that user

#creating a user class
class User(db.Model, UserMixin): #we inherit from db.Model class and Usermixing class


    __tablename__= 'users' #giving it a table name parameter, note, every user takes a row on the table, and each attribute take a column

    id= db.Column(db.Integer, primary_key=True) #every user should have a unique primary key so we dont have overlapping primary keys
    email=db.Column(db.String(64), unique=True, index=True) #the number 64 takes care of spam, unique takes care of more than one emails from users
    username=db.Column(db.String(64), unique=True, index=True)
    password_hash= db.Column(db.String(128)) #we have 128 because the password hash can be very lenghty

    #we use this to create an instance of the User object
    def __init__(self, email,username,password):
        self.email=email#save the email
        self.username=username #save the username
        self.password_hash=generate_password_hash(password) #we dont wantb to save the string the user typed in, we want to save the hashed password

    #in order to check when a user is login in, we need a method called check password
    def check_password(self, password):
        return check_password_hash(self.password_hash,password) #this will accept password, hash it and check it against the selfpassword saved earlier
