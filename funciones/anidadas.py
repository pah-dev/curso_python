
def comenzar_playlist(lista):

    def reproducir():
        nonlocal    # para poder modificar la lista
        lista = [1,2,3]
        for valor in lista:
            print(valor)

    reproducir()
    print(lista)


lista = ["track 1","track 2","track 3","track 4"]
comenzar_playlist(lista)