"""Clase animacion."""
import pygame
import sys
from pygame.locals import QUIT
from animacion.gui import gui
from animacion.anim_cola import anCola
from animacion.anim_caja import anCaja
pygame.init()


class anim(object):
    """Docstring for anim."""

    def __init__(self):
        """Intancia."""
        super(anim, self).__init__()
        self.ventana = pygame.display.set_mode((1000, 483))
        pygame.display.set_caption("Simulacion de banco")
        self.fondo = pygame.image.load("p2.jpg").convert()
        self.usuario = pygame.image.load("pspr.png")
        self.pData = 0
        self.pLi = []
        self.g = gui(self.ventana)
        self.acl = anCola(self.ventana, self.usuario)
        self.acj = anCaja(self.ventana, self.usuario)
        self.cargar_fondo()
        self.an_update()

    def an_cola_caja(self, cajad):
        """Activar animacion caminar a la caja."""
        self.acl.sacar_cola()
        self.acl.movimientoCola[cajad][1] = 1
        while 1:
            self.cargar_fondo()
            en = self.acl.mover_Usuario()
            if en:
                self.acj.agregar_caja(cajad)
                return
            self.an_update()

    def an_salir_caja(self, cajad):
        """Activar animacion saliendo a la caja."""
        self.acj.saliendo[cajad][1] = 1
        while 1:
            self.cargar_fondo()
            en = self.acj.salir_Caja()
            if en:
                return
            self.an_update()

    def an_entrando_cola(self):
        """Activar animacion saliendo a la caja."""
        while 1:
            self.cargar_fondo()
            en = self.acl.entrando_cola()
            self.an_update()
            if en:
                self.acl.agregar_cola()
                return

    def intefaz(self):
        """Mostrar Datos."""
        self.g.panel(self.pData)
        self.g.caja(self.pLi)

    def cargar_fondo(self):
        """cargar_fondo."""
        self.ventana.fill((255, 255, 255))
        self.ventana.blit(self.fondo, (0, 0))
        self.acl.mostrar_cola()
        self.acj.mostrar_caja()
        self.intefaz()

    def an_update(self):
        """Actualizar."""
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

    def cargar_salida(self):
        """Cargar Fin."""
        self.ventana.fill((255, 255, 255))

    def pantalla_fin(self, listEndogena):
        """Mostrar."""
        while 1:
            self.cargar_salida()
            self.g.an_mov_Fin(listEndogena)
            self.an_update()
