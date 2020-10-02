class Animal:
    def __init__(self, nombre, onomatopeya): #Constructor, objetos instancian propiedades automaticamente al ser creados
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print("Hola, soy ",self.nombre,", soy un ", self.tipo," y mi sonido es el ", self.onomatopeya)

class Gato(Animal):
    tipo = "gato"
    def __init__(self, nombre, onomatopeya): #El constructor de la clase hijo, omite el de la clase padre
        Animal.__init__(self, nombre, onomatopeya) #Se debe hacer referencia al padre junto con los parametros
        print("hola, soy un gato extendido") #Se ejecuta con la creacion del objeto

class Perro(Animal):
    tipo = "perro"
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya) #Otra manera de extender el self de la clase padre es llamar a super() junto con sus parametros
        print("Instanciando un perro") #Se ejecuta con la creacion del objeto

gato = Gato("Javier", "maullido")
perro = Perro("Calisio", "ladrido")

#gato.saludo()
#perro.saludo()


#class Usuario:      #definimos la clase, el objeto creado 
#    nombre = "Bruno" #definimos las propiedades
#    apellido = "Puca"
#
#usuario = Usuario() #llamamos a la clase como si fuese una funcion, la instanciamos para utilizarla
#print(usuario.nombre, usuario.apellido) #accedemos a la propiedad de la clase


#class Usuario:
#    def __init__(self, nombre, apellido): #Asi se crean objetos de usuario con distintos valores
#        self.nombre = nombre
#        self.apellido = apellido
    
#    def saludo(self):
#        print("Hola soy: ", self.nombre, self.apellido)

#class Admin(Usuario): #clase Admin hereda de clase Usuario
#    def superSaludo(self):
#        print("Hola soy: ", self.nombre, self.apellido, " y soy administrador")

#usuario1 = Usuario("Bruno", "Puca")
#usuario1.saludo()
#'del usuario1.nombre' elimina la propiedad
#usuario1.nombre = "Carlos" #Se puede cambiar la propiedad sin necesidad de ir a la instancia del objeto
#usuario1.saludo()
#'del usuario1' elimina el objeto completo
#admin1 = Admin("Super", "Administrador")
#a#min1.superSaludo()

