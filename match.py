serie = 'N-02'

if serie == 'N-01':
    print('samsung')
elif serie == 'N-02':
    print('nokia')    
elif serie == 'N-03':
    print('motorola')
else:
    print('no es un celular')
    
match serie:
    case 'N-01':
         print('samsung')
         
         
         
         
cliente = {'nombre':'luis','edad':45,'ocupacion':'docente'}
pelicula = {'tituño':'metrix','ficha_tecnica':{'protagonista':'keano reeves','director':'lana'}}
elemento = [cliente,pelicula,'libro']
for e in elemento:
    match e:
        case {'nombre':nombre,'edad':edad,'ocupacion':ocupacion}:
            print("Es un cliente")
            print(nombre;edad;ocupacion)
        case{'titilo':titulo,'ficha_tecnica':{'protagonista':protagonista,'director':director}}:
            print("Es una pelicula")
            print(titulo,protagonista,director)
        case _:
            print("Esto es un libro")    
            
                     
         
                  
