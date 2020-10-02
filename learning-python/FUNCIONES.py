"""FUNCIONES"""
#LAMBDA
#1 parametro# cuadrado = x: x**2 -> cuadrado(3) -> 9, se reemplaza la x por el parametro x
#2(o mas) parametros# raiz = x,y: x**(1/y) -> raiz(25,2) -> 5, se reemplazan ambos parametros

#def funcionConParametrosVariables(*parametro):
#       print(parametro) -> imprime la tupla de argumentos
#       print(parametro[0]) -> imprime el 1er elemento de la tupla
#funcionConParametrosVariables('argumento1', 'argumento2', 'argumento3')

#def nombreCompleto(**kwargs):
#   print(kwargs['nombre'], kwargs['apellido']) -> Bruno Puca
#nombreCompleto(nombre=Bruno, apellido='Puca')

#def valorPorDefectoDeFuncion(parametroPorDefecto = 'parametro'): -> Si no se le asigna un argumento, la funcion queda con este parametro

#INCORPORADAS
#len(lista) -> devuelve cantidad de elementos de una lista
#print(range(5)) -> "1,2,3,4,5"

"""RECURSIVIDAD""" #Se utilizan para los re intentos de reconexion o comprobacion multiple de algun dato
def recursion(i):
    if(i < 1):
        return i
    print(i)
    recursion(i-1)
recursion(6)



"""RANDOM"""
#import random
#numero al azar con rango#random.randint(desde,hasta)


