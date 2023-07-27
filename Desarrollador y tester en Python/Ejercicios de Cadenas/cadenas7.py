# Pide una cadena y dos caracteres por teclado (valida que sea un carácter),
#  sustituye la aparición del primer carácter en la cadena por el segundo carácter.

cad=input("Escribe una palabra: ")

char1="caracter"
char2="caracter"

while len(char1)>1:
    char1=input("Escribe una letra: ")
    if len(char1)>1:
        print("el caracter no es válido")

while len(char2)>1:
    char2=input("Escribe una letra: ")
    if len(char2)>1:
        print("el caracter no es válido")

nueva_cad=cad.replace(char1, char2)

print(nueva_cad)