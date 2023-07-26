# Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.

for n in range(1, 6):

    for n1 in range(1, 11):
        print(f"{n}x{n1}={n*n1}")
        if n1==10: 
            print("\n")
