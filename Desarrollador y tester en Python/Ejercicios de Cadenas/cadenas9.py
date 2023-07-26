# Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.

cad1=input("Escribe una frase: ")
cad2=input("Escribe otra palabra: ")

if cad2 in cad1:
    print(f"|{cad1}| contiene {cad2}")
else:
    print(f"|{cad1}| NO contiene {cad2}")
