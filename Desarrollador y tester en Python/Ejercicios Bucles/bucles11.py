# Escribe un programa que diga si un número introducido por teclado es o no primo. 
# Un número primo es aquel que sólo es divisible entre él mismo y la unidad.
# Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.

n=int(input("Elije un número: "))
cont=0
for num in range(n, 0, -1):
    if n%num==0:
        cont+=1
    if cont>2:
        break
if cont>2:
    print(f"El número {n} no es primo")
else:
    print(f"El número {n} es primo")
    