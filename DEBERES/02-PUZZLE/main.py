import pygame
import random
import sys
from pygame.locals import *

columnas = 3
filas = 3
tamano_fuente = 20
tamano_cuadrado = 100
ancho_ventana = 400
alto_ventana = 400
velocidad = 100
blanco = None

color_fondo = (32, 56, 54)
color_cuadrado = (39, 184, 123)
color_texto = (255, 255, 255)
color_borde = (52, 143, 121)
color_mensaje = (255, 255, 255)

margen_x = int((ancho_ventana - (tamano_cuadrado * columnas + (columnas - 1))) / 2)
margen_y = int((alto_ventana - (tamano_cuadrado * filas + (filas - 1))) / 2)

arriba = 'up'
abajo = 'down'
izquierda = 'left'
derecha = 'right'


def main():
    global velocidad_fps, pantalla, fuente, NEW_RECT

    pygame.init()
    velocidad_fps = pygame.time.Clock()
    pantalla = pygame.display.set_mode((ancho_ventana, alto_ventana))
    pygame.display.set_caption('DEBER 2 - PYTHON')
    fuente = pygame.font.Font('freesansbold.ttf', tamano_fuente)

    tablero_principal, sec_solucion = generar_puzzle(50)
    tablero_resuelto = get_tablero_inicial()  # un tablero resuelto es igual a su estado inicial
    lista_movimientos = []  # lista de movimientos realizados

    while True:  # bucle principal del juego
        deslizarce = None
        msg = '     CLICK PARA MOVER LAS PIEZAS'
        if tablero_principal == tablero_resuelto:
            msg = '        FELICITACIONES GANASTE!'

        dibujar_tablero(tablero_principal, msg)

        revisar_salir()
        for evento in pygame.event.get():  # bucle de manejo de eventos
            if evento.type == MOUSEBUTTONUP:
                pos_x, pos_y = get_clicked(tablero_principal, evento.pos[0], evento.pos[1])

                # comprobar si el cuadrado en el que se hizo click estaba junto al espacio en blanco
                if (pos_x, pos_y) != (None, None):
                    blanco_x, blanco_y = get_posicion_blanco(tablero_principal)

                    if pos_x == blanco_x + 1 and pos_y == blanco_y:
                        deslizarce = izquierda
                    elif pos_x == blanco_x - 1 and pos_y == blanco_y:
                        deslizarce = derecha
                    elif pos_x == blanco_x and pos_y == blanco_y + 1:
                        deslizarce = arriba
                    elif pos_x == blanco_x and pos_y == blanco_y - 1:
                        deslizarce = abajo

        if deslizarce:
            crear_animacion(tablero_principal, deslizarce, '     CLICK PARA MOVER LAS PIEZAS', 8)
            realizar_movimiento(tablero_principal, deslizarce)
            lista_movimientos.append(deslizarce)  # guardar movimiento
        pygame.display.update()
        velocidad_fps.tick(velocidad)


def generar_puzzle(num_mov):
    secuencia = []
    tablero = get_tablero_inicial()
    dibujar_tablero(tablero, '')
    pygame.display.update()
    pygame.time.wait(50)
    ultimo_movimiento = None

    for i in range(num_mov):
        mov = get_movimiento_aleatorio(tablero, ultimo_movimiento)
        crear_animacion(tablero, mov, 'Generando...', velocidad_animacion=int(tamano_cuadrado / 1))
        realizar_movimiento(tablero, mov)
        secuencia.append(mov)
        ultimo_movimiento = mov
    return (tablero, secuencia)


def get_tablero_inicial():
    # Retorna la estructura de datos del tablero
    # returns [[1, 4, 7], [2, 5, 8], [3, 6, BLANK]]
    contador = 1
    tablero = []
    for x in range(columnas):
        column = []
        for y in range(filas):
            column.append(contador)
            contador += columnas
        tablero.append(column)
        contador -= columnas * (filas - 1) + columnas - 1

    tablero[columnas - 1][filas - 1] = blanco
    return tablero


def get_movimiento_aleatorio(tablero, ultimo_movimiento=None):
    # comienza con una lista completa de los cuatro movimientos
    movimientos_validos = [arriba, abajo, izquierda, derecha]

    # eliminar movimientos de la lista que ya que están descalificados
    if ultimo_movimiento == arriba or not is_valid_move(tablero, abajo):
        movimientos_validos.remove(abajo)
    if ultimo_movimiento == abajo or not is_valid_move(tablero, arriba):
        movimientos_validos.remove(arriba)
    if ultimo_movimiento == izquierda or not is_valid_move(tablero, derecha):
        movimientos_validos.remove(derecha)
    if ultimo_movimiento == derecha or not is_valid_move(tablero, izquierda):
        movimientos_validos.remove(izquierda)

    # return a random move from the list of remaining moves
    return random.choice(movimientos_validos)


def is_valid_move(tablero, movimiento):
    blanco_x, blanco_y = get_posicion_blanco(tablero)
    return (movimiento == arriba and blanco_y != len(tablero[0]) - 1) or \
           (movimiento == abajo and blanco_y != 0) or \
           (movimiento == izquierda and blanco_x != len(tablero) - 1) or \
           (movimiento == derecha and blanco_x != 0)


