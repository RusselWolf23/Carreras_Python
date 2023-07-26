# Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero,
# o un mensaje de aviso en caso contrario.

n1=int(input("Elije un número: "))
n2=int(input("Elije otro número: "))

if n2!=0:
    print(f"{n1} entre {n2} es {n1/n2}")
else:
    print(f"Nungún número se puede dividir entre 0")

