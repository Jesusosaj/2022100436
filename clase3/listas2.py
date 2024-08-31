
array1=["futbol","Pc", 18.4, 15, [1,2,3,4,5], True, False]
array2=[1,2,3,4,5,65]

array3=array1+array2

print(array3)

print("Pc" in array1)

print(array1.index("Pc"))

print(array1.count("Pc"))

array1.remove("Pc")
print(array1)

#array1.clear()

array1.reverse()

print(array1)

array4=[23,5,4,23,6,4,2,1,-7]
array4.sort()

array4.sort(reverse=True)