def crear_tablero():
# Esta funcion crea un tablero vacio
    print("Este es el tablero inicial: ")
    tablero = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]        
    return tablero

def imprimir_formato(tablero):
# Esta funcion imprime el tablero en un formato mas lindo
    filas = len(tablero)
    cols = len(tablero)
    print("---+---+---")
    for r in range(filas):
        print(tablero[r][0], " |", tablero[r][1], "|", tablero[r][2])
        print("---+---+---")
    return tablero


#contar filas, columnas y diagonales con 2 elementos y 1 espacio (proximas a ganar), retorna 2 valores ind1 para quasilineas de 0 e ind2 para quasilineas de X
def contar_quasilineas(tablero, simbolo):
    contador_filas = 0
    contador_columnas = 0
    contador_diagonales = 0

    for fila in tablero:
        if fila.count(simbolo) == 2 and fila.count(' ') == 1:
            contador_filas += 1
       
    
    for i in range(3):
        columna = [tablero[0][i], tablero[1][i], tablero[2][i]]
        if columna.count(simbolo) == 2 and columna.count(' ') == 1:
            contador_columnas += 1
        
        
    diagonal1 = [tablero[0][0], tablero[1][1], tablero[2][2]]
    diagonal2 = [tablero[0][2], tablero[1][1], tablero[2][0]]
    if diagonal1.count(simbolo) == 2 and diagonal1.count(' ') == 1:
        contador_diagonales += 1
    
    
    if diagonal2.count(simbolo) == 2 and diagonal2.count(' ') == 1:
        contador_diagonales += 1
    
    
    ind1_2 = contador_filas + contador_columnas + contador_diagonales

    return ind1_2

#contar filas, columnas y diagonales con 2 elemento y 1 espacios (proximas a ganar) para la siguiente jugada de 'O', retorna 2 valores ind1 para quasilineas de 0 e ind2 para quasilineas de X
def contar_quasilineas_proximaJugada(tablero, simbolo):
    contador_filas = 0
    contador_columnas = 0
    contador_diagonales = 0


    #colocar un 'O' en cada espacio vacio para la proxima jugada y contar las quasilineas
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == ' ':
                tablero[i][j] = simbolo
                #contar filas con 2 'O' o 'X' y 1 espacio vacio
                for fila in tablero:
                    if fila.count(simbolo) == 2 and fila.count(' ') == 1:
                        contador_filas += 1
                    
                #contar columnas con 2 'O' o 'X' y 1 espacio vacio
                for i in range(3):
                    columna = [tablero[0][i], tablero[1][i], tablero[2][i]]
                    if columna.count(simbolo) == 2 and columna.count(' ') == 1:
                        contador_columnas += 1
                    
                #contar diagonales con 2 'O' o 'X' y 1 espacio vacio
                diagonal1 = [tablero[0][0], tablero[1][1], tablero[2][2]]
                diagonal2 = [tablero[0][2], tablero[1][1], tablero[2][0]]
                if diagonal1.count(simbolo) == 2 and diagonal1.count(' ') == 1:
                    contador_diagonales += 1 
                if diagonal2.count(simbolo) == 2 and diagonal2.count(' ') == 1:
                    contador_diagonales += 1
               
                #reinizalizar el tablero
                tablero[i][j] = ' '
    
    ind7_8 = contador_filas + contador_columnas + contador_diagonales

    return ind7_8

   

def contar_esquinas(tablero, simbolo):
    contador = 0
    esquinas = [tablero[0][0], tablero[0][2], tablero[2][0], tablero[2][2]]
    for esquina in esquinas:
        if esquina == simbolo:
            contador += 1
    return contador


def es_ganador(tablero, simbolo):
    # Verificar las filas
    for fila in range(3):
        if tablero[fila][0] == tablero[fila][1] == tablero[fila][2] == simbolo:
            return True

    # Verificar las columnas
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] == simbolo:
            return True

    # Verificar las diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == simbolo:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == simbolo:
        return True

    return False

