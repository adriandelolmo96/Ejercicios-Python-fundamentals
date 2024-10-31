'''Ejercicio 3. Función encontrar_duplicado :
Crea una función que busque y devuelva el primer elemento duplicado en una
lista dada.'''

def encontrar_duplicado():
    lista = input("Introduce una lista de números separados por comas: ")
    lista = lista.split(",")
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return "No se han encontrado duplicados"

resultado = encontrar_duplicado()
print("El primer duplicado es:", resultado)
