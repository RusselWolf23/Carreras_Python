# Escribe un programa python que pida un número por 
# teclado y que cree un diccionario cuyas claves sean desde el número 1 hasta el número indicado,
#  y los valores sean los cuadrados de las claves.

limite=int(input("Escribe el número límite del diccionario"))

diccionario={}

for n in range(1, limite+1):
    diccionario[n]=n**2

print(diccionario)