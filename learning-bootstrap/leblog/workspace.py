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
        "select b.id, b.title, b.blog, b.created_by, b.created_at, u.username from blog b JOIN user u on b.created_by = u.id order by created_at desc" 
    )
    blogs = c.fetchall()

    return render_template("workspace/index.html", blogs=blogs)