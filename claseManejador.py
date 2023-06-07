import json
from claseLista import Lista
from claseDecodificador import Decodificador
from claseVehiculo import Vehiculo
from claseNuevo import Nuevo
from claseUsado import Usado

class ManejadorV:
    __vehiculos: Lista
    
    def __init__(self):
        self.__vehiculos = Lista()
        
    def cargar(self):
        jsonF = Decodificador()
        diccionario = jsonF.leerJSON('vehiculos.json')
        self.__vehiculos = jsonF.decodificarDic(diccionario)
        
    def crear_vehiculo(self):
            print('Ingrese los siguientes datos')
            modelo = input('Modelo')
            puerta = int(input('Puertas'))
            color = input('Color')
            precio = float(input('Precio Base'))
            tipo = input('Ingrese el tipo de vehiculo a cargar ("Nuevo" o "Usado")')
            if tipo == 'Nuevo':
                marca = input('Marca')
                version = input('Version ("base" o "full)')
                unVehiculo = Nuevo(modelo, puerta, color, precio, marca, version)
            elif tipo == 'Usado':
                patente = input('Patente')
                año = int(input('Año'))
                km = float(input('Kilometros'))
                marca = input('Marca')
                unVehiculo = Usado(modelo, puerta, color, precio, patente, año, km, marca)
            return unVehiculo
        
    def agregar_vehiculo(self, unVehiculo):
        self.__vehiculos.agregarVehiculo(unVehiculo)
        
    def insertar_vehiculo(self, unVehiculo):
        self.__vehiculos.insertarVehiculo(unVehiculo)
        
    def mostrarVehiculo(self):
        self.__vehiculos.mostrarVehiculo()
        
    def modificar_precio(self):
        self.__vehiculos.modificar_precio()
        
    def mostrar_mas_economico(self):
        min = 999999999
        for vehiculo in self.__vehiculos:
            if vehiculo.get_precio() < min:
                min = vehiculo.get_precio()
                economico = vehiculo
        print('El vehículo mas económico es:')
        print(economico)
        print('Precio Total: ${}'.format(economico.get_precio()))
        
    def mostrar_vehiculos(self):
        for vehiculo in self.__vehiculos:
            print('Modelo: ' + vehiculo.get_modelo() + ', Cantidad de Puertas: {}'.format(vehiculo.get_puertas()) + ', Importe de venta: {}'.format(vehiculo.get_precio()))
            
    def toJSON(self):
        jsonF = Decodificador()
        d = self.__listaVehiculos.toJSON()
        jsonF.guardarJSONArchivo(d, "test.json")