# def suma(a, b):
#     return a + b
# suma(8,5)

def suma(*args):
    total = 0
    for i in args:
        total += i
    return  total


print(suma(1,2,3,4))    