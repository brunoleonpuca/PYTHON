#c = open('chanchito.txt', 'w') #open('.txt', '[r]ead/[a]ppend/[w]rite/[x]') -> permisos para leer, añadir, escribir, crear
#print(c.read()) #devuelve todo el archivo
#print(c.readline()) #devuelve linea del archivo
#c.write("\nagregamos otra linea a nuestro archivo")


#for x in c:
#    print(x) #devuelve cada una de las lineas del archivo

#c.close() #cierra el archivo por medida de seguridad, buena practica

#x = open('chanchito.txt')
#print(x.read())

import os

if os.path.exists("chanchito.txt"):
    os.remove("chanchito.txt")
else:
    print("archivo no existe")

os.rmdir("carpeta a eliminar")