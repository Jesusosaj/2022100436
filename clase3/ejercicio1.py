def ingresar_numeros():
    numeros=[]
    while True:
        numero = input("Ingresar un numero (o ingresar n para salir)")
        if(numero.lower == "n"):
            break
    
        numeros.append(float(numero))
    
    return numeros
    
def sumar_numeros(numeros):
    suma = 0
    for numero in numeros:
        suma+=numero

    return suma



def calcular_promedio(numeros):
    suma = sumar_numeros(numeros)
    promedio = suma/len(numeros)
    return promedio



def encontrar_max_min(numeros):
    maximo = max(numeros)
    minimo = min(numeros)

    return maximo, minimo


def numeros_mayores_que_promedio(numeros, promedio):
    mayores=[]

    for numero in numeros:
        if(numero > promedio):
            mayores.append(numero)

    return mayores

def main():
    numeros = ingresar_numeros()

    if len(numeros)==0:
        print("No se ingresaron numeros")
        return


    suma=sumar_numeros(numeros)
    promedio=calcular_promedio(numeros)
    maximo, minimo = encontrar_max_min(numeros)
    mayores=numeros_mayores_que_promedio(numeros,promedio)


    print(f"\nLos numeros ingresados es: {numeros}")
    print(f"\La suma de los numeros ingresados es: {suma}")
    print(f"\nEl promedio de los numeros ingresados es: {promedio}")
    print(f"\nNumero mas grande: {maximo}")
    print(f"\nNumero mas pequeño: {minimo}")
    print(f"\nNumeros mayores que el promedio: {mayores}")


    