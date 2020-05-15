for valor in range(10):
    print(valor)

for valor in range(1, 20):
    print(valor)

for valor in range(-5, 6):
    print(valor)

for valor in range(1, 101, 2):
    print(valor)

lista = [1, 2, 3, 4, 5, 6]
for indice in range(len(lista)):
    print("indice:", indice, "valor:", lista[indice])

for indice, valor in enumerate(lista):
    print("indice:", indice, "valor:", valor)

for indice, valor in enumerate(lista, 10):
    print("indice:", indice, "valor:", valor)