#contar filas, columnas y diagonales con 2 'O' y 1 espacio
"""
def contar_quasilineas(tablero):
    contador_filas = 0
    contador_columnas = 0
    contador_diagonales = 0

    for fila in tablero:
        if fila.count('O') == 2 and fila.count(' ') == 1:
            contador_filas += 1

    for i in range(3):
        columna = [tablero[0][i], tablero[1][i], tablero[2][i]]
        if columna.count('O') == 2 and columna.count(' ') == 1:
            contador_columnas += 1

    diagonal1 = [tablero[0][0], tablero[1][1], tablero[2][2]]
    diagonal2 = [tablero[0][2], tablero[1][1], tablero[2][0]]
    if diagonal1.count('O') == 2 and diagonal1.count(' ') == 1:
        contador_diagonales += 1
    if diagonal2.count('O') == 2 and diagonal2.count(' ') == 1:
        contador_diagonales += 1

    return contador_filas, contador_columnas, contador_diagonales
"""

def evaluar_tablero(tablero, simboloOrdenador, simboloHumano):
    # Calcula los indicadores
    ind1 = contar_quasilineas(tablero, simboloOrdenador) # ind1 para quasilineas de jugador Ordenador
    ind2 = contar_quasilineas(tablero, simboloHumano) # ind2 para quasilineas de jugador Humano
    ind3 = contar_esquinas(tablero, simboloOrdenador) #ind3 para esquinas de jugador Ordenador 
    ind4 = contar_esquinas(tablero, simboloHumano) #ind4 para esquinas de jugador Humano
    ind5 = sum([fila.count(simboloOrdenador) for fila in tablero]) #ind5 para contar simbolos de jugador Ordenador 
    ind6 = sum([fila.count(simboloHumano) for fila in tablero]) #ind6 para contar simbolos de jugador Humano
    ind7 = contar_quasilineas_proximaJugada(tablero, simboloOrdenador) #ind7 para quasilineas de jugador Ordenador en la proxima jugada
    ind8 = contar_quasilineas_proximaJugada(tablero, simboloHumano) #ind8 para quasilineas de jugador Humano en la proxima jugada
    
    if es_ganador(tablero, simboloOrdenador):
        ind9 = 100000000000000000
        print("Gana Ordenador")
    elif es_ganador(tablero, simboloHumano):
        ind9 = -100000000000000000
        print("Gana Humano")
    elif not hayMovimientos(tablero):
        ind9 = 0
        print("Empate")
    else:
        ind9 = 1
        # iniciarJuego(tablero, simboloOrdenador, simboloHumano, True)

    # Coeficientes
    W1, W2, W3, W4, W5, W6, W7, W8, W9 = 5, -5, 3, -3, 1, -1, 4, -4, ind9

    # Ho = W9 * (W1 * ind1 + W2 * ind2 + W3 * ind3 + W4 * ind4 + W5 * ind5 + W6 * ind6 + W7 * ind7 + W8 * ind8)
    Ho = W9 * (W1 * ind1 + W2 * ind2 + W3 * ind3 + W4 * ind4 + W5 * ind5 + W6 * ind6 + W7 * ind7 + W8 * ind8)


    return Ho



def minimax(tablero, depth, isMaximizing, simboloOrdenador, simboloHumano):
    score = evaluar_tablero(tablero, simboloOrdenador, simboloHumano)

    # Base Cases
    if score >= 100000000000000000:  
        return score
    if score <= -100000000000000000:  
        return score
    if not hayMovimientos(tablero):  
        return 0

    if isMaximizing:
        maxEval = float('-inf')
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == ' ':
                    tablero[i][j] = simboloOrdenador
                    eval = minimax(tablero, depth + 1, False, simboloOrdenador, simboloHumano)
                    maxEval = max(maxEval, eval)
                    tablero[i][j] = ' '
        return maxEval

    else:
        minEval = float('inf')
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == ' ':
                    tablero[i][j] = simboloHumano
                    eval = minimax(tablero, depth + 1, True, simboloOrdenador, simboloHumano)
                    minEval = min(minEval, eval)
                    tablero[i][j] = ' '
        return minEval

def hayMovimientos(tablero):
    for fila in tablero:
        for celda in fila:
            if celda == ' ':
                return True
    return False

