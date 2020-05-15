class Animal:
    def comer(self):
        print("Comiendo")

    def dormir(self):
        print("Durmiendo")

    def comun(self):
        print("Es un metodo de Animal")


class Mascota:
    def fecha_adopcion(self, fecha):
        self.fecha_de_adopcion = fecha

    def comun(self):
        print("Es un metodo de Mascota")


class Perro(Animal, Mascota):
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print("Ladrando")

    def comun(self):
        print("Es un metodo de Perro")

    # sobreescribo el metodo del padre
    def dormir(self):
        print(self.nombre, "esta durmiendo")
        # si necesito al del padre lo llamo asi
        Animal.dormir(self)
        print("No molestar")


class Gato(Animal, Mascota):
    def ronronear():
        print("ronroneando")


perro = Perro("Firulais")
""" 
perro.ladrar()
perro.dormir()
perro.comer()
 """
perro.fecha_adopcion("Hoy")
print(perro.fecha_de_adopcion)

# busca primero el metodo en la clase luego en los padres
perro.comun()
perro.dormir()
