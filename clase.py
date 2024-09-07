#practica 1
class personaje:
    def __init__(self,nombre):
        self.nom = nombre

        
p = personaje("Harry Potter")
print(p.nom)        
        
        
#practica 2
class Dinosaurio:
    def __init__(self,nombre):
        self.nom = nombre

        
d1 = Dinosaurio("velociraptor")
d2 = Dinosaurio("tiranosaurio_rex")
d3 = Dinosaurio("braquiosaurio")
print(d1.nom, d2.nom, d3.nom) 
        
        