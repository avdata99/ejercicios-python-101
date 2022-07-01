"""
Completar la funcion para que abra el archivo pasado
en el paremtro "path" y cuente cuantas veces se repite
cada palabra. La funcion debe devolver solo aquellas palabras
que:
 - Tengan 6 o más carcateres de largo
 - Se repitan al menos 50 veces
"""


def mas_de_50(path):
    """ 
    Abrir el archivo con el libro de texto, contar la
    repeticion de palabras y devolver solo aquellas que
    cumplen con los requisitos
    """
    pass

# NO BORRAR LAS LINEAS QUE SIGUEN
# Una vez terminada la funcion ejecutar este archivo
# Si se ve la leyenda 'Ejercicio terminado OK' esta listo, crear un PR

# Si el path no funciona en tu máquina, corregirlo.
pl = mas_de_50('florante.txt')
print(pl)
assert pl['corazón'] == 52
assert pl['cuando'] == 65

print('Ejercicio terminado OK')