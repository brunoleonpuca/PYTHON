"""STRINGS (Cadenas de caracteres) ejemplos: dia="Lunes", msg="Hola mundo" """
#cadena cruda#ruta = r"c:\\nuevo\datos.txt" -> print(ruta) -> "c:\\nuevo\datos.txt"

#ACCEDER A DATO
#print(dia[2]) -> "n"
#print(dia[1:3]) -> "un"

#MULTIPLICARLAS
#print(dia*3) -> "LunesLunesLunes"

#FUNCIONES COMUNES
#print(len(dia)) -> "5"
#if "es" in dia: -> True
#if "ah" not in dia: -> True
#max
#min
#index
#count

#FUNCION PARA DAR VUELTA UN STRING
#stringQueDeboDarVueltaa[::-1]

#METODO STR PARA IMPRIMIR NUMEROS EN CADENAS

#DIVIDIR CADENAS
#b = msg.split() -> print(b) -> "['Hola', 'mundo']"
#b = msg.split(" ") -> print(b) -> "['Hola',' ','Mundo']"
#b,c = msg.split() -> print(b);print(c) -> "['Hola'] ['Mundo']"
#UNIR CADENAS CON UN ELEMENTO
#b = "3".join(msg)

m = ",".join("Hola mundo")
print(m)