
class Usuario:

    def __init__(self, username="", email="", nombre=""):
        self.username = username
        self.email = email
        self.nombre = nombre

    def saluda(self):
        return "Hola soy un usuario " + self.nombre

    def mostrar_username(self):
        print(self.username)

    def mostrar_nombre(self):
        print(self.nombre)

    def crear_nombre(self, nombre):
        self.nombre = nombre


codi = Usuario("Codi","pepe@eke.com","Codigo")
#codi.username = "codi"
#codi.email = "codif@gmaol.xom"

facilito = Usuario()
#facilito.username = "facilito"
#facilito.email = "facilitp@gmaol.xom"

print(type(codi))
print(type(facilito))

print(codi.saluda())
print(facilito.saluda())

codi.mostrar_username()
facilito.mostrar_username()

codi.crear_nombre("Codigo")
codi.mostrar_nombre()