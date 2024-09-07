from random import randint

intentos = 0
estimado = 0
numero_secreto = randint(1,100)
nombre = input ("Dime tu nombre")
print(f"bueno{nombre},he pensado un numero entre 1 y 100 tienens 8 intentos para adivinar")
while intentos < 8:
    estimado = int(input("cual es el numero"))
    intentos +=1
    if estimado < numero_secreto:
        print("Mi numero es as alto")
    elif estimado >numero_secreto:
        print("Mi numero es as bajo")
else:
    print(f"felicidades{nombre}. has ganado en {intentos} intentos")
break

if estimado != numero_secreto:
    print("se ha agotado el numero de intentos")
        