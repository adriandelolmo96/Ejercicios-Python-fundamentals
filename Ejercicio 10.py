'''Ejercicio 10. Función resto_division usando lambdas:
Crea una función
lambda que calcule el resto de la división entre dos números dados.
'''

x = int(input("Introduce el dividendo (número que quieres dividir): "))
y = int(input("Introduce el divisor (número por el que quieres dividir): "))
resto_division = lambda x, y: x % y
print("El resto de la división de", x, "entre", y, "es:", resto_division(x, y))
