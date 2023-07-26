# Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.
# Ejemplo, si se introduce 23 que muestre 32.

def numero_inverso(numero):
    if(numero<10 or numero>99):
        return "El número debe ser de dos cifras"
    else:
       return str(numero)[1]+str(numero)[0]

print(numero_inverso(int(input("Escribe un número de dos cigras:"))))