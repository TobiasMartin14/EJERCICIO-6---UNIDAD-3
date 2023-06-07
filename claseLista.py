from zope.interface import implementer
from coleccionInterfaz import IColeccion
from claseNodo import Nodo
from claseNuevo import Nuevo
from claseUsado import Usado

@implementer(IColeccion)
class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int
    
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0
        self.__indice = 0
        
    def __iter__(self):
        self.__actual = self.__comienzo
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.get_dato()
            self.__actual = self.__actual.get_siguiente()
            return dato
        
    def insertarVehiculo(self, unVehiculo):
        posicion = int(input('Ingrese la posicion a guardar el vehiculo'))
        if posicion < 0 or posicion > self.__tope:
            raise Exception('Posicion No valida')
        else:  
            unNodo = Nodo(unVehiculo)
            if posicion == 0:
                aux = self.__comienzo
                self.__comienzo = unNodo
                self.__comienzo.set_siguiente(aux)
            else:
                i = 1
                anterior = self.__comienzo
                posterior = self.__comienzo
                while i < posicion and posterior.get_siguiente() != None:
                    anterior = posterior
                    posterior = posterior.get_siguiente()
                    i += 1
                if posterior == None:
                    anterior.set_siguiente(unNodo)
                else: 
                    anterior.set_siguiente(unNodo)
                    unNodo.set_siguiente(posterior)
            self.__tope += 1
        
    def agregarVehiculo(self, unVehiculo):
        unNodo = Nodo(unVehiculo)
        if self.__comienzo == None:
            self.__comienzo = unNodo
            self.__tope += 1
        else:
            aux = self.__comienzo
            while aux.get_siguiente() != None:
                aux = aux.get_siguiente()
            aux.set_siguiente(unNodo)
            self.__actual = unNodo
            self.__tope += 1

    def mostrarVehiculo(self):
        posicion = int(input('Ingrese la posicion a mostrar vehiculo'))
        if posicion < 0 or posicion > self.__tope:
            raise Exception('Posicion fuera de rango')
        else:  
            if posicion == 0:
                print(self.__comienzo.get_dato())
            else:
                i = 1
                aux = self.__comienzo.get_siguiente()
                while i < posicion and aux.get_siguiente() != None:
                    aux = aux.get_siguiente()
                    i += 1
                unVehiculo = aux.get_dato()
                if isinstance(unVehiculo, Usado):
                    print('El vehiculo de la posicion ingresada es Usado')
                else:
                    print('El vehiculo de la posicion ingresada es Nuevo')
    
    def modificar_precio(self):
        patente = input('Ingrese la patente del vehiculo')
        unVehiculo = self.__comienzo.get_dato()
        if isinstance(unVehiculo, Usado):
            if unVehiculo.get_patente() == patente:
                unVehiculo.modificar_precio_base()
        else:
            bandera = False
            aux = self.__comienzo.get_siguiente()
            unVehiculo = aux.get_dato()
            while aux.get_siguiente() != None and not bandera:
                if unVehiculo.get_patente() == patente:
                    bandera = True
                    unVehiculo.modificar_precio_base()
                else:
                    aux = aux.get_siguiente()
                    if aux != None:
                        unVehiculo = aux.get_dato()
            if bandera == False:
                print('La patente ingresada no se encontro')
            else:
                print('La patente se encontro, el nuevo precio es ${}'.format(unVehiculo.get_precio()))
                
    def toJSON(self):
        aux = self.__comienzo
        ld = []
        while aux != None:
            vdic = aux.toJSON()
            ld.append(vdic)
            aux = aux.getSiguiente()

    

            
                