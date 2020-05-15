diccionario = {}

# agregar una llave con su valor
diccionario["nombre"] = "Codi"
print(diccionario)

valor = diccionario["nombre"]
print(valor)

diccionario["nombre"] = 90
print(diccionario)

# no pueden existir llaves duplicadas
# muestra a=4
diccionario = {"a": 1, "b": 2, "c": 3, "a": 4}
print(diccionario)
