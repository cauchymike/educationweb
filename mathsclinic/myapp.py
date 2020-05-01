#view connects our forms to our templates
from mywebsite import  app, db
from flask import render_template,redirect,request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user #we use this to decorate our normal viewing functions
from mywebsite.models import User #this should activate the user we called in User.query.. in forms.py
from mywebsite.forms import LoginForm, RegistrationForm



#we start with our home view
@app.route('/')
def home():
    return render_template('home.html') #this function(view) connects to our home html file


#this view(function) welcomes the user after they have logged in
@app.route('/welcome')
@login_required #this decorator makes sure that in order to see the welcome page, you must be logged in
def welcome():
    return render_template('welcome.html') #this redirects you to the welcome html fter your login has been confirmd


@app.route('/logout')
@login_required#you cant logout if you are not logged in
def logout():
    logout_user()#this is being imported from flask login
    flash('you are now logged out. Thanks for visiting')
    return redirect(url_for('home'))#after logging out, you are taking to the homepage




#our login view

@app.route('/login', methods=['GET', 'POST'])#we have methods because there is a form to fill
def login():

    form=LoginForm() #we must first create an instance of the login form to activate the form
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first() #we grab user based on  the first email since email are unique
        #None takes care of a user that tries to log in with an email that doesnt exist.i.e  user=None in that case
        #check password makes sure that the password supplied by the user was correct
        if user.check_password(form.password.data) and user is not None: #recall the checkpasssword method we called on the object User

            login_user(user) #this was imported from flask_login
            flash('You are now logged in Successfully!')

            #if a user tries to access a page that requires login, we save that request as next
            next=request.args.get('next') #redirects the user to the login page, if next is none, it means they went directly to the login page
            if next==None or not next[0]=='/': # checks if the page exists, if it doesnt, they are directed to the welcome page
                next=url_for('welcome')#next[0] is asking if next exist at the homepage
            return redirect(next)
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form=RegistrationForm()

    if form.validate_on_submit():

        user= User(email=form.email.data,
                  username=form.username.data,
                  password=form.password.data)
        
        db.session.add(user)
        db.session.commit()
        flash(' Thanks for Joining our team!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


if __name__== '__main__':
    app.run(debug=True)






