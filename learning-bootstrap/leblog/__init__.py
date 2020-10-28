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
    
    from . import db
    db.init_app(app)

    from . import auth
    from . import workspace
    
    app.register_blueprint(auth.bp)
    app.register_blueprint(workspace.bp)


    return app