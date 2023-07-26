# Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100.
#  A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido,
# a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número
#  (además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número que había generado.
import random

num = random.randint(1, 100)
eleccion = 0
intentos = 10
max_ = 100
min_ = 0

while intentos > 0:
    eleccion = int(input(
        f"{num}Intenta adivinar el número (entre {min_}-{max_})\n(intentos {intentos})"))
    intentos -= 1
    if eleccion > num:
        print(f"El número que buscas es menor que {eleccion}")
        max_ = eleccion if eleccion < max_ else max_
    elif eleccion<num:
        print(f"El número que buscas es mayor que {eleccion}")
        min_ = eleccion if eleccion > min_ else min_
    else:
        break


if num != eleccion:
    print("no has acertado, el número era", num)
else:
    print("¡ENHORABUENA! el número era", num)

