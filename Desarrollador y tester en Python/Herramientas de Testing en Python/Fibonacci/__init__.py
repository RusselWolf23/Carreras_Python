
def sucesion(limite):
    n = [1, 1]
    while n[-1] + n[-2] <= limite:
        n.append(n[-1] + n[-2])
    return n
n = ""
while True:
    
    try:
        n = int(input("Escribe un número: "))
        break
    except ValueError:
        print("no es un número")

print(sucesion(n))
