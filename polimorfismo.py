class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        print(f'{self.nombre} dice muu')
        
class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hablar(self):
        print(f'{self.nombre} dice beee')
                        
vaca1 = Vaca('aurora') 
oveja1 = Oveja('nube')

vaca1.hablar()
oveja1.hablar()

animales = [vaca1, oveja1]
for animal in animales:
    animal.hablar()
    
def animal1_habla(animal):
    animal.hablar    