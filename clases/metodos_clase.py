class Circulo:
    pi = 3.14159

    @classmethod
    def area(cls, radio):
        return cls.pi * radio ** 2


resultado = Circulo.area(20)
print(resultado)
