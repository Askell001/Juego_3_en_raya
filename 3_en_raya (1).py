import os
import time
from colorama import Fore, init
import shutil

# Inicializar colorama
init(autoreset=True)

bucle = True
contador_jugador1 = 0
contador_jugador2 = 0

def imprimir_tablero(tablero):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.LIGHTYELLOW_EX+f"""
          ╔═════════════════════╗                       ╔════════════════════════╗ 
          ║       MARCADOR      ║                       ║ POSICIONES DEL TABLERO ║                       
          ╠═════════════════════╣                       ╠════════════════════════╣
          ║ JUGADOR 1: {contador_jugador1}        ║                       ║        1 ║ 2 ║ 3       ║
          ║ JUGADOR 2: {contador_jugador2}        ║                       ║        ══╬═══╬══       ║
          ╚═════════════════════╝                       ║        4 ║ 5 ║ 6       ║
                                                        ║        ══╬═══╬══       ║
                                                        ║        7 ║ 8 ║ 9       ║
                                                        ╚════════════════════════╝
          """+Fore.RESET)

    terminal_width = shutil.get_terminal_size().columns
    padding = (terminal_width - 17) // 2
    print(" " * padding)
    print("\t\t\t" + tablero[0] + Fore.LIGHTMAGENTA_EX + " ║ " + tablero[1] + Fore.LIGHTMAGENTA_EX + " ║ " + tablero[2] + Fore.RESET)
    print("\t\t\t" + Fore.LIGHTMAGENTA_EX + "══╬═══╬══" + Fore.RESET)
    print("\t\t\t" + tablero[3] + Fore.LIGHTMAGENTA_EX + " ║ " + tablero[4] + Fore.LIGHTMAGENTA_EX + " ║ " + tablero[5] + Fore.RESET)
    print("\t\t\t" + Fore.LIGHTMAGENTA_EX + "══╬═══╬══" + Fore.RESET)
    print("\t\t\t" + tablero[6] + Fore.LIGHTMAGENTA_EX + " ║ " + tablero[7] + Fore.LIGHTMAGENTA_EX + " ║ " + tablero[8] + Fore.RESET)
    print(" " * padding)

def ganador(tablero, jugador):
    combinaciones_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combinacion in combinaciones_ganadoras:
        if tablero[combinacion[0]] == tablero[combinacion[1]] == tablero[combinacion[2]] == jugador:
            return True
    return False

def jugar_tres_en_raya():
    global contador_jugador1, contador_jugador2
    rondas_totales = 5
    for ronda in range(rondas_totales):
        ronda += 1
        print(Fore.LIGHTCYAN_EX + f"""
                      ╔══════════════╗
                      ║  RONDA: {ronda}    ║
                      ╚══════════════╝
         """ + Fore.RESET)
        time.sleep(3)
        tablero = [" "] * 9
        jugador1 = Fore.BLUE + "X" + Fore.RESET
        jugador2 = Fore.RED + "O" + Fore.RESET
        juego_terminado = False
        turno = jugador1

        while not juego_terminado:
            imprimir_tablero(tablero)
            movimiento_valido = False
            while not movimiento_valido:
                movimiento = input(f"Elige una posición ({'Jugador 1' if turno == jugador1 else 'Jugador 2'}): ")
                if movimiento.isdigit():
                    movimiento = int(movimiento) - 1
                    if 0 <= movimiento <= 8 and tablero[movimiento] == " ":
                        tablero[movimiento] = turno
                        movimiento_valido = True
                    else:
                        print(Fore.RED + "Movimiento inválido. Inténtalo de nuevo." + Fore.RESET)
                else:
                    print("Entrada inválida. Inténtalo de nuevo.")
            
            if ganador(tablero, turno):
                imprimir_tablero(tablero)
                if turno == jugador1:
                    print(Fore.LIGHTGREEN_EX + """
                          ╔══════════════════╗
                          ║ ¡JUGADOR 1 GANA! ║
                          ╚══════════════════╝
                          """ + Fore.RESET)
                    contador_jugador1 += 1
                else:
                    print(Fore.LIGHTGREEN_EX + """
                          ╔══════════════════╗
                          ║ ¡JUGADOR 2 GANA! ║
                          ╚══════════════════╝
                          """ + Fore.RESET)
                    contador_jugador2 += 1
                juego_terminado = True
                time.sleep(3)
            elif " " not in tablero:
                imprimir_tablero(tablero)
                print(Fore.LIGHTMAGENTA_EX + """
                      ╔══════════════╗
                      ║ ¡EMPATE! ║
                      ╚══════════════╝
                      """ + Fore.RESET)
                juego_terminado = True
                time.sleep(3)
            else:
                turno = jugador2 if turno == jugador1 else jugador1

    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.LIGHTYELLOW_EX+f"""
        ╔═════════════════════╗ 
        ║    MARCADOR FINAL   ║                       
        ╠═════════════════════╣
        ║ JUGADOR 1: {contador_jugador1}          ║
        ║ JUGADOR 2: {contador_jugador2}          ║
        ╚═════════════════════╝
        """+Fore.RESET)
    
    print(Fore.LIGHTCYAN_EX+"""
            ╔═══════════════════╗
            ║ Gracias por jugar ║
            ╚═══════════════════╝
            
            """+Fore.RESET)
    input("Presiona ENTER para continuar...")

def main():
    global bucle
    os.system('cls' if os.name == 'nt' else 'clear')
    while bucle:
        os.system('cls' if os.name == 'nt' else 'clear')
        op = input("¿Desea jugar al 3 en raya (S/N)? ")
        if op.lower() == 's':
            os.system('cls' if os.name == 'nt' else 'clear')
            instrucciones()
            jugar_tres_en_raya()
        elif op.lower() == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Saliendo del juego...")
            input("Presiona ENTER para continuar...")
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opción inválida. Inténtalo de nuevo.")

def instrucciones():
    print(Fore.LIGHTYELLOW_EX+"""
    BIENVENIDO AL 3 EN RAYA:
        
    1) El juego se juega en un tablero de 3x3.
    2) Cada jugador tiene asignado un símbolo: uno es "X" y el otro es "O".
    3) El objetivo del juego es conseguir tres de tus símbolos en línea horizontal, vertical o diagonalmente.
    4) El jugador que utiliza el símbolo "X" siempre empieza primero.
    5) Los jugadores se turnan para colocar su símbolo en una casilla vacía del tablero.
    6) Para hacer tu movimiento, selecciona la posición en la que deseas colocar tu símbolo.
    7) Puedes seleccionar la posición escribiendo el número correspondiente a la casilla en el teclado (del 1 al 9).
    8) El juego verifica si tu movimiento es válido y coloca tu símbolo en la posición elegida.
    9) El siguiente jugador realiza su movimiento de la misma manera.
    10) El juego continúa hasta que un jugador consigue tres símbolos en línea o todas las casillas están ocupadas.
    11) Si un jugador consigue tres símbolos en línea, se declara como ganador.
    12) Si todas las casillas están ocupadas y no hay un ganador, el juego termina en empate.
    13) Después de que el juego haya terminado, puedes elegir si deseas jugar otra partida o salir del juego.     
          
    """+Fore.RESET)           
    input("Presiona ENTER para continuar...")

main()
