class Estudiante():
    def __init__(self, nombre, edad, grado):
        self.nombre= nombre
        self.edad = edad
        self.grado = grado
        
def __str__(self):
    return f"Nombre: {self.nomnbre}, edad: {self.edad}, Grado: {self.grado}"

class Curso():
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = []
    
    def agregar_estudiante(self, estudiante):
           self.estudiantes.append(estudiante)
           print(f"Estudiante {estudiante.nombre} agregado al curso {self.nombre}")
           
    def eliminar_estudiante(self, nombre_estudiante):
        for estudiante in self.estudiantes:
            if estudiante.nombre == nombre_estudiante:
                self.estudiante.remove(estudiante)
                print(f"Estudiante {nombre_estudiante} eliminado del curso {self.nombre}")
                return
            print(f"Estudiante {nombre_estudiante}  no se encontro en el curso {self.nombre}")
    def mostrar_estudiantes(self):
        
        if self.estudiantes:
            print(f"Estudiantes inscritos en el curso {self.nombre}")
            for estudiante in self.estudiantes:
                print(estudiante)
        else:
            print(f"no hay estudiantes incritos en el curso {self.nombre}")
estudiante1 = Estudiante('juan',15,'noveno')
estudiante2 = Estudiante('maria',14,'octavo')

curso1 = Curso('matematicaas especiales','julio gonzalez')
curso1.agregar_estudiante(estudiante1)
curso1.agregar_estudiante(estudiante2)

curso1.mostrar_estudiantes()
curso1.eliminar_estudiantes('maria')
curso1.mostrar_estudiantes()
                    
            
            