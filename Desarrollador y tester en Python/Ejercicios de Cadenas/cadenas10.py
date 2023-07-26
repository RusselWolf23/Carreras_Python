# Introducir una cadena de caracteres e indicar si es un palíndromo.
#  Una palabra palíndroma es aquella que se lee igual adelante que atrás.

cad = input("Escribe una palabra: ")

if cad == cad[::-1]:
    print(cad, " es un palíndromo")
else:
    print(cad, " NO es un palíndromo")
