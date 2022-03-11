
import os

class Config:
    SECRET_KEY = '67dc88e287b53f38'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaaccess:mapesa@localhost/mapesa'
    

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
}