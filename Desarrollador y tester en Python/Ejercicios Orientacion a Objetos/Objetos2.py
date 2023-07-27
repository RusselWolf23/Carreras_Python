# Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales).
# El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:

# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, solo ingresando o retirando dinero.
# mostrar(): Muestra los datos de la cuenta.
# ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
# retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

from Objetos1 import Persona


class Cuenta():

    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, value):
        self._titular = value

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, value):
        self._cantidad = value

    def mostrar(self):
        return str(f"{self.titular.mostrar()}\nCantidad: {self.cantidad}")

    def ingresar(self, importe):
        if importe > 0:
            self.cantidad += importe

    def retirar(self, cant_retirar):        
        self.cantidad -= cant_retirar

def main():
    pers=Persona("Manuel", 62, "01020304")

    banco=Cuenta(pers, 23233.32)

    print(banco.mostrar())  

    banco.ingresar(2000)

    print(banco.cantidad)

    banco.retirar(25240.32)

    print(banco.cantidad)


if __name__ == '__main__':
    main()
