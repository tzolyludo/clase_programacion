class Pelicula:
    
    def __init__(self, titulo):
        self.titulo = titulo
        self.vista = False
        
    def marcar_como_vista(self):
        self.vista = True
        
    def __str__(self):
        
        if self.vista:
            estado = 'Vista'
        else:
            estado = 'No vista'
            
        return f"{self.titulo} - {estado}"
    
class ListaPeliculas:
    
    def __init__(self):
        self.peliculas = []
        
    def agregar_pelicula(self,titulo):
        pelicula = Pelicula(titulo)
        self.peliculas.append(pelicula)
        print(f"Pelicula {titulo} agregada")
        
    def marcar_como_vista(self, indice):
        
        if 0<= indice < len(self.peliculas):
            
            self.peliculas[indice].marcar_como_vista()
            
            print(f"Pelicula {self.peliculas[indice].titulo} marcada como vista!")
        else:
            print("Indice de la pelicula no valido")
            
    def mostrar_peliculas(self):
        
        if self.peliculas:
            print("Lista de pliculas")
            for i, pelicula in enumerate(self.peliculas):
                print(f"{i}. {pelicula}")
        else:
            print("No hay peliculas en la lista.") 
            
    
    
def mostrar_menu():
    print("\nGestor de lista de peliculass")
    print("1. Agregar peliculaa")
    print("2. Marcar pulicula como vista")
    print("3. Mostrar todas las peliclas")
    print("4. Salir")
    
    
def main():
    
    lista_peliculas = ListaPeliculas()
    
    while True:
        mostrar_menu() 
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            titulo = input("Ingrese el titulo de la pelicula: ")
            lista_peliculas.agregar_pelicula(titulo)
        elif  opcion == "2":
            lista_peliculas.mostrar_peliculas()
            indice = int(input("Seleccione el numero de la pelicula a marcar como vista: "))
            lista_peliculas.marcar_como_vista(indice)  
        elif  opcion == "3":
            lista_peliculas.mostrar_peliculas()
        elif  opcion == "4":
            print("Saliendo del gestor de peliculass...")
            break
        else:
            print("Opcion no valida. Intenta de nuevo")
            
main()                    