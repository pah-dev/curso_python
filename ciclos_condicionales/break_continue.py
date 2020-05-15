
titulo = "Curso de Python 3"

for caracter in titulo:
    if caracter == "P":
        break # Termina en P
    print(caracter)

    
for caracter in titulo:
    if caracter == "P":
        continue # no imprime P
    print(caracter)