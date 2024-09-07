#************************ ejercicio #3 ********************
'''
 La consigna es la siguiente: vas a crear un programa que primero le pida al usuario que
ingrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo, una frase, un
poema, lo que quiera. Luego, el programa le va a pedir al usuario que también ingrese tres
letras a su elección y a partir de ese momento nuestro código va a procesar esa información
para hacer cinco tipos de análisis y devolverle al usuario la siguiente información:

1. Primero: ¿cuántas veces aparece cada una de las letras que eligió? Para lograr esto, te
recomiendo almacenar esas letras en una lista y luego usar algún método propio de string
que nos permita contar cuantas veces aparece un sub string dentro del string. Algo que
debes tener en cuenta es que al buscar las letras pueden haber mayúsculas y minúsculas
y esto va a afectar el resultado. Lo que deberías hacer para asegurarte de que se
encuentren absolutamente todas las letras es pasar, tanto el texto original como las
letras a buscar, a minúsculas.
2. Segundo: le vas a decir al usuario cuántas palabras hay a lo largo de todo el texto. Y
para lograr esta parte, recuerda que hay un método de string que permite transformarlo
en una lista y que luego hay una función que permite averiguar el largo de una lista.
3. Tercero: nos va a informar cuál es la primera letra del texto y cuál es la última. Aquí
claramente echaremos mano de la indexación.
4. Cuarto: el sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de
las palabras. ¿Acaso hay algún método que permita invertir el orden de una lista, y otro
que permita unir esos elementos con espacios intermedios? Piénsalo.
5. Y por último: el sistema nos va a decir si la palabra “Python” se encuentra dentro del
texto. Esta parte puede ser algo complicada de imaginársela, pero te voy a dar una pista:
puedes usar booleanos para hacer tu averiguación y un diccionario para encontrar la
manera de expresarle al usuario tu respuesta
'''
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
print(f"Hemos encontrado {len(palabra)} palabras  en un tu texto")

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


