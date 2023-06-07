from claseManejador import ManejadorV

class Menu:
    __cod: int
    
    def __init__(self, cod = 0):
        self.__cod = cod
    
    def mostrar_menu(self):
        print('Opcion 1: Cargar Lista')
        print('Opcion 2: Insertar un vehículo en la colección en una posición determinada')
        print('Opcion 3: Agregar un vehículo a la colección')
        print('Opcion 4: Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición')
        print('Opcion 5: Dada la patente de un vehículo usado, modificar el precio base, y luego mostrar el precio de venta')
        print('Opcion 6: Mostrar los datos del vehiculo mas economico')
        print('Opcion 7: Mostrar los datos de todos los vehiculos del concensionario')
        print('Opcion 8: Almacenar La lista en el Archivo')
        print('Opcion 0: Finalizar operacion')
        
    def ejecutar_menu(self, MV:ManejadorV):
        self.mostrar_menu()
        self.__cod = int(input('Ingrese el Codigo'))
        while self.__cod != 0:
            if self.__cod == 1:
                MV.cargar()
            elif self.__cod == 2:
                unVehiculo = MV.crear_vehiculo()
                MV.insertar_vehiculo(unVehiculo)
            elif self.__cod == 3:
                unVehiculo = MV.crear_vehiculo()
                MV.agregar_vehiculo(unVehiculo)
            elif self.__cod == 4:
                MV.mostrarVehiculo()
            elif self.__cod == 5:
                MV.modificar_precio()
            elif self.__cod == 6:
                MV.mostrar_mas_economico()
            elif self.__cod == 7:
                MV.mostrar_vehiculos()
            elif self.__cod == 8:
                MV.toJSON()
            else:
                print('Codigo Incorrecto')
            self.mostrar_menu()
            self.__cod = int(input('Ingrese el Codigo'))
            