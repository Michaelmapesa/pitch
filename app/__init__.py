from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
import psycopg2
import os


from .config import config_options

db = SQLAlchemy()

mail = Mail()

from .models import User

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    mail.init_app(app)
    login_manager.init_app(app)
    db.init_app(app)
    app.config.from_object(config_options[config_name])

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is the primary key, we use it to query
        return User.query.get(int(user_id))

        # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of the app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    
    return app