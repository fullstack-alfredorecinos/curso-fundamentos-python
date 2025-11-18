"""
Un módulo en python es un archivo que contiene definiciones y declaraciones de Python.
Un paquete en python permite coleccionar o agrupar un conjunto de módulos relacionados.
Los módulos y paquetes facilitan la organización y reutilización del código en proyectos de Python.

SDK: Software Development Kit
-Es un conjunto de clases, objetos y funciones

Math Python documentation: https://docs.python.org/3/library/math.html

Para cada problema que se requiera resolver, siempre va a existir un algoritmo y una función para resolverlo.

json.dumps: Convierte un objeto de Python en una cadena JSON.
json.loads: Convierte una cadena JSON a un diccionario de Python.

Date Time Python documentation: https://docs.python.org/3/library/datetime.html

"""

import math
import json
import datetime
# from math import pi, sqrt, pow, floor, ceil
from operaciones import suma, resta, multiplicacion, division

# Uso del paquete de operaciones
print("Suma desde el paquete operaciones",suma.suma(10, 5))  # Salida: 15
print("Resta desde el paquete operaciones",resta.resta(10, 5))  # Salida: 5
print("Multiplicación desde el paquete operaciones",multiplicacion.multiplicacion(10, 5))  # Salida: 50
print("División desde el paquete operaciones",division.division(10, 5))  # Salida: 2.0

#Ejemplos de math
print(math.pi) #Imprime el valor de pi
print(math.sqrt(16)) #Imprime la raiz cuadrada de 16
print(math.pow(2, 3)) #Imprime 2 elevado a la 3
print(math.floor(4.7)) #Imprime el valor redondeado hacia abajo
print(math.ceil(4.3)) #Imprime el valor redondeado hacia arriba


json.dumps({"nombre": "Juan", "edad": 30})  # Convierte un diccionario de Python en una cadena JSON
json.loads('{"nombre": "Juan", "edad": 30}')  # Convierte una cadena JSON a un diccionario de Python

print(datetime.datetime.now())  # Imprime la fecha y hora actual
print(datetime.date.today())  # Imprime la fecha actual
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))  # Imprime la fecha y hora actual en formato específico
print(datetime.timedelta(days=5))  # Imprime un objeto timedelta que representa un intervalo de tiempo de 5 días

ahora = datetime.datetime.now()
print(ahora.year)  # Imprime el año actual
print(ahora.month)  # Imprime el mes actual
print(ahora.day)  # Imprime el día actual
print(ahora.hour)  # Imprime la hora actual
print(ahora.minute)  # Imprime los minutos actuales
print(ahora.second)  # Imprime los segundos actuales






