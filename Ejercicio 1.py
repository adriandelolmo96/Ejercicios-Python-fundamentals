'''Ejercicio 1. Función contar_caracteres :
Crea una función que cuente el número de caracteres en una cadena de texto
dada.'''

def contar_caracteres():
    cadena = input("Introduce una frase: ")
    return len(cadena.replace(" ", ""))


resultado = contar_caracteres()
print("El número de caracteres es:", resultado)

