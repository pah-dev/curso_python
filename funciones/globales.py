animal = "Leon"  # Variable global


def mostrar_animal():
    global animal  # para trabajar con la misma variable
    # son variables diferentes al asig un nuevo valor
    animal = "Ballena"  # Variable local
    print(animal)


mostrar_animal()
print(animal)
