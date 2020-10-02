"""DICCIONARIOS"""
#diccionario = { "nombre": "chanchito feliz",
#               "raza": "Persa",
#               "edad": 5
#  }
#
#IMPRIMIR DICCIONARIO -> print(diccionario)
#ACCEDER UNICAMENTE A UN DATO -> print(diccionario['nombre'])
#ACCEDER A DATO 2 -> print(diccionario.get('nombre'))

#CAMBIAR DATOS DE DICCIONARIO
#diccionario['nombre'] = "fluffy" -> print(diccionario['nombre']) -> "fluffy"

#CONTAR ELEMENTOS DE DICCIONARIO (columnas)
#print(len(diccionario)) -> 3

#AGREGAR ELEMENTO A DICCIONARIO -> diccionario['pelaje'] = 'negro'

#ELIMINAR VALOR DE DICCIONARIO -> diccionario.pop('pelaje')
#ELIMINAR ULTIMO VALOR DE DICCIONARIO -> diccionario.popItem()
#ELIMINAR CON DEL -> del diccionario['pelaje']
#ELIMINAR TODOS LOS VALORES -> diccionario.clear()

#COPIAS DE DICCIONARIO -> copiaDeGatito = diccionario.copy()
#OTRA FORMA DE COPIAR -> copiaDeGatito = dict(diccionario)

"""DICCIONARIOS ANIDADOS"""
fluffy = {
        "nombre": "fluffy",
        "edad": 4
}
mamba = {
        "nombre": "mamba",
        "edad": 8
}
gatitos = {
        "Fluffy": fluffy,
        "Mamba": mamba
}
print(gatitos)

#OTRA MANERA ES CON DICT
perritos = dict(nombre="chanchito feliz", edad=6)