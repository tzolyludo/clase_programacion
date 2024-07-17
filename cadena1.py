nombre = input("Escribe tu Nombre: ")
Num_asoci = int (input("Ingresa numero de asociado :"))
print(f'Estimado/a {nombre},su numero de de asociado es: {Num_asoci}')

puntos_nuevos = int(input("Escribe tus puntos: "))
puntos_totales = puntos_nuevos
print(f'Has ganado {puntos_nuevos} puntos en total,acumulados:{puntos_totales} puntos ')

puntos_anteriores = puntos_totales
puntos_nuevos = int(input("Escribe tus nuevos puntos: "))
print("Has ganado {} puntos! en total,acumulas {} puntos!".format (puntos_nuevos,puntos_anteriores + puntos_nuevos))