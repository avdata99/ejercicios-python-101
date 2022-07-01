"""
La clase Persona entrega una version mejorada del
nombre cuando se llama a la propiedad "nombre".
Sin embargo no hace todas las correcciones que se esperan
Tarea: 
 Corregir la propiedad nombre (no tocar ninguna otra parte del codigo)
 de modo que se eliminen:
  - Los dobles espacios en el interior de los nombres
  - Los espacios al inicio y al final
"""


class Persona:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre.title()


def crear_multiples_personas(nombres):
    personas = []
    for nombre in nombres:
        p = Persona(nombre)
        personas.append(p)
        # if nombre != p.nombre:
        #     print(f'El nombre "{nombre}" fue corregido por "{p.nombre}"')
        # else:
        #     print(f'El nombre "{nombre}" está ok')
    return personas


# NO BORRAR LAS LINEAS QUE SIGUEN
# Una vez terminada la funcion ejecutar este archivo
# Si se ve la leyenda 'Ejercicio terminado OK' esta listo, crear un PR

nombres = ['juan', 'Pedro', 'Juan manuel', ' victor  hugo ']
personas = crear_multiples_personas(nombres)
nombres_mejorados = [persona.nombre for persona in personas]
assert nombres_mejorados == ['Juan', 'Pedro', 'Juan Manuel', 'Victor Hugo']

print('Ejercicio terminado OK')
