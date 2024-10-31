'''Ejercicio 16. Función procesar_texto :
Crea una función llamada
procesar_texto que procesa un texto según la opción especificada:
contar_palabras , reemplazar_palabras , eliminar_palabra . Estas opciones son otras
funciones que tenemos que definir primero y llamar dentro de la función
procesar_texto .
Código a seguir:
1. Crear una función contar_palabras para contar el número de veces que
aparece cada palabra en el texto. Tiene que devolver un diccionario.
2. Crear una función reemplazar_palabras para remplazar una palabra_original
del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo
de palabras.
3. Crear una función eliminar_palabra para eliminar una palabra del texto.
Tiene que devolver el texto con la palabra eliminada.
4. Crear la función procesar_texto que tome un texto, una opción(entre
"contar", "reemplazar", "eliminar") y un número de argumentos variable
según la opción indicada.
Caso de uso:
texto = "Este es un ejemplo de texto. Este texto contiene palabras repetidas."
Dado el texto de ejemplo, llama a la función procesar_texto para probar sus
funcionalidades:
Cuenta el número de veces que aparece cada palabra.
Reemplaza la palabra texto por relato.
Elimina la palabra ejemplo.'''

from collections import Counter
import re

def contar_palabras(texto):
    texto = re.sub(r'[^\w\s]', '', texto.lower())
    palabras = texto.split()
    return dict(Counter(palabras))

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return re.sub(rf'\b{re.escape(palabra_original)}\b', palabra_nueva, texto)

def eliminar_palabra(texto, palabra_a_eliminar):
    return re.sub(rf'\b{re.escape(palabra_a_eliminar)}\b', '', texto).replace("  ", " ").strip()

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar" and len(args) == 2:
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar" and len(args) == 1:
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida o argumentos incorrectos.")

texto = "Este es un ejemplo de texto. Este texto contiene palabras repetidas."
print(procesar_texto(texto, "contar"))
print(procesar_texto(texto, "reemplazar", "texto", "relato"))
print(procesar_texto(texto, "eliminar", "ejemplo"))

