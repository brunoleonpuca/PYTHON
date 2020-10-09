import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY = "mikey",
        DATABASE_HOST = "localhost",#os.environ.get("FLASK_DATABASE_HOST"), #localhost
        DATABASE_USER = "chanchito",#os.environ.get("FLASK_DATABASE_USER"), #chanchito
        DATABASE_PASSWORD = "feliz",#os.environ.get("FLASK_DATABASE_PASSWORD"), #feliz
        DATABASE = "leblog"#os.environ.get("FLASK_DATABASE") #leblog
    )
    
    from db import init_app
    db.init_app(app)

    return app