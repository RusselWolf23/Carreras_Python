def intro_numero()->int:
    n=0
    while True:
        user_input = input("Ingrese un número entero: ")
        if user_input.isdigit():
            # La cadena representa un número entero
            n = int(user_input)
            break
        else:
            print("Error. Por favor, ingresa un número entero válido.")
    return n

def intro_operador():
    while True:
        operador = input("Introduce un operador (sum, rest, mult, div): ")
        if operador in _OPERADOR:
            return _OPERADOR[operador]
        else:
            print("Operador incorrecto. Por favor, elige un operador válido.")

def calculando():
    n1=intro_numero()
    print("seguimos")
    n2=intro_numero()
    operador=intro_operador()
    result=eval(f"{n1}{operador}{n2}")
    return f"el resultado es", result

def calcular(n1:int, operador, n2:int)->str:
    try:
        expresion=f"{n1}{operador}{n2}"
        result=eval(expresion)
        return f"{expresion}={result}"
    except KeyError:
        raise InvalidOperation("Operacion no válida")
    except:
        print("Operacion no válida, indefinida")
    return ""


_OPERADOR={
    "sum":"+",
    "rest":"-",
    "mult":"*",
    "div":"/"
    }

# print(_OPERADOR["sum"])

print(calcular(22,"+",11))


