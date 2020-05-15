
# = es valor por defecto
def crear_usuario(nombre, apellido="", edad=18):
    return {
        "nombre": nombre,
        "apellido": apellido,
        "nombre_completo": "{} {}".format(nombre, apellido),
        "edad": edad,
    }

codi = crear_usuario("Jean", "Paul", "31")

print(codi["nombre_completo"])
print(codi["edad"])


codi = crear_usuario(edad=31, apellido="Pepe", nombre="Juan")

print(codi["nombre_completo"])
print(codi["edad"])
