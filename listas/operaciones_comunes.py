lista = [8.17, 90, 1, 5, 44, 1.32]

lista.sort()
lista.sort(reverse=True)

mayor = lista[0]

print(lista)
print(mayor)

menor = min(lista)
mayor = max(lista)
longitud = len(lista)

resultado = 8.17 in lista
indice = lista.index(8.17)
print(resultado)
print(indice)

contador = lista.count(8.17)
