# Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas. 
# El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y 
# nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario. Si la fruta no existe nos dará un error. 
# Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.

frutas={"manzana":0.5, "pera":0.35, "platano":1.0, "naranja":1.25, "aguacate":0.9}

salir=False

while not salir:
    fruta=input("Elige una fruta: ").lower()

    if fruta not in frutas:
        print("la fruta no existe")
        break

    cantidad=int(input(f"¿Cuant@s {fruta}s se han vendido? "))
 
    print(f"El precio total de l@s {fruta}s es de {frutas.get(fruta)*cantidad}€")
    
    salir=True if input("¿desea salir?(S/N)").upper()=="S" else False

