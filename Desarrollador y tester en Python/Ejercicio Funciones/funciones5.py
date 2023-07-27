# Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo.
# Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.

def calcularMaxMin(lista):
    if type(lista)==list:
        return max(lista), min(lista)
    else:
        return "no se ha introducido una lista"

lista=[]

while True:    
    try:
        numero=int(input("Añade un número a la lista: "))
        lista.append(numero)
    except ValueError:
        break


print(calcularMaxMin(lista))
