class Animal:
    def __init__(self,edad, color):
        self.edad = edad
        self.nombre = color
    
    def nacer(self):
        print("El animal nacio")    
    
    def hablar(self):
        print("Este animal emite un sonido") 
        
class Pajaro(Animal):
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)           
        self.altura_vuelo = altura_vuelo
        
    def hablar(self):
        print('Pio')
        
    def volar(self, metros):
        print(f'El pajaro vuela {metros} metros')
        
piolin = Pajaro(2, 'amarrillo',20)

piolin.hablar()
piolin.volar(100)
                