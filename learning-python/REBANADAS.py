"""MAP (aplica funcion a todos los elementos de una lista)"""
#list,map y lambda#lista1 = list(map(lambda x:x+10, lista1)) -> print(lista1) -> "[11,12,13,14,15,16,17]"
#lista2 = list(map(lambda x:x+'c', lista)) -> print(lista) -> "[ac,abc,abcc,abcdc,abcdec]"

"""FILTER (filtra una lista a partir de una funcion, o funcion lambda)"""
#llamar a filter usando 1 funcion y 1 lista#filter(funcion,lista)
#llamar lambda dentro de filter#list(filter(lambda numero: numero%5 == 0, numeros))
#lista1 = list(filter(lambda x:x*2 > 5, lista1)) -> print(lista1) -> "[3,4,5,6,7]"

"""LISTAS POR COMPRESION (Listas con conjuntos)"""
#cuadrados = [i**2 for i in range(6)] -> print(cuadrados) -> "[0,1,4,9,16,25]"
#con condicion#mayoresA100 = [i**3 for i in range(7) if i**3 > 100] -> print(mayoresA100) -> "[125,216]"

