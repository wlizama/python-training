class Persona():

    # Constructor
    def __init__(self, nombre, edad, sexo):
        self._nombre = nombre
        self._edad = edad
        self._sexo = sexo

    # Definicion de propiedades getter y setter
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        self._edad = value

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, value):
        self._sexo = value


objPersona = Persona("Wilder", 45, "M")
print("{} tiene {} años y es de sexo: {}".format(
    objPersona.nombre, objPersona.edad, objPersona.sexo))
# objPersona.nombre = "Wily Colon"
# print(objPersona.nombre)
# print(objPersona.__dict__)
