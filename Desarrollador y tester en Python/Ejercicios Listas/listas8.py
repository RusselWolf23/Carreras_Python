# Queremos guardar los nombres y la edades de los alumnos de un curso. Realiza un programa que introduzca el nombre y la edad de cada alumno. 
# El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos:
# Todos lo alumnos mayores de edad.
# Los alumnos mayores (los que tienen más edad)

nombres=[]
edades=[]

dato=""

while dato!="*":
    dato=input("Escribe el nombre del alumno: ")
    if dato=="*":
        break
    nombres.append(dato)
    dato=input("Escribe la edad del alumno: ")
    if dato=="*":
        del nombres[-1]
        break
    edades.append(int(dato))

print("\n__Mayores de edad__ ")
for nombre, edad in zip(nombres, edades):
    if edad>=18:
        print(f"Nombre:{nombre} edad:{edad}")

mayor=nombres[edades.index(max(edades))]

print(f"Alumno de mayor edad: {mayor} {max(edades)} años")

