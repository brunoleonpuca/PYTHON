import mysql.connector # importamos el paquete que conecta mysql con python

midb = mysql.connector.connect( # conectamos la base de datos con estos 4 parametros
    host="localhost", # [host, user, password y database] se encuentran en la informacion de la sesion
    user="root",
    password="admin",
    database="prueba"
) # midb es la variable contenedora de la conexion

cursor = midb.cursor() # obtenemos un cursor, permite la modificacion de la tabla con lenguaje sql

# VER DATOS
cursor.execute("select * from Usuario") # nos permite llamar el metodo de execute para pasarle la query
resultado = cursor.fetchall() # nos devuelve TODOS los elementos elementos encontrados en la query anterior
# # resultado = cursor.fetchone() # solo nos devuelve el 1er elemento encontrado en la query anterior
print(resultado) #imprimimos el resultado

#INGRESAR DATOS
# sql = "insert into Usuario (id, email, username, edad) values (%s, %s, %s, %s)" # creamos la query para ingresar un registro
# values = ("3", "pepe@grillo.com", "pepegrillo", "45") # separamos los valores por sintaxis
# cursor.execute(sql, values) # le pasamos la query y los valores
# midb.commit() # despues de ejecutar una query de ingreso de datos, se debe llamar a commit

# VER DEFINICIONES DE LAS TABLAS
# cursor.execute("show create table Usuario") # devuelve la definicion de la tabla, columnas y tipos de datos

# print(cursor.rowcount)

# ACTUALIZAR DATOS
# sql = "update Usuario set email = %s where id = %s"
# values = ("micorreo@correo.com", "4")
# cursor.execute(sql, values)
# midb.commit()

# ELIMINAR DATOS
# sql = "delete from Usuario where id = %s"
# values = (4, ) # Se debe poner la coma y espacio(, ) si o si, sino da error
# cursor.execute(sql, values)
# midb.commit()