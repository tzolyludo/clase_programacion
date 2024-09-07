


# try:
#     print("Esta todo el codigo a jecutar")
# except :
#     print("manejo de errores")  

# else:
#     print("es cuando no hay erroes en el coddigo") 

# finally:
#     print("siemprese va a ejecutar si hay o no error")
    
  
  
  
# def sumar():
#     try:
#         n1 = int(input( "numero 1: "))    
#         n2 = int(input( "numero 2: "))    
#     except ValueError:
#         print("error : ingrese solo numeros")
#         return
#     else:
#         print(n1+n2)
#         print("gracias por sumar")
        
#     finally:
#         print("sto fue todo")
        
# sumar()     



def dividir():
    try:
        numerador = int(input("ingrese numerador: "))
        demominador = int(input("ingrese denominador: "))
        resultado = numerador/demominador
    except ValueError:
        print("Error: ingrese solo numeros")
        
    except ZeroDivisionError:    
        print("Error: no se puede dividir entre cero")
        
    else:
       print(resultado)
       
       print("gracias por dividir")
        
    finally:
        print("sto fue todo")
        
dividir()        
            
          
        