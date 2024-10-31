'''Ejercicio 5. Función es_anagrama :
Crea una función que determine si dos palabras son anagramas, es decir, si
están formadas por las mismas letras pero en diferente orden.'''

def son_anagramas():
    palabra1 = input("Introduce la primera palabra: ").replace(" ", "").lower()
    palabra2 = input("Introduce la segunda palabra: ").replace(" ", "").lower()
    if sorted(palabra1) == sorted(palabra2):
        print("Son anagramas.")
    else:
        print("No son anagramas.")

son_anagramas()


