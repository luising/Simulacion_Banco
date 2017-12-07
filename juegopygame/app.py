"""animacion de la simulacion."""
import pygame
import sys
from pygame.locals import QUIT
pygame.init()


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


def mostar_cola():
    """Prueba de cola."""
    for pos in cola:
        crear_Usuario(pos)


def mostar_caja():
    """Prueba de cola."""
    for pos in caja:
        crear_Usuario(pos)


def sacar_cola():
    """Eliminar uno de la cola."""
    cola.pop()


def obtener_caja_disponible():
    """Obtener caja disponible."""
    for i in range(len(caja)):
        if caja[i][1]:
            print(i)
            return i


ventana = pygame.display.set_mode((800, 483))
pygame.display.set_caption("Simulacion de banco")
fondo = pygame.image.load("p2.jpg").convert()
usuario = pygame.image.load("pspr.png")

cola = crear_cola(10)
caja = crear_caja(4)

velocidad = 1
atiende = 1000
cont = 0
atendiendo = 0
pos = cola[0]
while True:
    ventana.blit(fondo, (0, 0))
    mostar_caja()
    mostar_cola()
    if cont > atiende:
        cont = 0
        sacar_cola()
        atendiendo = 1
    else:
        cont += 1
    if(atendiendo):
        i = obtener_caja_disponible()
        pos = atender_cliente(pos, i)
        if type(pos) == int:
            caja[i][1] = 0
            pos = cola[0]
    control_evento()
