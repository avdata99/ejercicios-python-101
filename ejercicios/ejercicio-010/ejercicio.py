"""
Completar la funcion para que devuelva la tercera
letra de la "palabra" (string) que se pasa como parametro.
"""


def tercera_letra(palabra:str) -> str:
    return palabra[2]


# NO BORRAR LAS LINEAS QUE SIGUEN
# Una vez terminada la funcion ejecutar este archivo
# Si se ve la leyenda 'Ejercicio terminado OK' esta listo, crear un PR

print(tercera_letra("hola"))

assert tercera_letra("hola") == "l"
assert tercera_letra("Es facil") == " "
assert tercera_letra("341A") == "1"

print('Ejercicio terminado OK')