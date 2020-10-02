from flask import Flask, request, url_for, redirect, abort, render_template # Importamos las librerias: 
                                                # Flask = Necesaria para flask
                                                # request = Para recibir datos del usuario y poder utilizarlos
                                                # url_for = Manejo de Url's
                                                # redirect = Redireccion al usuario
                                                # abort = para detener el navegador y devolver un mensaje al usuario
                                                # render_template = devuelve al usuario el html para una respuesta

# Especifica que este archivo va a ser el main de la application
app = Flask(__name__) 

import mysql.connector

midb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "admin",
    database = "prueba"
)

cursor = midb.cursor(dictionary=True)

# @ = Decoradores instancian rutas
@app.route("/") # Indica que el codigo siguiente a ejecutarse va a ser a partir de la raiz del navegador
def index(): # La funcion que se ejecuta
    return "hola mundo"

@app.route("/post/<post_id>") # Indica la /direccion/ y <argumento> que tomara la direccion del servidor
def post(post_id): # El argumento es tomado a partir de la URL definida. El nombre de la funcion debe estar relacionado a la direccion 
    return "El id del post es: " + post_id

@app.route("/post1/<post_id>", methods=["GET", "POST"]) # Metodos web [GET, POST, PUT, DELETE]
def post1(post_id):
    if request.method == "GET":
        return "El id del post es: " + post_id
    else:
        return "Este es otro metodo distinto a GET"

@app.route("/lele", methods=["GET", "POST"]) 
def lele():
    cursor.execute("select * from Usuario")
    usuarios = cursor.fetchall()
    print(usuarios)
    # abort(404) # Devuelve el error del codigo (403, 404, etc) al ingresar a esta ruta, el metodo GET debe estar obligatoriamente
    # return redirect(url_for("post", post_id=2)) # Obligatoriamente necesitamos el return y esto nos permite redirigirnos a la url puesta dentro de los parentesis
    # print(url_for("index")) # Nos indica la raiz contenedora de la funcion index, en este caso seria '/'
    # print(url_for("post", post_id=2)) # Lo mismo, en este caso seria '/post/2'
    # print(request.form) # Si por GB pasamos: 'curl -d "llave1=dato1&llave2=dato2" --silent -X POST http://localhost:5000/lele' devuelve "ImmutableMultiDict([('llave1', 'dato1'), ('llave2', 'dato2')])"
    # print(request.form['llave1']) # Si pasamos lo mismo, devolveria 'dato1'
    # print(request.form['llave2']) # En este casi, 'dato2'
    # return "lele"
    # return render_template("lele.html") # Retorna el codigo de lele.html
    # return { # Retorna el siguiente Json, no se usa el render_template
    #     "username":"chanchito feliz",
    #     "email":"chanchito@feliz.com"
    # }
    return render_template("lele.html", dataUsuarios=usuarios)

@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html", mensaje="Hola Mundo") # En home.html se reformatea el 'mensaje' con {{}}

@app.route("/crear", methods=["GET", "POST"])
def crear():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        edad = request.form["edad"]
        sql = "insert into Usuario (email, username, edad) values (%s, %s, %s)"
        values = (email, username, edad)
        cursor.execute(sql, values)
        midb.commit()
        return redirect(url_for("lele"))
    return render_template("crear.html")