def encontrar_mejor_jugada(tablero, simboloOrdenador, simboloHumano):
    mejor_valor = -float('inf')
    mejor_movimiento = (-1, -1)

    for i in range(3):
        for j in range(3):
            if tablero[i][j] == ' ':
                tablero[i][j] = simboloOrdenador
                valor_movimiento = minimax(tablero, 0, False, simboloOrdenador, simboloHumano)  # Corrección aquí
                tablero[i][j] = ' '
                
                if valor_movimiento > mejor_valor:
                    mejor_movimiento = (i, j)
                    mejor_valor = valor_movimiento

    return mejor_movimiento


def intro():
# Esta funcion da la bienvenida al usuario, e introduce las reglas del juego
    print("Hola! Bienvenido al juego de Triqui")
    print("\n")
    print("Es un juego para dos jugadores, donde se alterna para colocar sus respectivos simbolos en un tablero de 3x3 casillas."
          "Uno de los jugadores utiliza el simbolo 'X' mientras que el otro utiliza 'O'."
          "El juego termina cuando uno de los jugadores logra una linea horizontal, vertical o diagonal de tres de sus propios simbolos antes que el oponente. o cuando el tablero esta lleno, resultando en un empate."
          )
    print("\n")
    input("Presiona enter para continuar")
    print("\n")

def jugador_humano():
    # Esta función le pide al jugador que ingrese el símbolo con el que va a jugar y el turno en el que va a jugar
    simbolo = input("Jugador, ingresa el simbolo con el que quieres jugar (X/O): ")
    while simbolo != "X" and simbolo != "O":
        simbolo = input("Jugador, ingresa el simbolo con el que quieres jugar (X/O): ")

    # turno = int(input("Jugador, ingresa el turno en el que quieres jugar (1/2): "))
    # while turno != 1 and turno != 2:
    #     turno = int(input("Jugador, ingresa el turno en el que quieres jugar (1/2): "))

    return simbolo
    
# def jugador_ordenador():


#iniciar juego

def iniciarJuego(tablero, simboloOrdenador, simboloHumano, turno):
    while True:  # Ciclo principal del juego
        imprimir_formato(tablero)
        
        # Comprobamos si el juego ha terminado antes del siguiente movimiento
        if es_ganador(tablero, simboloHumano):
            print("¡Ganaste!")
            return
        elif es_ganador(tablero, simboloOrdenador):
            print("¡Gana la computadora!")
            return
        elif not hayMovimientos(tablero):
            print("¡Es un empate!")
            return

        # Movimiento del jugador
        if turno:
            fila = int(input("Jugador, elige la fila (0, 1, 2): "))
            columna = int(input("Jugador, elige la columna (0, 1, 2): "))

            # Asegurarse de que la posición seleccionada esté vacía
            while tablero[fila][columna] != ' ':
                print("La celda ya está ocupada. Elije otra.")
                fila = int(input("Jugador, elige la fila (0, 1, 2): "))
                columna = int(input("Jugador, elige la columna (0, 1, 2): "))

            tablero[fila][columna] = simboloHumano
            turno = not turno

        # Movimiento del ordenador
        else:
            mejor_movimiento = encontrar_mejor_jugada(tablero, simboloOrdenador, simboloHumano)
            tablero[mejor_movimiento[0]][mejor_movimiento[1]] = simboloOrdenador
            turno = not turno

    # Si el tablero está lleno y no hay un ganador, es un empate
    print("¡Es un empate!")

def main():
# Funcion main
    intro()
    tablero = crear_tablero()
    imprimir_formato(tablero)
    
    simboloHumano = jugador_humano()
    simboloOrdenador = 'O' if simboloHumano == 'X' else 'X'
    
    # Preguntar al jugador humano si quiere empezar
    respuesta = input("¿Quieres empezar el juego? (si/no): ").lower()
    turno = True if respuesta == 'si' else False
    
    iniciarJuego(tablero, simboloOrdenador, simboloHumano, turno)

if __name__ == '__main__':
    main()



# Nota: Esta es una implementación básica del algoritmo Minimax. En un juego real, querrías optimizar esto usando alfa-beta pruning y tal vez una tabla de transposición para guardar estados previamente evaluados.