def realizar_movimiento(tablero, movimiento):

    blanco_x, blanco_y = get_posicion_blanco(tablero)

    if movimiento == arriba:
        tablero[blanco_x][blanco_y], tablero[blanco_x][blanco_y + 1] = tablero[blanco_x][blanco_y + 1], tablero[blanco_x][blanco_y]
    elif movimiento == abajo:
        tablero[blanco_x][blanco_y], tablero[blanco_x][blanco_y - 1] = tablero[blanco_x][blanco_y - 1], tablero[blanco_x][blanco_y]
    elif movimiento == izquierda:
        tablero[blanco_x][blanco_y], tablero[blanco_x + 1][blanco_y] = tablero[blanco_x + 1][blanco_y], tablero[blanco_x][blanco_y]
    elif movimiento == derecha:
        tablero[blanco_x][blanco_y], tablero[blanco_x - 1][blanco_y] = tablero[blanco_x - 1][blanco_y], tablero[blanco_x][blanco_y]


def dibujar_tablero(tablero, mensaje):

    pantalla.fill(color_fondo)

    if mensaje:
        textSurf, textRect = crear_texto(mensaje, color_mensaje, color_fondo, 5, 5)
        pantalla.blit(textSurf, textRect)

    for cuadrado_x in range(len(tablero)):
        for cuadrado_y in range(len(tablero[0])):
            if tablero[cuadrado_x][cuadrado_y]:
                dibujar_cuadrado(cuadrado_x, cuadrado_y, tablero[cuadrado_x][cuadrado_y])

    left, top = get_sup_izq_cuadrado(0, 0)
    ancho = columnas * tamano_cuadrado
    alto = filas * tamano_cuadrado
    pygame.draw.rect(pantalla, color_borde, (left - 5, top - 5, ancho + 11, alto + 11), 4)


def dibujar_cuadrado(cuadrado_x, cuadrado_y, numero, adjx=0, adjy=0):
    # Dibuja un cuadrado en las coordenadas del tablero que recibe como parametro
    izq, sup = get_sup_izq_cuadrado(cuadrado_x, cuadrado_y)
    pygame.draw.rect(pantalla, color_cuadrado, (izq + adjx, sup + adjy, tamano_cuadrado, tamano_cuadrado))
    textSurf = fuente.render(str(numero), True, color_texto)
    textRect = textSurf.get_rect()
    textRect.center = izq + int(tamano_cuadrado / 2) + adjx, sup + int(tamano_cuadrado / 2) + adjy
    pantalla.blit(textSurf, textRect)


def crear_texto(text, color, bgcolor, top, left):
    # Crear los objetovs Surface y Rect para algún texto.
    textSurf = fuente.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)


def crear_animacion(tablero, direccion, mensaje, velocidad_animacion):
    blanco_x, blanco_y = get_posicion_blanco(tablero)
    if direccion == arriba:
        moverse_x = blanco_x
        moverse_y = blanco_y + 1
    elif direccion == abajo:
        moverse_x = blanco_x
        moverse_y = blanco_y - 1
    elif direccion == izquierda:
        moverse_x = blanco_x + 1
        moverse_y = blanco_y
    elif direccion == derecha:
        moverse_x = blanco_x - 1
        moverse_y = blanco_y

    # Prepara la superficie base
    dibujar_tablero(tablero, mensaje)
    baseSurf = pantalla.copy()
    # Dibujar cuadrado en blanco sobre el cuadrado en movimiento
    moverse_izq, moverse_sup = get_sup_izq_cuadrado(moverse_x, moverse_y)
    pygame.draw.rect(baseSurf, color_fondo, (moverse_izq, moverse_sup, tamano_cuadrado, tamano_cuadrado))

    for i in range(0, tamano_cuadrado, velocidad_animacion):
        # Animar el cuadrado deslizandose sobre el tablero
        revisar_salir()
        pantalla.blit(baseSurf, (0, 0))
        if direccion == arriba:
            dibujar_cuadrado(moverse_x, moverse_y, tablero[moverse_x][moverse_y], 0, -i)
        if direccion == abajo:
            dibujar_cuadrado(moverse_x, moverse_y, tablero[moverse_x][moverse_y], 0, i)
        if direccion == izquierda:
            dibujar_cuadrado(moverse_x, moverse_y, tablero[moverse_x][moverse_y], -i, 0)
        if direccion == derecha:
            dibujar_cuadrado(moverse_x, moverse_y, tablero[moverse_x][moverse_y], i, 0)

        pygame.display.update()
        velocidad_fps.tick(velocidad)


def get_posicion_blanco(board):
    # Devuelve las coordenadas x & y del tablero del espacio en blanco.
    for x in range(columnas):
        for y in range(filas):
            if board[x][y] == blanco:
                return (x, y)


def get_sup_izq_cuadrado(cuadrado_x, cuadrado_y):
    izq = margen_x + (cuadrado_x * tamano_cuadrado) + (cuadrado_x - 1)
    sup = margen_y + (cuadrado_y * tamano_cuadrado) + (cuadrado_y - 1)
    return (izq, sup)


def get_clicked(tablero, x, y):
    # A partir de las coordenadas de píxel x & y, obtenga las coordenadas del tablero x & y
    for cuadrado_x in range(len(tablero)):
        for cuadrado_y in range(len(tablero[0])):
            izq, sup = get_sup_izq_cuadrado(cuadrado_x, cuadrado_y)
            tileRect = pygame.Rect(izq, sup, tamano_cuadrado, tamano_cuadrado)
            if tileRect.collidepoint(x, y):
                return (cuadrado_x, cuadrado_y)
    return (None, None)


def revisar_salir():
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
