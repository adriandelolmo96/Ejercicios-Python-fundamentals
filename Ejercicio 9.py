'''Ejercicio 9. Función cubo_numero usando lambdas:
Descripción del ejercicio:
Descripción:
Crea una función que calcule el cubo de un número dado mediante una
función
lambda
'''

cubo_numero = lambda x: x ** 3
numero = float(input("Ingresa un número para calcular su cubo: "))
resultado = cubo_numero(numero)
print(f"El cubo de {numero} es: {resultado}")
