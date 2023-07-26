# Suponiendo que hemos introducido una cadena por teclado que representa una frase
#  (palabras separadas por espacios), realiza un programa que cuente cuantas palabras tiene.

frase = input("Escribe una frase: ")

print(f"la frase '{frase}' tiene {len(frase.split())} palabras")
