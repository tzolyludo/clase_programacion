def suma(**kwargs):
    print(type(kwargs))
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        
    
suma(x=3, y=5, z=2)

    