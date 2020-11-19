from flask import (
    Blueprint, # Paquete blueprint, permite la creacion de blueprints para una mejor configuracion y orden de codigo
    flash,  # Para enviar mensajes a nuestros blueprints de forma generica
    g, # La Bdd 
    render_template, request, url_for,  redirect,
    session # Para mantener una referencia del usuario en el contexto de la aplicacion
)
from werkzeug.exceptions import abort # Cuando el usuario quiera realizar una peticion que no le pertenezca
from todo.auth import login_required # Un metodo para proteger los endpoints, False=redireccion
from todo.db import get_db

bp = Blueprint("todo",__name__) # Creacion de blueprint
# Esta linea va a inscribir a 'todo.bp'

@bp.route("/", methods=["GET", "POST"])
@login_required # Funcion que creamos en auth.py para proteger las funciones de index (la rama principal). Te asegura que el usuario ya inicio sesion
def index():
    db, c = get_db()
    c.execute(
        "select t.id, t.description, u.username, t.completed, t.created_at from todo t JOIN user u "
        "on t.created_by = u.id where t.created_by = %s order by created_at desc", (g.user["id"],)
    )
    todos = c.fetchall() # Obtenemos el response

    return render_template("todo/index.html", todos=todos) # Creamos ruta y pasamos listado

# Ruta 'create'
@bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        description = request.form["description"]
        error = None
        if not description:
            error = "Descripcion es requerida"
        if error is not None:
            flash(error)
        else:
            db, c = get_db()
            c.execute (
                "insert into todo (description, completed, created_by) values (%s, %s, %s)", (description, False, g.user["id"])
            )
            db.commit()
            return redirect(url_for("todo.index")) # Nos redirige hacia la ruta

    return render_template("todo/create.html") # Renderiza el html

def get_todo(id):
    db, c = get_db()
    c.execute(
        "select t.id, t.description, t.completed, t.created_by, t.created_at, u.username from todo t JOIN user u on t.created_by=u.id where t.id = %s",
        (id,) 
    )
    todo = c.fetchone()
    if todo is None:
        abort(404, "El todo de id {0} no existe".format(id))
    return todo

# Ruta 'update'
@bp.route("/<int:id>/update", methods=["GET", "POST"])
@login_required
def update(id):
    todo = get_todo(id)
    if request.method == "POST":
        description = request.form["description"]
        completed = True if request.form.get("completed") == "on" else False
        error = None

        if not description:
            error = "La descripcion es requerida"

        if error is not None:
            flash(error)
        else:
            db, c = get_db()
            c.execute(
                "update todo set description = %s, completed = %s where id = %s and created_by = %s", (description, completed, id, g.user["id"])
            )
            db.commit()
            return redirect(url_for("todo.index"))
    return render_template("todo/update.html", todo=todo)

# Ruta 'delete'
@bp.route("/<int:id>/delete", methods=["POST"])
@login_required
def delete(id):
    db, c = get_db()
    c.execute(
        "delete from todo where id = %s and created_by = %s", (id, g.user["id"]))
    db.commit()
    return redirect(url_for("todo.index"))