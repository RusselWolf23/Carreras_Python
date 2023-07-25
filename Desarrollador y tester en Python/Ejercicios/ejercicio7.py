# Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
# Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

time = int(input("Indica una cantidad de tiempo en minutos:"))

horas = int(time/60)
minutos = int(time % 60)

print(f"{time} minutos son {horas} horas y {minutos} minutos")
