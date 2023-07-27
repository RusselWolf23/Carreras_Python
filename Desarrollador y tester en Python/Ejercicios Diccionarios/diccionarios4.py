# Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase 
# y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guarda la información en un diccionario 
# cuya claves serán los nombres de los alumnos
#  y los valores serán listas con las notas de cada alumno.
# El programa pedirá el número de alumnos que vamos a introducir,
# pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo. 
# Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos. 
# Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.

clase={}

num_alumnos=int(input("¿Cuántos alumnos hay?"))

for n in range(1,num_alumnos+1):
    alumno=input("Nombre del alumno: ")
    clase[alumno]=[]
    nota=0
    while nota>=0:
        nota=int(input("Nota: "))
        if nota>=0:
            clase[alumno].append(nota)

for clave, valor in clase.items():
    print(f"{clave}| Nota media:{sum(valor)/len(valor)}")