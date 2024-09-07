#para hacer el mismo ejercicio en menos lineas
palabra = 'python'

# lista = []
# for letra in palabra:
#     lista.append(letra)
# print(lista)    


# lista = [letra for letra in palabra]
# print(lista)

# lista2 = [n for n in range(0,21,2)]
# print(lista2)

# lista3 = [n/2 for n in range(0,21,2)]
# print(lista3)

lista4 = [n for n in range(0,21,2) if n*2 > 10]
print(lista4)