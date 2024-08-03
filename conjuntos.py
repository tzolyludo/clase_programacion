#menera de defnir conjuntos
# mi_set = set([1,2,3,4])
# mi_set = set({1,2,3,4})
# mi_set = set((1,2,3,4))

mi_set2 = {1,2,3,4,5}
print(type(mi_set2))

mi_set = {1,2,3,4,5,6,1,1,1,1,1}#no permite duplicados es decir en pantalla no salen los repetidos
print(mi_set)

#cuentas los elementos del conjunto
print(len(mi_set2))

#busca el 2 en el cojunto
print(2 in mi_set)

#union de conjuntos
s1 = {1,2,3}
s2 =  {3,4,5}
s3 = s1.union(s2)
print(s3)


s1.add(4)
print(s1)