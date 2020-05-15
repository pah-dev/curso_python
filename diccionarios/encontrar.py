
diccionario = {"a": 1, "b": 2, "c": 3, "a": 4}

resultado = diccionario["a"]
print(resultado)


resultado = "z" in diccionario
print(resultado)

# segundo param es el resultado cuando no existe
resultado = diccionario.get("z", "")
print(resultado)

resultado = diccionario.setdefault("z", {})
print(resultado)
print(diccionario)