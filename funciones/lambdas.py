
def centigrados_a_farhenheit(grados):
    return grados * 1.8 + 32

# se asig funcion a una variable
funcion_variable = centigrados_a_farhenheit
resultado = funcion_variable(32)
print(resultado)



mi_funcion = lambda grados=0 : grados * 1.8 + 32

resultado = mi_funcion(32)
print(resultado)


# diferentes formas de funcion lambda
sin_parametros = lambda : True

con_valores = lambda val, val1=10, val2=10 : val + val1 + val2

con_asterisco = lambda *args : args[0]

con_doble_asterisco = lambda **kwargs : args[0]

con_asteriscos = lambda *args , **kwargs : kwargs.get('key', False)