# El día juliano correspondiente a una fecha es un número entero que indica los días que han transcurrido
# desde el 1 de enero del año indicado. Queremos crear un programa principal que al introducir una fecha
# nos diga el día juliano que corresponde. Para ello podemos hacer las siguientes subrutinas:

# LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
# DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
# EsBisiesto: Recibe un año y nos dice si es bisiesto.
# Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano.

def LeerFecha():
    while True:
        try:
            dia = int(input("Escribe el día (1-31): "))
            mes = int(input("Escribe el mes (1-12): "))
            ano = int(input("Escribe el año: "))
            if 1 <= dia <= 31 and 1 <= mes <= 12 and ano > 0:
                return dia, mes, ano
            else:
                print("Fecha inválida. Por favor, ingrese una fecha válida.")
        except ValueError:
            print("Error al leer la fecha. Solo valores numéricos.")


def DiasDelMes(mes, ano):
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mes == 2 and EsBisiesto(ano):
        return 29
    return dias_por_mes[mes - 1]


def EsBisiesto(ano):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        return True
    return False


def Calcular_Dia_Juliano(dia, mes, ano):
    dias_totales = 0
    for i in range(1, mes):
        dias_totales += DiasDelMes(i, ano)
    dias_totales += dia
    return dias_totales


print("Calculadora de Día Juliano")
dia, mes, ano = LeerFecha()
dia_juliano = Calcular_Dia_Juliano(dia, mes, ano)
print(
    f"El día juliano correspondiente a la fecha {dia}/{mes}/{ano} es: {dia_juliano}")


