curso = "Curso de Python"

length = len(curso)
print(length)

resultado = curso[1:16:2]
print(resultado)

# los strings no se pueden modificar una vez declarados
# curso[-1] = "4"
# print(curso)

curso = "c" + curso[1:] + " " + str(3) + " " + "en Codi"
print(curso)
