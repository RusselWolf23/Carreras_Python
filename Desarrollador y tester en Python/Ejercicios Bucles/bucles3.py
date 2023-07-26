# Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.

acum=0
cont=0
num=1
while num!=0:
    num=int(input("Añade un numero: (pulsa 0 para salir)"))
    acum+=num
    cont+=1 if num!=0 else 0

if acum!=0:
    print(f"Suma de los números: {acum}\nMedia: {acum/cont}")
else:
    print(f"Suma de los números: {acum}\nMedia: 0")
