variable_uno = 10
variable_dos = 18

mayor = variable_uno > variable_dos
menor = variable_uno < variable_dos
mayor_igual = variable_uno >= variable_dos
menor_igual = variable_uno <= variable_dos
# igual = variable_uno == variable_dos
# PARA VALORES ENTEROS SE PUEDE USAR is
igual = variable_uno is variable_dos
diferente = variable_uno != variable_dos

print(mayor)
print(menor)
print(mayor_igual)
print(menor_igual)
print(igual)
print(diferente)

resultado = True and False and diferente
resultado = True or False or diferente
resultado = not True

print(resultado)
