"""
La funcion "calcular_edad" indica correctamente la cantidad
de años que pasaron desde una fecha al 5 de enero de 2023
siempre y cuando se le pase el parámetro "fecha_nac_str"
con el formato YYYY-m-d (4 digitos para el año, luego un 
guion, luego el mes y luego el dia)
Por ejemplo: calcular_edad('1992-1-7') es igual 31

Algunos usuarios llaman a la funcion usando mal
el formato de fecha.
Por ejemplo '1997 - 1 - 7' o ' 2003-2  - 9'
El error son siempre espacios en la fecha

Tarea: Corregir el parámetro "fecha_nac_str" para que no tenga espacios
al inicio, final o dentro de la fecha

"""
from datetime import datetime

hasta = datetime(2023, 1, 5)
def calcular_edad(fecha_nac_str):
    fecha_nac = datetime.strptime(fecha_nac_str, '%Y-%m-%d')
    diff = hasta - fecha_nac
    return diff.days // 365


# NO BORRAR LAS LINEAS QUE SIGUEN
# Una vez terminada la funcion ejecutar este archivo
# Si se ve la leyenda 'Ejercicio terminado OK' esta listo, crear un PR

assert calcular_edad(fecha_nac_str='2021-1-2') == 2
assert calcular_edad(fecha_nac_str='2021-1-7') == 1
assert calcular_edad('1992-1-7') == 31
assert calcular_edad('1978-1-7') == 45
assert calcular_edad('1978 - 1 - 7') == 45
assert calcular_edad(' 1978 -  1 - 7 ') == 45

print('Ejercicio terminado OK')
