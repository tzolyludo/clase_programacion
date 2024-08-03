#************************ ejercicio ********************
texto = input("Ingresa un texto cualquiera: ")
texto = texto.lower()

letras = []
letras.append(input("Ingresa la primera letra :".lower()))
letras.append(input("Ingresa la segunda letra :".lower()))
letras.append(input("Ingresa la tercera letra :".lower()))

print("¨\n")
print("cantidad de letras")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])
print(f"Hemos encontrado la letra {letras[0]} repetidas {cantidad_letras1} veces")
print(f"Hemos encontrado la letra {letras[1]} repetidas {cantidad_letras2} veces")
print(f"Hemos encontrado la letra {letras[2]} repetidas {cantidad_letras3} veces")


print("\n")
print("Cantidad de palabras")
palabra = texto.split()
print(f"Hemos encontrado {len(palabra)}palabras  en un tu texto")

print("\n")
print("LETRA DE INICIO Y DE FIN")
letra_inicio = texto[0]
letra_fin = texto[-1]
print(f"la letra inicial es {letra_inicio} y la la final es {letra_fin}")

print("\n")
print("texto invertido")
palabra.reverse()
texto_invertido = ''.join(palabra)
print(f"si ordenamos  tu texto al reves va a decir :{texto_invertido}")

print("\n")
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = 'python'in texto
dic = {True:"si",False:"no"}
print(f"La palabra python {dic[buscar_python]}se encuentra en el texto")


