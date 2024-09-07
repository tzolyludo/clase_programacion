class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
class Alumno(Persona):
    pass
alumno = Alumno('julio', 20)

class Mascota:
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas
        
        
mascota = Mascota(7,'peluche',4)    

class Vehiculo:
    def acelerar():
        pass
    def frenar():
        pass
    
class Automovil(Vehiculo):
    pass

batimovil = Automovil()    
            
            