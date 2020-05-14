tupla = (1, 2, 3, 4)
# uno, dos, tres, cuatro = tupla[0], tupla[1], tupla[2], tupla[3]
# se puede hacer asi porque  cantidad elem =  cant variables
uno, dos, tres, cuatro = tupla

print(uno)
print(dos)
print(tres)
print(cuatro)


tupla_dos = (1, 2, 3, 4, 5, 6)

# pone los ultimos elem en la ultima variable
uno, dos, tres, *cuatro = tupla_dos

print(uno)
print(dos)
print(tres)
print(cuatro)

uno, *dos, cinco, seis = tupla_dos
print(uno)
print(dos)
print(cinco)
print(seis)


lista = [10, 20, 30, 40]
resultado = zip(tupla, lista, tupla_dos)
resultado = tuple(resultado)
resultado = list(resultado)

print(resultado)

# guion bajo para ignorar elementos
tupla_tres = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400)
primero, segundo, *_, ultimo = tupla_tres
print(primero)
print(segundo)
print(ultimo)
