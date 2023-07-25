# Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas,
# el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las
# tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

sueldo_base = int(input("¿Cuánto gana el vendedor de sueldo base?"))
comisiones = sueldo_base/10*3

print(f"El vendedor gana {comisiones}€ de comisión y un total de {sueldo_base + comisiones}€ al mes")
