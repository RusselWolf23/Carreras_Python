# Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.
import time
import os

horas=0
minutos=0
segundos=0

while horas<2:
    print("%02d:%02d:%02d" %(horas,minutos, segundos))
    time.sleep(1)
    segundos+=1
    if segundos>59:
        segundos=0
        minutos+=1
    if minutos>59:
        minutos=0
        horas+=1
    os.system("cls")

