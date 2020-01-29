from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


app =  Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy()
def create_app():
    app.config.from_object(Config)
    
    
    db.init_app(app)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
    