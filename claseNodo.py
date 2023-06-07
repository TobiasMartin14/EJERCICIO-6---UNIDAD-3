from claseVehiculo import Vehiculo
from claseNuevo import Nuevo
from claseUsado import Usado

class Nodo:
    __vehiculo: Vehiculo
    __siguiente: object
    
    def __init__(self, unVehiculo):
        self.__vehiculo = unVehiculo
        self.__siguiente = None
        
    def set_siguiente(self, siguiente):
        self.__siguiente = siguiente
        
    def get_siguiente(self):
        return self.__siguiente
    
    def get_dato(self):
        return self.__vehiculo
    
    def get_patente(self):
        if isinstance(self.__vehiculo, Usado):
            return self.__vehiculo.get_patente()
        
    def toJSON(self):
        d = self.__vehiculo.toJSON()
        return d
    