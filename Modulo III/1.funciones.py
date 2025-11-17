"""
    Las funciones en python son bloques de código reutilizables que realizan una tarea específica.
    Se definen utilizando la palabra clave def seguida del nombre de la función y paréntesis
    que pueden incluir parámetros. Para que las funciones sean reutilizables y modulares, es recomendable
    Las funciones pueden devolver valores utilizando la palabra clave return.

"""
# Declaración de una función sin parámetros
def saludo():
    """Función que imprime un saludo."""
    print("¡Hola, bienvenido a Python!") 

# Llamada a la función
saludo()

# función sin parámetros que devuelve un valor
def mensaje():
    """Función que devuelve un mensaje de bienvenida."""
    return "¡Hola, bienvenido a Python!"    
# Llamada a la función y almacenamiento del valor devuelto
texto = mensaje()
print(texto)


## Declaración de una función con parámetros y retorno de valor
def suma(numero1, numero2):
    """Función que suma dos números y devuelve el resultado."""
    resultado = numero1 + numero2
    return resultado

# Llamada a la función con argumentos
resultado = suma(5, 3)
print("La suma es:", resultado)

#Funcion con parámetros por defecto
def resta(numero1, numero2=2):
    """Función que eleva un número a una resta dada (por defecto al cuadrado)."""
    resultado = numero1 - numero2
    return resultado

# Llamada a la función con y sin el parámetro por defecto
print("resta:", resta(5, 3))  # Usa el valor por defecto de exponente

def mostrar_mensaje(mensaje="¡Hola!"):
    """Función que muestra un mensaje dado."""
    print(mensaje)
# Llamada a la función con y sin el parámetro por defecto
mostrar_mensaje("¡Bienvenido a la programación en Python!")  # Mensaje personalizado


def calcular_area_rectangulo(base, altura):
    """Función que calcula el área de un rectángulo."""
    area = base * altura
    return area
# Llamada a la función con argumentos
print(calcular_area_rectangulo(5, 3))  # Área: 15
print(calcular_area_rectangulo(7, 4))  # Área: 28

