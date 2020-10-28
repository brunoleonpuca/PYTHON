from flask import Flask , render_template

app = Flask(__name__) 

@app.route("/", methods=['GET', 'POST'])
def index():
    titulo = "hola mundo"
    return render_template("index.html", titulo=titulo)

if __name__ == "__main__":
    app.run(debug=True)