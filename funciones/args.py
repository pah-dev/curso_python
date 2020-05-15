

def suma(param_req,*args):
    total = 0
    print(param_req)
    for valor in args:
        total+=valor
    return total

resultado = suma("Arg requerido",10,20,30,40,50,60,70,80)
print(resultado)


def usuarios_autenticados(**kwargs):
    print(kwargs)

usuarios_autenticados(codi=True, facilito=False)

def combinacion(requerido, *args,**kwargs):
    print(requerido)
    print(args)
    print(kwargs)

combinacion("Valor requerido", 10,20,30,40, valor1=False, valor2=True)