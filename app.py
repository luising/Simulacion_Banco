"""animacion de la simulacion."""
import pygame
import sys
import copy
from pygame.locals import QUIT
from animacion.gui import gui
pygame.init()


def intefaz():
    """Mostrar Datos."""
    # tll = "{0:.3f}".format(5.1234554321)
    g.panel()
    g.caja()


def control_evento():
    """Manejo de eventos."""
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


def crear_Usuario(pos):
    """Entra un usuario."""
    ventana.blit(usuario, pos)


def crear_cola(ncola):
    """Crear cola."""
    primer = [10, 400]
    listpos = [primer]
    for i in range(1, ncola):
        pos = [listpos[i - 1][0] + 72, 400]
        listpos.append(pos)
    return listpos


def crear_caja(ncola):
    """Crear caja."""
    primer = [[136, 70], 1]
    listpos = [primer]
    for i in range(1, ncola):
        pos = [[listpos[i - 1][0][0] + 150, 70], 1]
        listpos.append(pos)
    return listpos


def atender_cliente(pos, ncaja):
    """Atender cliente."""
    if pos[0] < caja[ncaja][0][0]:
        pos[0] += velocidad
    if pos[1] > caja[ncaja][0][1]:
        pos[1] -= velocidad
    if pos == caja[ncaja][0]:
        return 1
    return pos


def mostrar_cola():
    """Prueba de cola."""
    for pos in cola:
        crear_Usuario(pos)


def mostrar_caja():
    """Prueba de cola."""
    for i, ocupado in enumerate(cajaOcupado):
        if ocupado:
            crear_Usuario(caja[i][0])


def sacar_cola():
    """Eliminar uno de la cola."""
    cola.pop()


def salir_Caja():
    """Saliendo usuario."""
    for i in range(len(cajaOcupado)):
        if cajaOcupado[i]:
            saliendo[i][1] = 1
    for i in range(len(cajaOcupado)):
        if saliendo[i][1]:
            cajaOcupado[i] = 0
            if saliendo[i][0][0] > salida[0]:
                saliendo[i][0][0] -= velocidad
            if saliendo[i][0][0] <= salida[0]:

                saliendo[i][0] = copy.copy(caja[i][0])
                saliendo[i][1] = 0
                caja[i][1] = 1
            crear_Usuario(saliendo[i][0])


def obtener_caja_disponible():
    """Obtener caja disponible."""
    for i in range(len(caja)):
        if caja[i][1]:
            caja[i][1] = 0
            return i


def mover_Usuario():
    """MoverUsuario."""
    for i in range(len(movimientoCola)):
        if movimientoCola[i][1]:
            movimientoCola[i][0] = atender_cliente(movimientoCola[i][0], i)
            if type(movimientoCola[i][0]) == int:
                movimientoCola[i][1] = 0
                cajaOcupado[i] = 1
                movimientoCola[i][0] = [10, 400]

        crear_Usuario(movimientoCola[i][0])


ventana = pygame.display.set_mode((1000, 483))
pygame.display.set_caption("Simulacion de banco")
fondo = pygame.image.load("p2.jpg").convert()
usuario = pygame.image.load("pspr.png")
g = gui(ventana)

cola = crear_cola(7)
caja = crear_caja(4)
posInicial = [10, 400]
salida = [10, 70]

cajaOcupado = [0 for _ in range(4)]
saliendo = [[copy.copy(caja[i][0]), 0] for i in range(4)]
movimientoCola = [[posInicial[:], 0] for _ in range(4)]

velocidad = 1
atiende = 1000
cont = 0


while True:
    ventana.fill((255, 255, 255))
    ventana.blit(fondo, (0, 0))
    mostrar_caja()
    mostrar_cola()
    if cont > atiende:
        cont = 0
        sacar_cola()
        i = obtener_caja_disponible()
        print("mover a la caja", i)
        movimientoCola[i][1] = 1
    else:
        salir_Caja()
        cont += 1
    mover_Usuario()
    intefaz()
    control_evento()
