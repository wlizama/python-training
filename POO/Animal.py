class Felino:

    def __init__(self, grito):
        self._grito = grito

    @property
    def grito(self):
        return self._grito

    @grito.setter
    def grito(self, value):
        self._grito = value

    def tiene_garras(self):
        return True

    def tiene_colmillos(self):
        return True


class Gato(Felino):

    def __init__(self, grito, es_domestico, nombre):
        super().__init__(grito)
        self._es_domestico = es_domestico
        self._nombre = nombre

    @property
    def es_domestico(self):
        return self._es_domestico

    @es_domestico.setter
    def es_domestico(self, value):
        self._es_domestico = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    def tiene_flojera(self):
        return True


class Leon(Felino):

    def __init__(self, grito, color_melena):
        super().__init__(grito)
        self._color_melena = color_melena

    @property
    def color_melena(self):
        return self._color_melena

    @color_melena.setter
    def color_melena(self, value):
        self._color_melena = value


mi_gato = Gato("meaw", True, "Rasputin")
print("Mi gato se llama: {} y cuando tiene hambre dice \"{}\"".format(
    mi_gato.nombre, mi_gato.grito))
print(" tiene garras: {}".format(mi_gato.tiene_garras()))
print(" tiene colmillos: {}".format(mi_gato.tiene_colmillos()))
print(" es domestico: {}".format(mi_gato.es_domestico))
print(" tiene flojera: {}".format(mi_gato.tiene_flojera()))

print()

un_leon = Leon("grawwww", "negro")
print("En el zoologico hay un león que tiene una melena color: {}, cuando nos \
acercamos el grita \"{}\"".format(
    un_leon.color_melena, un_leon.grito))
print(" tiene garras: {}".format(un_leon.tiene_garras()))
print(" tiene colmillos: {}".format(un_leon.tiene_colmillos()))
