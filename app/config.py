
import os

class Config:
    SECRET_KEY = '67dc88e287b53f38'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaaccess:mapesa@localhost/mapesa'
    

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = False


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
}