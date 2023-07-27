# Escribe un programa que lea una cadena y devuelva un diccionario
# con la cantidad de apariciones de cada carácter en la cadena.

diccionario={}

palabra=input("Escribe una palabra: ")

for l in palabra:
    if l not in diccionario:
        diccionario[l]=palabra.count(l)

print(f"Apariciones de cada letra en la palabra '{palabra}'")

print(diccionario)