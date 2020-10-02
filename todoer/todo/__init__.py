import os # Modulo para utilizar funciones del sistema operativo

from flask import Flask

# Funcion obligatoria para empezar la aplicacion
def create_app(): 
    app = Flask(__name__) # Donde Flask se instancia
    
    app.config.from_mapping( # Nos permite definir variables de entorno para configurar la app 
        SECRET_KEY="mikey", # Para definir la llave de una sesion, crear la sesion, famosa "cookie"="identificador unico"
        DATABASE_HOST=os.environ.get("FLASK_DATABASE_HOST"), # Definimos donde esta la bdd
        DATABASE_PASSWORD=os.environ.get("FLASK_DATABASE_PASSWORD"), # La contraseña de la bdd
        DATABASE_USER=os.environ.get("FLASK_DATABASE_USER"), # El usuario que va a acceder a la bdd
        DATABASE=os.environ.get("FLASK_DATABASE"), # El nombre de la bdd
    )# Esto se utiliza para definir la base de los accesos de nuestra app
    
    from . import db # Traemos db.py
    db.init_app(app) # Llamamos a la funcion para inicializar la bdd

    from . import auth # Traemos desde auth.py
    from . import todo # Traemos desde todo.py
    
    # REGISTRAMOS LOS BLUEPRINTS PARA TENER ACCESO A SUS ENDPOINTS
    app.register_blueprint(auth.bp) 
    app.register_blueprint(todo.bp)

    return app