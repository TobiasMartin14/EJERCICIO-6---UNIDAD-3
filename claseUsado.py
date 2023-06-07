from claseVehiculo import Vehiculo

class Usado(Vehiculo):
    __patente: str
    __año: int
    __kilometraje: float
    __marca: str
    
    def __init__(self, marca, modelo, puertas, color, preciobase, patente, anio, kilometraje):
        super().__init__(modelo, puertas, color, preciobase)
        self.__patente = patente
        self.__año = anio
        self.__kilometraje = kilometraje
        self.__marca = marca
        
    def __str__(self):
        cadena = super().__str__()
        cadena += ', Patente: ' + self.__patente + ', Año: {}'.format(self.__año) + ', Kilometros: {}'.format(self.__kilometraje) + ', Marca: ' + self.__marca
        return cadena
    
    def toJSON(self):
        d = super().toJSON()
        c = dict(**d, patente = self.__patente, año = self.__año, km = self.__kilometraje, marca = self.__marca)
        return c
    
    
        
    def get_precio(self)->float:
        precio_base = super().get_precio()
        precio_total = precio_base - (precio_base * 0.01 * (2023 - self.__año))
        if self.__kilometraje >= 100000:
            precio_total -= precio_base * 0.02
        return precio_total

    def get_patente(self):
        return self.__patente