# Una persona adquirió un producto para pagar en 20 meses.
# El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. 
# Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total de
# lo que pagó después de los 20 meses.

pago=10
total=10

for n in range(1,21):
    print(f"Mes {n}:\n\tPago: {pago}€\n")   
    pago+=pago
    total+=pago

print(f"Pagó en total {total}€")