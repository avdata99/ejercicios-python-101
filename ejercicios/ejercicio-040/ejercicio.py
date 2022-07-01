"""
Tarea: corregir la funcion para que dado el parametro "data"
lo separe en líneas y lo transforme en una lista sin elementos vacios.
La función esta incompleta y necesita corregirse.
¿Cuál es la falla?
"""


def process_data(data):
    return data.split('\n')


# NO BORRAR LAS LINEAS QUE SIGUEN
# Una vez terminada la funcion ejecutar este archivo
# Si se ve la leyenda 'Ejercicio terminado OK' esta listo, crear un PR

data = """
juan
pedro
Laura
"""
f1 = process_data(data)
assert f1 == ['juan', 'pedro', 'Laura']


print('Ejercicio terminado OK')