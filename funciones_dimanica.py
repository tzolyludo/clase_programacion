# def chequear_3_cifras(numero):
#     return numero in range(100,1000)

# resultado = chequear_3_cifras(58)
# print(resultado)


def chequear_3_cifras(lista):
    listas_3_cifras = []
    for n in lista:
        if n in range(100,1000):
            listas_3_cifras.append(n)
        else:
            pass
    return listas_3_cifras    
resultado = chequear_3_cifras([555,45,700,4000])
print(resultado)
    
