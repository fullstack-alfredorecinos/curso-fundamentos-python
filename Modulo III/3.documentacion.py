"""
Documentación y anotaciones de tipo
La documentación de tipo se utiliza para documentar los tipos de datos que se esperan en funciones, variables y otros elementos del código.
Y las anotaciones de tipo se utilizan para indicar que una variable tiene un tipo específico.
"""

def suma(numero1:int, numero2:int) -> int:
    """
    Esta función suma dos números enteros.
    
    :param numero1: Primer número entero a sumar.
    :type numero1: int
    :param numero2: Segundo número entero a sumar.
    :type numero2: int
    :return: La suma de los dos números enteros.
    :rtype: int
    """
    return numero1 + numero2
print(suma(5, 10))
print(suma.__doc__)

help(suma)


# Definir una función que calcule un salario
def calcular_salario(salario_base:float, horas_extras:int, horas_faltadas:int)-> float:
    """
    Calcula el salario total de un empleado.

    :param salario_base: Salario base del empleado.
    :type salario_base: float
    :param horas_extras: Número de horas extras trabajadas.
    :type horas_extras: int
    :param horas_faltadas: Número de horas faltadas.
    :type horas_faltadas: int
    :return: Salario total después de considerar horas extras y faltadas.
    :rtype: float
    """
    salario_total = salario_base + (horas_extras * 10) - (horas_faltadas * 15)
    return salario_total

print(calcular_salario.__doc__)


def resta(numero1:str, numero2:str) -> str:
    """
    Esta función resta dos parametros enteros y retorna la resta
    """
    return numero1 - numero2
print(resta(10, 5))  # Esto generará un error en tiempo de ejecución
