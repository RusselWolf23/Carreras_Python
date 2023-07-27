# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10).
#  A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

notas=[]

for i in range(1, 6):
    notas.append(int(input("escribe una calificación")))

print(notas)

media=sum(notas)/len(notas)

print(f"Nota media: {media}")

print(f"Nota más alta: {max(notas)}")

print(f"Nota más baja: {min(notas)}")
