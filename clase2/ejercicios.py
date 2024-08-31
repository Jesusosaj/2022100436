'''
    Crear un programa que pida dos numeros y obtenga como resultado cual de ellos es par o si ambos lo son
'''

dato1 = int(input("Ingrese un numero"))
dato2 = int(input("Ingreso otro numero"))

if(dato1%2 == 0 and dato2%2 == 0):
    print(f"El numero {dato1} y {dato2} es par")
elif(dato1%2 == 0 and dato2%2 != 0):
    print(f"El numero {dato1} es par y {dato2} es impar")
elif(dato1%2 != 0 and dato2%2 == 0):
    print(f"El numero {dato1} es impar y {dato2} es par")
else:  
    print(f"Ninguno es par")