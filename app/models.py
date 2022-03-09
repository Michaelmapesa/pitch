from cgitb import text
from datetime import date
from email.policy import default
from multiprocessing.sharedctypes import Value
from unicodedata import category
from flask_login import UserMixin
from app import db
from flask_sqlalchemy  import SQLAlchemy
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_wtf import FlaskForm 

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    pitches = db.relationship('Pitch', backref='user', passive_deletes=True)
    coments = db.relationship('comment', backref='user', passive_deletes=True)
    upvotes = db.relationship('Upvote', backref='user', passive_deletes=True)
    downvotes = db.relationship(
        'Downvote',backref='user',passive_deletes=True
    )

class Pitch (db.Model):
        id = db.Column(db.Integer,primary_key=True)
        text= db.Column(db.String(2000))
        category = db.Column(db.String(100),nullable=False)
        date_created = db.Column(db.DateTime,default=db.func.current_timestamp())
        author = db.Column(db.Integer,db.ForeignKey(
            'user.id',ondelete='CASCADE'),nullable=False)
        comments=db.relationship(
            'Comment',backref='pitch',passive_deletes=True
        )

class comment (db.Model):
        id = db.Column(db.Integer,primary_key=True)
        text = db.Column(db.String(300),nullable=False)
        date_created = db.Column(db.DateTime,default=db.func.current_timestamp())
        author = db.Column(db.Integer,db.ForeignKey(
            'user.id',ondelete='CASCADE'),nullable=False)
        pitch_id = db.Column(db.Integer,db.ForeignKey(
              'pitch.id',ondelete='CASCADE'), nullable=False)


class Upvote (db.Model):
        id = db.Column(db.Integer,primary_key=True)
        Value = db.Column(db.Integer,)
        user_id = db.Column(db.Integer,db.ForeignKey(
            'user.id',ondelete='CASCADE'),nullable=False)
        pitch_id = db.Column(db.Integer, db.ForeignKey(
             'pitch.id',ondelete='CASCADE'),nullable=False)
        

class Downvote (db.Model):
    id = db.Column(db.Integer,primary_key=True)
    value = db.Column(db.Integer,)
    user_id = db.Column(db.Integer,db.ForeignKey(
         'user.id',ondelete='CASCADE'), nullable=False)
    Pitch_id = db.Column(db.Integer,db.ForeignKey(
         'pitch.id',ondelete='CASCADE'),nullable=False)



class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])



        


