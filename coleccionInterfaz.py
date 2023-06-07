from zope.interface import Interface

class IColeccion(Interface):

    def insertarElemento(self, vehiculo, posicion):
        pass

    def agregarElemento(self, vehiculo):
        pass

    def mostrarElemento(self, posicion):
        pass