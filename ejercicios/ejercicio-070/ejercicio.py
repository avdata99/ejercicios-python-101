"""
Tarea: La función "multisuma" recibe un numero variable de
argumentos y los suma
Por ejemplo multisuma(1, 2, 1) es igual a 4
Buscamos aquí agregar una nueva funcionalidad:
Si uno de los argumentos es 0, entonces al argumento
siguiente se lo deberá sumar pero al doble de su valor
Por ejemplo 
 - multisuma(1, 2, 0, 1) deberá ser igual a 5 (1 + 2 + (1*2))
 - multisuma(1, 0, 50) deberá ser igual a 101 (1 + (50*2))
"""

def multisuma(*args):
    """
    Dada una serie de parametros, los suma y devuelve el resultado.
    """
    resultado = 0
    for arg in args:
        resultado += arg
    return resultado


# NO BORRAR LAS LINEAS QUE SIGUEN
# Una vez terminada la funcion ejecutar este archivo
# Si se ve la leyenda 'Ejercicio terminado OK' esta listo, crear un PR

assert multisuma(3, 4, 5) == 12
assert multisuma(3, 1, 5) == 9
assert multisuma(3, 1, -5) == -1
assert multisuma(1, 2, 0, 1) == 5
assert multisuma(1, 0, 50) == 101
assert multisuma(1, 0, -1) == -1

print('Ejercicio terminado OK')
