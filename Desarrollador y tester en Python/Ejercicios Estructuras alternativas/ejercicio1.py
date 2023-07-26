# Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no.
n1=int(input("Elije un número: "))
n2=int(input("Elije otro número: "))

if n1>n2:
    print(f"{n1} es mayor que {n2}")
elif n1==n2:
    print(f"{n1} y {n2} son iguales")
else:
    print(f"{n2} es mayor que {n1}")
