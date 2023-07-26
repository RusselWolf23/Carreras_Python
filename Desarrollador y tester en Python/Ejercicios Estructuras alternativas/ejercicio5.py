# Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe”
# y “asdasd” se indica “Has entrado al sistema”, sino se da un error.

usuario = input("Escribe el nombre del usuario: ")
contraseña = input("Escribe la contraseña: ")

if usuario == "pepe" and contraseña == "asdasd":
    print("Has entrado al sistema")
else:
    print("Error al introducir usuario o la contraseña")
