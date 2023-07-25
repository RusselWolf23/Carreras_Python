# Calcular el perímetro y área de un rectángulo dada su base y su altura.

base = float(input("¿Cuál es la base del rectángulo?"))
altura = float(input("¿Cuál es la altura del rectángulo?"))

area = (base*altura)/2

perimetro = 2*base + 2*altura

print(f"El área del rectángulo es {area} y su perímetro es {perimetro}")
