
def saludar():
    print("Hola Mundo")

saludar()

def crear_mensaje(nombre):
    return "Hola {}, bienvenido al curso de Python 3".format(nombre)

def suma(val1,val2,val3):
    return val1+val2+val3

def obtener_curso():
    return "Curso de Python", "Basico", 3.8

nuevo_mesaje = crear_mensaje("Eduardo")
print(nuevo_mesaje)

resultado = suma(10,20,30)
print(resultado)

curso, nivel, version = obtener_curso()
print(curso, nivel, version)