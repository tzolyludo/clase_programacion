# class Pajaro:
#     alas = True
#     def __init__(self, color, especie):
#         self.color = color
#         self.especie = especie
    
# piolin = Pajaro('amarrillo','Canario')  

# print(piolin.color, piolin.especie)
# # printe(f"Mi pajaro es de color {piolin.color} de especie {piolin.especie}")










# class Casa:
#      def __init__(self,color, cantidad_pisos):
#         self.color = color
#         self.cantidad = cantidad_pisos
# hogar = Casa('Blanco',2)  
# print(hogar.color, hogar.cantidad)      

# class Cubo:
#     caras = 6
#     def __init__(self,color):
#         self.color = color
        
# cubo_rojo = Cubo('Blanco')  
# print(cubo_rojo.color)   

class  Personaje:
    real = False
    def __init__(self, especie, magico, edad):
        self.especie = especie 
        self.magico = magico
        self.edad = edad
harry_potter = Personaje("Humano",True,17)
print(harry_potter.especie, harry_potter.magico,harry_potter.edad)  
          