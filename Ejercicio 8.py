'''Ejercicio 8. Función encontrar_puesto_empleado :
Crea una función que tome un nombre completo y una lista de empleados,
busque el nombre completo en la lista y devuelve el puesto del empleado si
está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
no trabaja aquí.
Caso de uso:
empleados = [{'nombre': "Juan", 'apellido': "García", 'puesto': "Secretario"},
{'nombre': "Mabel", 'apellido': "García", 'puesto': "Product Manager"},
{'nombre': "Isabel", 'apellido': "Martín", 'puesto': "CEO"}]'''

def encontrar_puesto_empleado(nombre_completo, empleados):
    for empleado in empleados:
        nombre = empleado['nombre'] + " " + empleado['apellido']
        if nombre == nombre_completo:
            return empleado['puesto']
    return "no trabaja aquí."
empleados = [
    {'nombre': "Juan", 'apellido': "García", 'puesto': "Secretario"},
    {'nombre': "Mabel", 'apellido': "García", 'puesto': "Product Manager"},
    {'nombre': "Isabel", 'apellido': "Martín", 'puesto': "CEO"}
]

nombre_completo = "Mabel García"
print(f"Puesto de {nombre_completo}: {encontrar_puesto_empleado(nombre_completo, empleados)}")

nombre_completo = "Pedro Diaz"
print(f"La persona '{nombre_completo}' {encontrar_puesto_empleado(nombre_completo, empleados)}")
