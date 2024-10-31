'''Ejercicio 6. Función buscar_nombre :
Crea una función que solicite al usuario ingresar una lista de nombres y luego
solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se
imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza
una excepción.
Caso de uso:
Incorpora los siguientes nombres a la lista y comprueba que la función
funciona correctamente: "Jaime", "Silvia" y "Ana"'''


def buscar_nombre():
    nombres = input("Ingresa una lista de nombres separados por comas: ").split(",")
    nombres = [nombre.strip() for nombre in nombres]
    nombres.extend(["Jaime", "Silvia", "Ana"])
    nombre_a_buscar = input("Ingresa el nombre a buscar: ").strip()

    if nombre_a_buscar in nombres:
        print(f"El nombre '{nombre_a_buscar}' fue encontrado.")
    else:
        raise Exception(f"El nombre '{nombre_a_buscar}' no se encontró en la lista.")

try:
    buscar_nombre()
except Exception as e:
    print(e)
