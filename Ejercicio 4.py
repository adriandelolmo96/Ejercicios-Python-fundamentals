'''Ejercicio 4. Función enmascarado_datos :
Crea una función que convierta una variable en una cadena de texto y
enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.'''

def enmascarar(variable):
   
    texto = str(variable)
    if len(texto) > 4:
        return '#' * (len(texto) - 4) + texto[-4:]
    return texto
resultado = enmascarar("123456789")
print(resultado)
