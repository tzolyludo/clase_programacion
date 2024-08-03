porcentaje = 13/100
float(porcentaje)
nombre = input("Escribe tu Nombre: ")
ventas_totales = float (input("Ingresa el valor de tus ventas totales :"))
resultado= ventas_totales * porcentaje
neto = ventas_totales + resultado
print(f"hola {nombre} tus comisiones son {round(resultado,2)} y el valor a pagarte es de {round(neto,2)}")