# Diseñar el algoritmo correspondiente a un programa, que:
# Crea una tabla bidimensional de longitud 5x5 y nombre ‘diagonal’.
# Carga la tabla de forma que los componentes pertenecientes a la diagonal de la matriz tomen el valor 1 y el resto el valor 0.
# Muestra el contenido de la tabla en pantalla.

tabla_bidimensional = [[], [], [], [], []]

cont = 0
for i in tabla_bidimensional:
    cont += 1
    for n in range(1, 6):
        if n == cont:
            i.append(1)
        else:
            i.append(0)

for l in tabla_bidimensional:
    print(l)
