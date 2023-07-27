# Crea un función EscribirCentrado, que reciba como parámetro un texto y lo escriba centrado en pantalla
# (suponiendo una anchura de 80 columnas;
#  pista: deberás escribir 40 - longitud/2 espacios antes del texto). Además subraya el mensaje utilizando el carácter =.

def EscribirCentrado(texto):
    posicion = int(40-len(texto)/2)

    for n in range(1, 81):
        print("=", end="")
        if n == posicion:
            print(texto, end="")


EscribirCentrado("Frase escrita por mí")
