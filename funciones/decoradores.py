
# a, b, c
# a(b) -> c  formula de decoradores
# formula a recibe a funcion b y retorna funcion c

def decorador(funcion):
    def nueva_funcion():
        print("Podemos agregar codigo antes")
        funcion()
        print("Podemos agregar codigo despues")
    return nueva_funcion

@decorador
def funcion_a_decorar():
    print("Esta es una funcion a decorar")

funcion_a_decorar()



def decorador(funcion):
    def nueva_funcion(*args,**kwargs):
        print("Podemos agregar codigo antes")
        resultado = funcion(*args,**kwargs)
        print("Podemos agregar codigo despues")
        return resultado

    return nueva_funcion

@decorador
def suma(val1,val2):
    return val1+val2

funcion_a_decorar()

resultado = suma(10,20)
print(resultado)