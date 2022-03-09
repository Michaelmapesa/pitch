from distutils.command.upload import upload
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_migrate import Migrate
from .config import config_options

app = Flask(__name__)

app.config['SECRET_KEY'] = ""
app.config['SQLALCHEMY_DATABASE_URI'] = "database_uri goes here"

bootstrap = Bootstrap(app)

db = SQLAlchemy(app)
Migrate = Migrate(app, db)

mail = Mail(app)

def create_app(config_name):
      login_manager = LoginManager()
      login_manager.init_app(app)
      login_manager.login_view = 'auth.login'
      app.config.from_object(config_options[config_name])



      @login_manager.user_loader
      def load_user(user_id):
          return User.query.get(int(user_id))

      from.auth import auth as auth_blueprint
      app.register_blueprint(auth_blueprint)

      from .main import main as main_blueprint
      app.register_blueprint(main_blueprint)
      return app





