import functools # Set de funciones para construir aplicaciones

from flask import (
    Blueprint, # Paquete blueprint, permite la creacion de blueprints para una mejor configuracion y orden de codigo
    flash,  # Para enviar mensajes a nuestros blueprints de forma generica
    g, # La Bdd 
    render_template, request, url_for, redirect,
    session # Para mantener una referencia del usuario en el contexto de la aplicacion
)

from werkzeug.security import check_password_hash, generate_password_hash # Para verificar y encriptar la contraseña. Por seguridad

from todo.db import get_db # La funcion para obtener la bdd

bp = Blueprint("auth", __name__, url_prefix="/auth") # Creamos el blueprint y le ponemos el prefijo '/auth' a todas las rutas consiguientes (Vamos a crear todos los blueprints en una carpeta nueva 'auth')
# Esta linea va a inscribir a 'auth.bp'

#CREACION DE ENDPOINTS

@bp.route("/register", methods=["GET","POST"]) # El decorador va a contener 'bp' no 'app' desde ahora en nuestros blueprints
def register(): # La funcion que llamamos para hacer el registro de usuarios
    if request.method == "POST": # If para asegurarnos el caso de exito (happy path)
        username = request.form["username"]
        password = request.form["password"] # Datos que vamos a agarrar del usuario
        db, c = get_db() # Abrimos el acceso a la Bdd
        error = None
        c.execute(
            "select id from user where username = %s", (username, )
        ) # Query para buscar al usuario en la bdd
        if not username: # Si el user no escribe nada en username
            error = "Username es requerido"
        if not password: # Si el user no escribe nada en password
            error = "Password es requerido"
        elif c.fetchone() is not None: # Si lo que encontro en la Bdd no trajo ningun resultado
            error = f"Usuario {username} se encuentra registrado."#.format(username)
        
        if error is None: # Si error es invalido, osea la query dio OK, registramos al usuario...
            c.execute(
                "insert into user (username, password) values (%s, %s)",
                (username, generate_password_hash(password))
            ) # Ejecuta el script para añadir el usuario a la tabla y le agrega la contraseña encriptada
            db.commit() # Compromete la tabla para asentar la query anterior

            return redirect(url_for("auth.login")) # Ruta donde vamos a redireccionar al usuario, una vez dio exitoso el register, necesitamos la ruta y funcion login()
    
        flash(error, "error") # Si error no es None, lo va a representar
    
    return render_template("auth/register.html") # Para realizar si el usuario hace la peticion al metodo GET, a prueba de errores

@bp.route("/login", methods=["GET", "POST"]) # Ruta para el login, bp por app nuevamente
def login():
    if request.method == "POST": # Si es POST en login, es porque el usuario esta intentando inciar sesion
        username = request.form["username"] # Agarramos lo que el usuario esta ingresando
        password = request.form["password"]
        db, c = get_db() # Accedemos nuevamente a la Bdd y al cursor
        error = None
        c.execute(
            "select * from user where username = %s", (username,)
        ) # Ejecutamos la query para ver si el usuario existe y recolectar los datos '(username,)' porque las tuplas se escriben obligatoriamente asi
        user = c.fetchone() # Recibimos la informacion de la query anterior

        if user is None: # Si el usuario existe
            error = "Usuario y/o contraseña invalida"
        elif not check_password_hash(user["password"], password): # Utilizamos el chequeo de la contraseña encriptada y la que se ingresa (guarda la pass y la pass+encript)
            error = "Usuario y/o contraseña invalida"

        if error is None: # Si el login fue exitoso
            session.clear() # Si teniamos una sesion vamos a limpiarla 
            session["user_id"] = user["id"] # Creamos una variable dentro de nuestra sesion y le asignamos el id del usuario que buscamos. La sesion la referenciamos luego
            return redirect(url_for("todo.index")) # Vamos a index

        flash(error, "error")
    
    return render_template("auth/login.html") # Por el prefijo del principio hay que agregarlo en todos los casos de render_template o redirect url_for para omitir errores

@bp.before_app_request # Funcion decoradora que se ejecuta siempre antes de cada peticion al servidor
def load_logged_in_user(): # Funcion que carga el usuario a g (Variable global que contiene al usuario)
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None
    else:
        db, c = get_db()
        c.execute(
            "select * from user where id = %s", (user_id,)
        )
        g.user = c.fetchone() # Agregamos el usuario a g

def login_required(view): # View va a definir nuestros Endpoints
    @functools.wraps(view) # Envolvemos la funcion
    def wrapped_view(**kwargs):
        if g.user is None: # Si el usuario esta logeado
            return redirect(url_for("auth.login"))

        return view(**kwargs) # Si se encuentra logeado, devolvemos el endpoint con sus argumentos
    return wrapped_view

@bp.route("/logout")
def logout():
    session.clear() # Limpiamos la sesion
    flash("Cerraste tu sesion...", category="error")
    return redirect(url_for("auth.login")) # Volvemos al login