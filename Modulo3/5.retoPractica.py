"""
Realizar el juego de piedra, papel o tijera haciendo uso de funciones
"""

import random

JUGADAS = ["piedra", "papel", "tijera"]

def jugada_maquina():
    #pass #Pass permite dejar la función vacía temporalmente
    return random.choice(JUGADAS)

def jugada_usuario():
    return int(input("Ingrese el número de su elección: "))

def menu():
    print("Bienvenido al juego de piedra, papel o tijera. Seleccione una opción:")
    print("1. piedra")
    print("2. papel")
    print("3. tijera")
    opcion_usuario = jugada_usuario()
    print("Tu jugada es:", JUGADAS[(opcion_usuario) - 1])
    opcion_maquina = jugada_maquina()
    print("La jugada de la máquina es:", opcion_maquina)

    if(JUGADAS[(opcion_usuario) - 1] == "piedra"):
        if(opcion_maquina == "tijera"):
            print("¡Ganaste! ✊")
        elif(opcion_maquina == "papel"):
            print("¡Perdiste! 😒")
        else:
            print("Empate 😑")
    if(JUGADAS[(opcion_usuario) - 1] == "papel"):
        if(opcion_maquina == "piedra"):
            print("¡Ganaste! ✋")
        elif(opcion_maquina == "tijera"):
            print("¡Perdiste! 😒")
        else:
            print("Empate 😑")
    if(JUGADAS[(opcion_usuario) - 1] == "tijera"):
        if(opcion_maquina == "papel"):
            print("¡Ganaste! ✌️")
        elif(opcion_maquina == "piedra"):
            print("¡Perdiste! 😒")
        else:
            print("Empate 😑")

menu()

print("\n")

pregunta = input("¿Desea jugar de nuevo? (si/no): ")
while pregunta.lower() == "si":
    menu()
    pregunta = input("¿Desea jugar de nuevo? (si/no): ")
print("Gracias por jugar. ¡Hasta luego!")






