# Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# mostrar(): Muestra los datos de la persona.
# esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:
    def __init__(self, nombre="", edad=0,DNI=""):
        self.mombre=nombre
        self.edad=edad
        self.DNI=DNI

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre=value
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, value):
        if type(value)==int:
            self.__edad = value
        else:
            print("Valor inválido de edad")
            self.__edad=0

    @property
    def DNI(self):
        return self.__DNI

    @DNI.setter
    def DNI(self, value):
        if len(str(value))==8:
            self.__DNI = value
        else:
            print("El DNI introducido es incorrecto")
            self.__DNI="00000000"

    def mostrar(self):
        return str(f"Nombre:{self.mombre}\nEdad:{self.edad}\nDNI:{self.DNI} ")

    def esMayorDeEdad(self):
        if self.edad>=18:
            return True
        else:
            return False

def main():    
    pers=Persona("Juan", 21, 20899199)
    print(pers.mostrar())
  
    if pers.esMayorDeEdad():
        print("es mayor de edad")
    else:
        print("no es mayor de edad")



if __name__ == '__main__':
    main()
