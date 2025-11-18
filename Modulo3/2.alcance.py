"""
El alcance o scope es el contexto en el que se define una variable.
Las variables localces solo son accesibles dentro de la función.
Las variables globales son accesibles dentro y fuera de la función.

El alcance se refiere a la región del programa donde un espacio de nombres es directamente accesible.

Local: la variable se busca primero en el espacio de nombre local.
Enclosing (intermedio): Si no se encuentra, se busca en los espacios de nombres de cualquier función envolvente.
Global: Si no se encuentra en los dos anteriores, se busca en el espacio de nombres global.
Built-in: finalmente, si no se encuentra en ninguno de los anteriores, se busca en el espacio de nombres incorporado (built-in) de Python.
    
"""

variable_global = "Soy una variable global"

def mi_funcion():
    variable_local = "Soy una variable local"
    print(variable_local)  # Acceso a la variable local
    print(variable_global)  # Acceso a la variable global

mi_funcion()

# print(variable_local)  # Esto generará un error, ya que variable_local no es accesible fuera de la función

#Scope de una variable  
contador = 0  # Variable global
def incrementar():
    global contador  # Indica que se usará la variable global
    # contador = 10  # Variable local
    contador += 1
    return contador

print(incrementar())  # Salida: 1
print(contador)  # Salida: 0

#CONSTANTES
PI = 3.1416  # Convención para constantes en Python
print(PI)


# Ambito global y local (enclosing)

def funcion_externa():
    variable_exterior = "Soy una variable externa"

    def funcion_interior():
        variable_interior = "Soy una variable interior"
        # print(variable_interior)  # Acceso a la variable local
        print(variable_exterior)  # Acceso a la variable de la función externa
    funcion_interior()

funcion_externa()

#ciclo for
lista = [1, 2, 3, 4, 5]
for numero in lista:
    print(numero)
print(numero)  # Acceso a la variable del ciclo for fuera del ciclo