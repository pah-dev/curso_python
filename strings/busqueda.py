mensaje = (
    "Este es un texto un poco grande en cuanto a longitud de caracteres se refiere"
)

resultado = mensaje.count("texto")
print(resultado)


resultado = mensaje.count("e")
print(resultado)


resultado = "texto" in mensaje
print(resultado)


resultado = mensaje.find("texto")
print(resultado)

resultado = mensaje[resultado : resultado + len("texto")]
print(resultado)

resultado = mensaje.startswith("texto")
print(resultado)

resultado = mensaje.endswith("texto")
print(resultado)
