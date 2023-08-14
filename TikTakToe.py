import copy


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
def contar_quasilineas_proximaJugada(tablero_original, simbolo):
    contador_filas = 0
    contador_columnas = 0
    contador_diagonales = 0

    # Colocar un 'O' o 'X' en cada espacio vacío para la próxima jugada y contar las quasilineas
    for i in range(3):
        for j in range(3):
            tablero = copy.deepcopy(tablero_original)  # Creamos una copia del tablero original al inicio de cada iteración
            if tablero[i][j] == ' ':
                tablero[i][j] = simbolo
                # contar filas con 2 'O' o 'X' y 1 espacio vacío
                for fila in tablero:
                    if fila.count(simbolo) == 2 and fila.count(' ') == 1:
                        contador_filas += 1
                    
                # contar columnas con 2 'O' o 'X' y 1 espacio vacío
                for k in range(3):
                    columna = [tablero[0][k], tablero[1][k], tablero[2][k]]
                    if columna.count(simbolo) == 2 and columna.count(' ') == 1:
                        contador_columnas += 1
                    
                # contar diagonales con 2 'O' o 'X' y 1 espacio vacío
                diagonal1 = [tablero[0][0], tablero[1][1], tablero[2][2]]
                diagonal2 = [tablero[0][2], tablero[1][1], tablero[2][0]]
                if diagonal1.count(simbolo) == 2 and diagonal1.count(' ') == 1:
                    contador_diagonales += 1 
                if diagonal2.count(simbolo) == 2 and diagonal2.count(' ') == 1:
                    contador_diagonales += 1

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
    if es_ganador(tablero, simboloOrdenador):
        ind9 = 100000000000000000
        # print("Gana Ordenador")
    elif es_ganador(tablero, simboloHumano):
        ind9 = -100000000000000000
        # print("Gana Humano")
    elif not hayMovimientos(tablero):
        ind9 = 0
        # print("Empate")
    else:
        ind9 = 1
        # iniciarJuego(tablero, simboloOrdenador, simboloHumano, True)
    # Calcula los indicadores
    ind1 = contar_quasilineas(tablero, simboloOrdenador) # ind1 para quasilineas de jugador Ordenador
    ind2 = contar_quasilineas(tablero, simboloHumano) # ind2 para quasilineas de jugador Humano
    ind3 = contar_esquinas(tablero, simboloOrdenador) #ind3 para esquinas de jugador Ordenador 
    ind4 = contar_esquinas(tablero, simboloHumano) #ind4 para esquinas de jugador Humano
    ind5 = sum([fila.count(simboloOrdenador) for fila in tablero]) #ind5 para contar simbolos de jugador Ordenador 
    ind6 = sum([fila.count(simboloHumano) for fila in tablero]) #ind6 para contar simbolos de jugador Humano
    ind7 = contar_quasilineas_proximaJugada(tablero, simboloOrdenador) #ind7 para quasilineas de jugador Ordenador en la proxima jugada
    ind8 = contar_quasilineas_proximaJugada(tablero, simboloHumano) #ind8 para quasilineas de jugador Humano en la proxima jugada
    

    # Coeficientes
    W1, W2, W3, W4, W5, W6, W7, W8, W9 = 5, -5, 3, -3, 1, -1, 4, -4, ind9

    # Ho = W9 * (W1 * ind1 + W2 * ind2 + W3 * ind3 + W4 * ind4 + W5 * ind5 + W6 * ind6 + W7 * ind7 + W8 * ind8)
    Ho = W9 * (W1 * ind1 + W2 * ind2 + W3 * ind3 + W4 * ind4 + W5 * ind5 + W6 * ind6 + W7 * ind7 + W8 * ind8)


    return Ho



def minimax(tablero, depth, isMaximizing, simboloOrdenador, simboloHumano):
    score = evaluar_tablero(tablero, simboloOrdenador, simboloHumano)
    
    # Base Cases
    if abs(score) == 100000000000000000 or depth == 9:  # Si hay un ganador o el tablero está lleno, retornamos la puntuación
        return score

    if isMaximizing:
        maxEval = float('-inf') # Inicializamos la evaluación con un valor muy pequeño
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == ' ':
                    tempTablero = [row.copy() for row in tablero]  # Creamos una copia del tablero para no modificar el original
                    tempTablero[i][j] = simboloOrdenador
                    eval = minimax(tempTablero, depth + 1, False, simboloOrdenador, simboloHumano)
                    maxEval = max(maxEval, eval)
        return maxEval

    else:
        minEval = float('inf') # Inicializamos la evaluación con un valor muy grande
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == ' ':
                    tempTablero = [row.copy() for row in tablero]  # Creamos una copia del tablero para no modificar el original
                    tempTablero[i][j] = simboloHumano
                    eval = minimax(tempTablero, depth + 1, True, simboloOrdenador, simboloHumano)
                    minEval = min(minEval, eval)
        return minEval

def hayMovimientos(tablero):
    for fila in tablero:
        for celda in fila:
            if celda == ' ':
                return True
    return False

def encontrar_mejor_jugada(tablero, simboloOrdenador, simboloHumano):
    maxScore = float('-inf')
    move = (-1, -1)
    
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == ' ':
                tempTablero = [row.copy() for row in tablero]  # Creamos una copia del tablero
                tempTablero[i][j] = simboloOrdenador
                score = minimax(tempTablero, 0, False, simboloOrdenador, simboloHumano)
                # Ya no es necesario "deshacer" el movimiento en el tablero original porque trabajamos con una copia
                if score > maxScore:
                    maxScore = score
                    move = (i, j)

    return move



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


def main():
    tableroJuego = crear_tablero()
    imprimir_formato(tableroJuego)
    
    while hayMovimientos(tableroJuego):
    # Jugada del humano
        for i in range(9):
            print("Turno: ", i)
            if i % 2 == 0: # Turno del humano
                while True:
                    try:
                        fila = int(input("Ingresa la fila (0, 1, 2): "))
                        columna = int(input("Ingresa la columna (0, 1, 2): "))

                        # Validar que la posición ingresada es válida y no está ocupada
                        if fila in [0, 1, 2] and columna in [0, 1, 2] and tableroJuego[fila][columna] == ' ':
                            break  # Salimos del bucle cuando el usuario ingresa valores válidos
                        else:
                            if fila not in [0, 1, 2] or columna not in [0, 1, 2]:
                                print("Valor fuera de rango. Por favor, ingresa valores entre 0 y 2.")
                            else:
                                print("Esa posición ya está ocupada. Intenta de nuevo.")
                    except ValueError:
                        print("Por favor, ingresa un número válido.")

                tableroJuego[fila][columna] = simboloHumano
                imprimir_formato(tableroJuego)
                tablero_actual = tableroJuego
                # Verificar si el humano ganó
                if es_ganador(tableroJuego, simboloHumano):
                    print("¡Felicidades, ganaste!")
                    return
        
                # Jugada de la computadora
                i, j = encontrar_mejor_jugada(tableroJuego, simboloOrdenador, simboloHumano)
                tableroJuego[i][j] = simboloOrdenador
                
                imprimir_formato(tableroJuego)

                # Verificar si la computadora ganó
                if es_ganador(tableroJuego, simboloOrdenador):
                    print("La computadora gana.")
                    return

if __name__ == "__main__":
    intro()
    simboloHumano = jugador_humano()
    simboloOrdenador = 'O' if simboloHumano == 'X' else 'X'
    main()










# Nota: Esta es una implementación básica del algoritmo Minimax. En un juego real, querrías optimizar esto usando alfa-beta pruning y tal vez una tabla de transposición para guardar estados previamente evaluados.

