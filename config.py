import os

class Config:

    SECRET_KEY ='SECRET_KEY'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michael:joker@localhost/question'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}