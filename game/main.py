import random

def opcJugadores():
    opcionUsuario = input("Elije -> piedra, papel o tijera: ")
    opcionUsuario = opcionUsuario.lower()

    opcComputer = ("piedra", "papel", "tijera")
    opcionDelPC = random.choice(opcComputer)

    if opcionUsuario not in opcComputer:
        opcionUsuario = None
        opcionDelPC = None

    return opcionUsuario, opcionDelPC

def reglas(opcionUsuario, opcionDelPC):
    puntajeUsuario = 0
    puntajePC = 0

    if opcionUsuario == opcionDelPC:
        print("Empate")
    elif opcionUsuario == "papel":
        if opcionDelPC == "piedra":
            print(f"Opc del PC: {opcionDelPC}, el usuario gana")
            puntajeUsuario += 1
        elif opcionDelPC == "tijera":
            print(f"Opc del PC: {opcionDelPC}, el usuario pierde")
            puntajePC += 1
    elif opcionUsuario == "tijera":
        if opcionDelPC == "piedra":
            print(f"Opc del PC: {opcionDelPC}, el usuario pierde")
            puntajePC += 1
        elif opcionDelPC == "papel":
            print(f"Opc del PC: {opcionDelPC}, el usuario gana")
            puntajeUsuario += 1
    elif opcionUsuario == "piedra":
        if opcionDelPC == "papel":
            print(f"Opc del PC: {opcionDelPC}, el usuario pierde")
            puntajePC += 1
        elif opcionDelPC == "tijera":
            print(f"Opc del PC: {opcionDelPC}, el usuario gana")
            puntajeUsuario += 1

    return puntajeUsuario, puntajePC


def Game(puntajeUsuario=0,puntajePC=0):
    cont = 1
    while puntajeUsuario < 2 and puntajePC < 2:
        print()
        print("-" * 10)
        print(f"[GAME {cont}]")
        print("-" * 10)
        print()

        opcUsuario, opcPC = opcJugadores()
        if opcUsuario is not None:
            puntosU, puntosPC = reglas(opcUsuario, opcPC)
            puntajeUsuario += puntosU
            puntajePC += puntosPC
        else:
            print("Opcion no valida")
            continue

        cont += 1
        if puntajeUsuario == 2:
            print()
            print("GANASTE EL JUEGO")
            break
        elif puntajePC == 2:
            print()
            print("PERDISTE EL JUEGO")
            break
    
#ejecutamos el juego completo
Game()