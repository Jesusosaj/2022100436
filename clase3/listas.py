'''
    Listas
'''

array=["futbol","Pc", 18.4, 15, [1,2,3,4,5], True, False]


print (array)

print(array[1])

print(array[-1])

print(array[0:3])

print(array[:2])

print(array[2:])


#Para saber la cantidad de datos
print(len(array))

#Cargar valores
array.append(32)

print(array)

#Insertar en una posicion especifica
array.insert(0,23)

print(array)

#Añadir mas de un valor al final
array.extend([1,2,3,2342,1,2])
print(array)