"""LISTAS (ejemplos: lista1=[1,2,3], lista2=[4,5,6]), lista3=[a,ab,abc]"""
#INCORPORADAS (lista.append(dato) para agregar dato)
#impresion#a-print(lista1) -> "[1,2,3]"; b-print(*lista1) -> "1 2 3"
#concatenacion#lista3=lista1+lista2 -> print(lista3) -> "[1,2,3,4,5,6]"
#concatenacion 1 elemento#lista3=lista1+[4] -> print(lista3) -> "[1,2,3,4]"
#replicadas#print(lista*2) -> "[1,2,3,1,2,3]"
#agregar dato#lista1.append(4) -> print(lista1) -> "[1,2,3,4]"
#reemplazar dato#lista1[2]=8 -> print(lista1) -> "[1,2,8]"
#sumar lista#print(sum(lista1)) -> "6"
#mayor/menor elemento de lista#print(max(lista1)) -> "3" ; print(min(lista1)) -> "1"
#rango de listas#lista = list(range(5)) -> print(lista) -> "[1,2,3,4,5]"
#operador in/not in#if 3 in lista1: print("Si") -> "Si" (el if devuelve true por el in)

#COPY - Copia los valores de una lista definida (Sin copiar puntero, copiar la lista completa)
#lista2 = lista1.copy() -> print(lista2) -> [1,2,3]
#copia = lista1[:]
#copia = list(lista1)
#copia = lista1.copy()

#INSERT - Inserta valor a partir de posicion
#lista.insert(posicion, elemento) -> lista1.insert(1,9) -> print(lista1) -> "[1,9,2,3]"

#POP - Remueve elemento a partir de posicion
#lista.pop(posicion) -> lista1.pop(1) -> print(lista1) -> "[1,3]"

#REMOVE - Remueve elemento a partir de valor
#lista.remove(valor) -> lista1.remove(3) -> print(lista1) -> "[1,2]"

#INDEX - Devuelve posicion de valor
#lista.index(valor) -> print(lista1.index(1)) -> "0"

#COUNT - Devuelve repeticiones de elemento
#lista.count(valor) -> print(lista1.count(2)) -> "1"

#CLEAR - Borra lista, deja el objeto igualmente
#lista.clear() -> print(lista.clear()) -> "[]"

#REVERSE - Da vuelta la lista
#lista.reverse() -> print(lista1.reserve()) -> "[3,2,1]"

#SORT - Ordena la lista
#lista.sort() -> print(lista1.sort()) -> "[1,2,3]"
#lista.sort(reverse=True) -> print(lista1.sort(reverse=True)) -> "[3,2,1]"
#key, ordena segun algo#lista1.sort(key=lambda x:x%2) -> "[2,1,3]"
#segun cantidad de letras#lista3.sort(key=len) -> print(lista3) -> "[abc,ab,a]"

"""REBANADAS (ejemplos: lista1=[1,2,3,4,5,6,7] / lista2=[a,ab,abc,abcd,abcde])"""
#CREACION DE SUBLISTAS
#ultimo indice excluido#sub=lista1[2:5] -> print(sub) -> "[3,4,5]"
#inicio hasta fin#sub=lista1[5::] -> print(sub) -> "[6,7]"
#datos de atras hacia delante#sub=lista1[::-1] -> print(sub) -> "[7,6,5,4,3,2,1]"

#REEMPLAZAR
#por rango#lista1[1:2] = [10,15] -> print(lista1) -> "[1,10,15,4,5,6,7]"
#eliminar por rango#lista1[1,6] -> print(lista1) -> "[1]"
#insertar elemento por rebanada nula#lista1[2:2]=[a,b,c] -> print(lista1) -> "[1,2,a,b,c,3,4,5,6,7]"

#COMPARACION (1er elemento con 1er elemento y asi...)
#print([4,3,1] > [3,2]) -> "True"

#ENUMERATE (Devuelve valor y posicion)
#for i, palabra in enumerate(lista1) -> "0 1, 1 2, 2 3, 3 4, 4 5, 5 6, 6 7"

#DEL (Borra elemento a partir de posicion o lista completa)
#del lista1[1] -> print(lista1) -> "[1,3,4,5,6,7]"
#del lista1[1:5] -> print(lista1) -> "[1,7]"
#del lista1 -> print(lista1) -> error, no hay lista