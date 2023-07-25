# Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos)
# después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).

monedas_dos_eur = int(input("Número de monedas de 2€:"))*2

mon_1eur = int(input("Número de monedas de 1€:"))

mon_50cen = float(input("Número de monedas de 50 céntimos:"))/2

mon_20cent = float(input("Número de monedas de 20 céntimos:"))*20/100

mon_10cent = float(input("Número de monedas de 10 céntimos:"))/10

dinero_total = monedas_dos_eur+mon_1eur+mon_50cen+mon_20cent+mon_10cent

print(f"Posees un total de {dinero_total}€")
