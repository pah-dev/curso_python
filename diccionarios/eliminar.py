
diccionario = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}

print(diccionario)
print(len(diccionario))

del diccionario["a"]

print(diccionario)
print(len(diccionario))

valor = diccionario.pop("b")

print(valor)
print(diccionario)
print(len(diccionario))

# vacia el diccionario
diccionario = {}
diccionario.clear()
