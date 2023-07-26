# Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo
# que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.

A=int(input("Escribe un número (A)"))
B=int(input("Escribe un número (B)"))

aux=A
A=B
B=aux

print(f"Ahora A={A} y B={B}")