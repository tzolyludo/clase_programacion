from random import choice

palabras = ['rojo','verde','cafe','negro']

letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_termiado = False

def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))
    return palabra_elegida, letras_unicas
def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abeccedario = 'abcdefghijklmnopqrstvwxyz'
    
    while not es_valida:
        letra_elegida = input("Eligeuna letra: ").lower()
        if letra_elegida in abeccedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("no has elegido una letra  correcta")
    return letra_elegida
def mostra_nuevo_tablero(palabra_elegida):
    lista_oculta = []  
              
    