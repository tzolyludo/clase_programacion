

import mysql.connector

class Database:
    
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="tzolly0276",
            database="ParqueBD" 
        )
        
        self.cursor = self.connection.cursor()
        
    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        self.connection.commit()
        
    def fetch_query(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
class Reserva:
    
    def __init__(self):
        self.db = Database()
        
    def agregar_reserva(self, nombre, fecha, personas, tipo_tour):
        query = "INSERT INTO reservas (nombre, fecha, personas, tipo_tour) VALUES (%s, %s, %s, %s)" 
        self.db.execute_query(query, (nombre, fecha, personas, tipo_tour)) 
        print(f"Reserva {nombre} agregado correctamente.")
        
    def listar_reservas(self):
        query = "SELECT * FROM reservas"
        reservas = self.db.fetch_query(query)
        print("\nLista de reservas")
        if not reservas:
            print("No hay reservas registradas")
        else:
            for reserva in reservas:
                print(f"ID: {reserva[0]}, Nombre: {reserva[1]}, Fecha: {reserva[2]}, Personas: {reserva[3]}, Tipo de tour: {reserva[4]} ")  
        print()   
        
    def actualizar_tipo_tour(self, id_reserva, nuevo_tipo_tour):
        query = "UPDATE reservas SET tipo_tour = %s WHERE id = %s"
        self.db.execute_query(query, (nuevo_tipo_tour, id_reserva)) 
        print(f"Tipo de tour con ID {id_reserva}, actualizado a {nuevo_tipo_tour}")
        
    def eliminar_reserva(self, id_reserva):
        query = "DELETE FROM reservas WHERE id = %s"
        self.db.execute_query(query, (id_reserva,)) 
        print(f" Reserva con ID {id_reserva} eliminado.")  
            
def menu():
    gestion_reserva = Reserva()
    while True:
        
        print("════════════════════════════════════════")
        print("\n--- Menu de Gestion de Reservas ---")
        print("1. Registrar nueva reserva")
        print("2. Listar todas las reservas")
        print("3. Actualizar reserva")
        print("4. Eliminar reserva")
        print("5. Salir")
        
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
            personas = int(input("Ingrese el numero de personas: "))
            tipo_tour = input("ingrese el tipo de tour: ")
            gestion_reserva.agregar_reserva(nombre, fecha, personas, tipo_tour)
        elif opcion == "2":
           gestion_reserva.listar_reservas()
        elif opcion == "3":
            id_reserva = int(input("Ingrese el ID de la reserva a actualizar: "))
            nuevo_tipo_tour = input("Ingrese el nuevo tipo de tour: ")
            gestion_reserva.actualizar_tipo_tour(id_reserva, nuevo_tipo_tour)
        elif opcion == "4":
            id_reserva = int(input("Ingrese el ID de la reserva a eliminar: "))
            gestion_reserva.eliminar_reserva(id_reserva) 
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida. Intente de nuevo")
            
menu()                             