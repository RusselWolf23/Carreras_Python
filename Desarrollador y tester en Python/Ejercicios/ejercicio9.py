# Una tienda ofrece un descuento del 15% sobre el total de la compra
# y un cliente desea saber cuanto deberá pagar finalmente por su compra.

precio_producto=float(input("¿Cuanto cuesta el producto?"))

precio_final=precio_producto-precio_producto*15/100
print(f"El precio final de la compra aplicando el 15% de descuento es de:{precio_final}€")