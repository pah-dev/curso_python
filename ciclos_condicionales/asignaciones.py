
calificacion = input("Calificacion?\n")

color = "rojo"
if int(calificacion) >=7:
    color = "verde"
print(calificacion, color)

color = "verde" if int(calificacion) >=7 else "rojo"
print(calificacion, color)