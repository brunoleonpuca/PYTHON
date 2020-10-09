import mysql.connector
import click # Para ejecutar comandos en la terminal, necesario para crear las tablas y la relacion entre ellas
from flask import current_app, g # current_app = mantiene la app levantada, g = variable global para distintas variables y acceder de distintos lados
from flask.cli import with_appcontext # cuando ejecutamos el Script de bdd, necesitamos el contexto de nuestra aplicacion, acceso a variables de configuracion (host, user, pass)
from .schema import instructions # .schema=schema.py va a contener todos los Scripts para crear nuestra bdd

def get_db(): # Para obtener la base de datos y el cursor
    if "db" not in g:
        g.db = mysql.connector.connect( # Asignamos a g.db la base de datos a la cual nos conectamos
            host=current_app.config["DATABASE_HOST"],
            user=current_app.config["DATABASE_USER"],
            password=current_app.config["DATABASE_PASSWORD"],
            database=current_app.config["DATABASE"]
        )
        g.c = g.db.cursor(dictionary=True) # Accedemos al cursor y lo asignamos a g.c para ejecutar las querys
    return g.db, g.c # Devolvemos ambas variables configuradas necesarias para el uso de la bdd (configuraciones de bdd y cursor)

def close_db(e=None): # Funcion necesaria para cerrar la conexion cada vez que hagamos una peticion, por seguridad
    db = g.pop("db", None)
    if db is not None: # Si esta definida (osea si se uso), se cierra
        db.close()

def init_db():
    db, c = get_db()
    for i in instructions:
        c.execute(i)
    db.commit()

@click.command("init-db") # Aca se utiliza click, init-db pasa a ser un comando en la terminal
@with_appcontext # Para que funcione correctamente, tenemos que utilizar la configuracion de las variables
def init_db_command():
    init_db()
    click.echo("Base de datos inicializada")

def init_app(app): # Funcion para Flask para ejecutar la funcion de cierre de bdd, cuando termine de ejecutar la peticion, llama a close_db
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command) # Suscribimos el comando a flask