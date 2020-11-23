from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    v = "Listado de links y cosas utiles"
    return render_template("index.html", example=v)
