class Felino:

    def es_domestico(self):
        return True

    def grito(self):
        return "zZzZzZzZz"

    def tiene_garras(self):
        return True

    def tiene_colmillos(self):
        return True


class Gato(Felino):
    pass


class Leon(Felino):
    pass


mi_gato = Gato()
print("Mi gato es domestico {} y tiene garras {}".format(
    mi_gato.es_domestico(), mi_gato.tiene_garras()))
