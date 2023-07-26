# Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.

mes=int(input("Elije un mes (Numérico 1-12): "))


if mes==2:
    dias=28
elif mes%2==0:
    dias=30
else:
    dias=31

if mes>0 and mes<13:
    print(f"El mes {mes} tiene {dias} dias")
else:
    print("El mes no es correcto")