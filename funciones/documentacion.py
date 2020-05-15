def mi_funcion(*args):
    """Esta es la documentación de mi_función"""
    print(args)


print(mi_funcion.__doc__)


def suma(a, b):
    """Función suma"""
    return a + b


def resta(a, b):
    """Función resta"""
    return a - b


opciones = {"a": suma, "b": resta}
print("Ingrese la opción deseada")

for opcion, funcion in opciones.items():
    mensaje = "{}) {}".format(opcion, funcion.__doc__)
    print(mensaje)

opcion = input("Opción : ")
