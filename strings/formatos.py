texto = "  curso de Python 3   "

resultado = texto.capitalize()
print(resultado)

resultado = texto.swapcase()
print(resultado)

resultado = texto.upper()
print(resultado)
print(resultado.isupper())

resultado = texto.lower()
print(resultado)
print(resultado.islower())

resultado = texto.title()
print(resultado)

# tercer valor es cant de remplazos
resultado = texto.replace("3", "4", 1)
print(resultado)

# clasico trim
resultado = texto.strip()
print(resultado)


curso = "Python"
version = "3"

resultado = "Curso de %s %s" % (curso, version)
print(resultado)

resultado = "Curso de {} {}".format(curso, version)
resultado = "Curso de {a} {b}".format(b=version, a=curso)
print(resultado)
