class Pelicula:
    def _init_(self, titulo):
        self.titulo = titulo
        self.vista = False

    def marcar_como_vista(self):
        self.vista = True

    def _str_(self):
        if self.vista:
            estado = 'Vista'
        else:
            estado = 'No vista'
            
        return f"{self.titulo} - {estado}"
        


class ListaPeliculas:
    def _init_(self):
        self.peliculas = []

    def agregar_pelicula(self, titulo):
        pelicula = Pelicula(titulo)
        self.peliculas.append(pelicula)
        print(f"Película '{titulo}' agregada")

    def marcar_como_vista(self, indice):
        if 0 <= indice < len(self.peliculas):
            self.peliculas[indice].marcar_como_vista()
            print(f"Película '{self.peliculas[indice].titulo}' marcada como vista.")
        else:
            print("Índice inválido.")

    def mostrar_peliculas(self):
        if self.peliculas:
            print("Lista de peliculas")
            for i, pelicula in enumerate(self.peliculas):
                print(f"{i}. {pelicula}")
        else:
            print("No hay peliculas en la lista.") 
        

def menu():
    print("\n--- Gestor de Lista de Películas ---")
    print("1. Agregar película")
    print("2. Marcar película como vista")
    print("3. Mostrar películas")
    print("4. Salir")
    return input("Seleccione una opcion: ")


def main():
    lista_peliculas = ListaPeliculas()

    while True:
        opcion = menu()

        if opcion == "1":
            titulo = input("Ingrese el título de la película: ")
            lista_peliculas.agregar_pelicula(titulo)
        elif opcion == "2":
            lista_peliculas.mostrar_peliculas()
            indice = int(input("Ingrese el número de la película que desea marcar como vista: ")) - 1
            lista_peliculas.marcar_como_vista(indice)
        elif opcion == "3":
            lista_peliculas.mostrar_peliculas()
        elif opcion == "4":
            print("Gracias por usar el Gestor de Lista de Películas. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")



main ()