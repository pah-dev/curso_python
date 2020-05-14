cursos = ["python", "django", "flask", "C", "C++", "C#", "java", "php"]

# curso = cursos[3]

# negativo para recorrer a la inversa
curso = cursos[-1]
print(curso)

# sublista
sub = cursos[0:3]
# sub = cursos[:3] desde 0
# sub = cursos[2:] hasta el final
print(sub)

sub = cursos[1:7:2]  # salto de 2 en 2
print(sub)

# lista inversa
sub = cursos[::-1]
print(sub)
