'''Ejercicio 7. Función fibonacci :
Crea una función que calcule el término n de la serie de Fibonacci utilizando
recursión.
Definición de la secuencia de Fibonacci:
La secuencia de Fibonacci es una serie de números en la que cada número es
la suma de los dos números anteriores, comenzando con 0 y 1. La posición 0
es la primera:
Ejemplo para los primeros 5 términos de la función de Fibonacci: [0, 1, 1, 2, 3]
Primer término: 0 (0)'''

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = 10
print(f"El término {n} de la serie de Fibonacci es: {fibonacci(n)}")
