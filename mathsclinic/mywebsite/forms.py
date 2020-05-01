#we  create some forms so the user can register and login
from flask_wtf import FlaskForm
from wtforms import  StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
#datarequired checks to make sure you fill the data, Email makes sure you enter correct format for emails,Equalto confirms password
from wtforms import ValidationError


#this form will enable the user login
class LoginForm(FlaskForm):
    email=StringField('Email', validators=[DataRequired(), Email()])
    password=PasswordField('Password', validators=[DataRequired()])
    submit=SubmitField('Log in')


class RegistrationForm(FlaskForm): #we inherit Flaskform
    email=StringField('Email', validators=[DataRequired(), Email()])
    username= StringField('Username', validators=[DataRequired()]) #your validators should alays be a list
    password=PasswordField('Pasword', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords mus match')])
    pass_confirm= PasswordField('Confirm Password', validators=[DataRequired()])
    submit=SubmitField('Register')

    #this method will check if not None for the email
    def check_email(self, field):
        if User.query.filter_by(email=field.data).first(): #filter_by is an ORM call, this function will check if the email has been registered or activated
            raise  ValidationError('Your email has been already registerd')