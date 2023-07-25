# Calcular la media de tres números pedidos por teclado.

def media(n1, n2, n3):
    # if type(n1,n2,n3)==int:
    return float((n1+n2+n3)/3)


n1 = int(input("Escribe el primer número:"))
n2 = int(input("Escribe el segundo número:"))
n3 = int(input("Escribe el tercer número:"))

print("La media de los tres números es: %.1f" % media(n1, n2, n3))
