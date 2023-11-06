# Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuentaJoven que deriva de la anterior.
# Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada
# en tanto por ciento.Construye los siguientes métodos para la clase:

# Un constructor.
# Los setters y getters para el nuevo atributo.
# En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad.,
#  por lo tanto hay que crear un método esTitularValido() que devuelve verdadero
#  si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
# Además la retirada de dinero sólo se podrá hacer si el titular es válido.
# El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
# Piensa los métodos heredados de la clase madre que hay que reescribir.

from Objetos1 import Persona
from Objetos2 import Cuenta


class CuentaJoven(Cuenta):

    def __init__(self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self._bonificacion

    @bonificacion.setter
    def bonificacion(self, value):
        self._bonificacion = value

    def esTitularValido(self):
        return 18 <= self.titular.edad <= 25

    def retirar(self, cant_retirar):
        if self.esTitularValido():
            super().retirar(cant_retirar)
        else:
            return str("Titular no válido")

    def mostrar(self):
        return str(f"__Cuenta Joven__\n {super().mostrar()}\nBonificacion:{self.bonificacion}%")


def main():
    cuentaJoven = CuentaJoven(Persona("Pepe", 23, 34678900), 12000, 12)

    print(cuentaJoven.mostrar())

    cuentaJoven.ingresar(2000)

    print("Saldo:", cuentaJoven.cantidad)

    cuentaJoven.retirar(10000)

    print("Saldo:", cuentaJoven.cantidad)


if __name__ == '__main__':
    main()
