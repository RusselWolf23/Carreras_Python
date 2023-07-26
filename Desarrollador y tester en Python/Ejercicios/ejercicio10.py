# Un alumno desea saber cual será su calificación final en la materia de Algoritmos.
# Dicha calificación se compone de los siguientes porcentajes:

# 55% del promedio de sus tres calificaciones parciales.
# 30% de la calificación del examen final.
# 15% de la calificación de un trabajo final.

parciales = float(input("Nota final de los parciales:"))*55/100

examen_final = float(input("Nota examen final:"))*30/100

trabajo = float(input("Nota del trabajo final:"))*15/100

print(f"Tu calificación final para la asignatura de Algoritmos es de:{(parciales+examen_final+trabajo)}")
