# Crea una aplicación que pida un número y calcule su factorial 
# (El factorial de un número es el producto de todos los enteros entre 1 y el propio número
#  y se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120),

def factorial(num):
    fact=1
    for n in range(1,num+1):
        fact=fact*n
    print(f"!{num}={fact}", end="")

num=int(input("Elije un número: "))

factorial(num)

# for var in range(0,21, 5):
#     print(var," ", end="\n")