# Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. 
# Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.

lista=[]
for p in range(1, 6):
    lista.append(input("Añade una palabra a la lista"))

lista_invertida=lista[::-1]

print(lista_invertida)