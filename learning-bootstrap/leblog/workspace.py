from flask import Blueprint, flash, g, render_template, request, url_for, redirect, session
from werkzeug.exceptions import abort
from leblog.auth import login_required
from leblog.db import get_db

bp = Blueprint("workspace", __name__)

@bp.route("/", methods=["POST", "GET"])
@login_required
def index():
    db, c = get_db()
    c.execute(
        "select b.id, b.title, u.username, b.created_at, b.analysis, b.rating from blog b JOIN user u "
        "on b.created_by = u.id where b.created_by = %s order by b.created_at desc", (g.user["id"],) 
    )
    blogs = c.fetchall()

    return render_template("workspace/index.html", blogs=blogs)

@bp.route("/create", methods=["POST", "GET"])
@login_required
def create():
    if request.method == "POST":
        title = request.form["title"]
        analysis = request.form["analysis"]
        rating = request.form["ratingRadioButton"]
        error = None

        if not title:
            error = "El titulo es necesario para crear este analisis."
        if not analysis:
            error = "El analisis debe tener informacion para poder guardarse."
        if not rating:
            error = "El rating no puede ser nulo"

        if error is not None:
            flash(error)
        else:
            db, c = get_db()

            c.execute(
                "insert into blog (title, analysis, rating, created_by) values (%s, %s, %s, %s)",
                (title, analysis, rating, g.user["id"])
            )
            
            db.commit()
            
            return redirect(url_for("workspace.index"))

    return render_template("workspace/create.html")

def get_blog(id):
    db, c = get_db()
    c.execute (
        "select b.id, b.analysis, b.rating, b.title, b.created_by, b.created_at, u.username"
        " from blog b JOIN user u on b.created_by = u.id where b.id = %s", (id,)
    )
    blog = c.fetchone()

    if blog is None:
        abort(404, "El blog de id {0} no existe".format(id))
    
    return blog

@bp.route("/<int:id>/update", methods=["POST", "GET"])
@login_required
def update(id):
    movie = get_blog(id)

    if request.method == "POST":
        analysis = request.form("analysis")
        rating = request.form["ratingRadioButton"]
        error = None

        if not analysis:
            error = "Analysis is required."
        if not rating:
            error = "Rating is required."
        
        if error is not None:
            flash(error)
            
        else:
            db, c = get_db()
            c.execute(
                "update blog set analysis = %s and rating = %s where id = %s and created_by = %s", (analysis, rating, id, g.user["id"])
            )
            db.commit()

            return redirect(url_for("workspace.index"))

    return render_template("workspace/update.html", blog=movie)


@bp.route("/<int:id>/delete", methods=["POST", "GET"])
@login_required
def delete(id):
    db, c = get_db()
    c.execute (
        "delete from blog where id = %s and created_by = %s", (id, g.user["id"])
    )
    db.commit()
    return redirect(url_for("workspace.index"))