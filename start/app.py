
from wsgiref.validate import validator
from flask import Flask, app, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordFile,BooleanField
from wtforms.validators import Inputrequired, Email, Length

app= Flask(__name__)
Bootstrap(app)

class LoginForm(FlaskForm):
    username = StringField('username',validators=[Inputrequired(),Length(min=4,max=15)])
    pasword = PasswordFile('password',validators=[Inputrequired(),Length(min=8,)])
    remember = BooleanField("remember me")
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',form=form)
@app.route('/signup')
def signup():
    return render_template('signup.html')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
if __name__ == '__main__':
    app.run(debug=True)