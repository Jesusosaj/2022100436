#Tipos de variables en python

print("Hola mundo")
entero = 50
flotante = 9.8
palabra="Hola de nuevo"
dato = True
print(entero)
print(type(entero))
print(flotante)
print(type(flotante))
print(type(palabra))
print(type(dato))

print("Sumando")
num1 = 2
num2 = 6

print("La suma es: ", num1+num2)

'''
    Operadores de asignacion
'''

c=0
c+=1
print(c)

d= 10
d-=4
print(d)

f= 2
f+=5
print(f)


'''
    Operadores relacionales
'''

r=100==100
print(r)
r=90>100
print(r)
r=90<100
print(r)
r=90<=100
print(r)
r=90>=100
print(r)

'''
    Operadores Aritmeticos
'''

num1 = 2
num2 = 5
print("Resultado de la suma: ", num1+num2)

print("Resultado de la resta: ", num1-num2)

print("Resultado de la mult: ", num1*num2)

print("Resultado de la div: ", num1/num2)



'''
    Operadores logicos
'''

a=30
b=40
c=50
r=((a<b) and (b<c))
print(r)

r=((a<b) or (c<a))
print(r)

r=not ((a<b) or (c<a))
print(r)




'''
    Entradas de datos
'''

cadena = input("¿Como se llama tu proyecto?")
print(f"Tu proyecto se llama: {cadena}")

#cadena = input("¿Que version es?")
#print(f"Tu proyecto es {cadena +1}")

cadena = int(input("¿Que version es?"))
print(f"La version es: {cadena}")



'''
    Condiciones
'''

dato = int(input("Ingrese un numero: "))

if dato>0:  
    print("Numero postivo")
elif dato == 0: 
    print("Resultado igual a cero")
else:   
    print("Numero negativo")