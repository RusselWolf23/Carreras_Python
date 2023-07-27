# Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro.
#  Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.

def EsMultiplo(n1, n2):
    if n1%n2==0:
        return True
    else:
        return False

if EsMultiplo(20, 5):
    print("Es múltiplo")
else:
    print("No es múltiplo")
