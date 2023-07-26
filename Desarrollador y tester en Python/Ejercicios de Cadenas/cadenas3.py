# Pide una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas veces aparece el carácter en la cadena.

cad=input("Escribe una palabra: ")

caracter="caracter"

while len(caracter)>1:
    caracter=input("Escribe una letra: ")
    if len(caracter)>1:
        print("el caracter no es válido")

cont=0

for letra in cad:
    if letra==caracter:
        cont+=1
print(f"El caracter {caracter} aparece {cont} veces en la palabra {cad}")