'''Ejercicio 2. Función calcular_promedio :
Crea una función que calcule el promedio de una lista de números'''

def calcular_promedio(lista):
    return sum(lista) / len(lista) if lista else 0

numeros = [10, 20, 30, 40, 50,]
print(calcular_promedio(numeros))

