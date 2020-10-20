from flask import Blueprint, flash, g, render_template, request, url_for, redirect, session, jsonify
from werkzeug.exceptions import abort
from leblog.auth import login_required
from leblog.db import get_db

bp = Blueprint("workspace", __name__)

@bp.route("/", methods=["POST", "GET"])
@login_required
def index():
    db, c = get_db()
    c.execute(
        "select u.id, b.title, b.blog, b.created_by, b.created_at, u.username from blog b JOIN user u on b.created_by = u.id order by created_at desc" 
    )
    blogs = c.fetchall()

    return render_template("workspace/index.html", blogs=blogs)

@bp.route("/create", methods=["POST", "GET"])
@login_required
def create():
    if request.method == "POST":
        title = request.form["title"]
        blog = request.form["blog"]
        error = None

        if not title:
            error = "El titulo es necesario para crear este blog."
        if not blog:
            error = "El blog debe tener informacion para poder guardarse."
        
        if error is not None:
            flash(error)
        else:
            db, c = get_db()

            c.execute(
                "insert into blog (title, blog, created_by) values (%s, %s, %s)",
                (title, blog, g.user["id"])
            )
            
            db.commit()
            
            return redirect(url_for("workspace.index"))

    return render_template("workspace/create.html")


@bp.route("/<int:id>/update", methods=["POST", "GET"])
@login_required
def update(id):
    return render_template("workspace/update.html")
