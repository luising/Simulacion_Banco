"""Animacion de la caja."""
import copy


class anCaja(object):
    """docstring for anCaja."""

    def __init__(self, sup, us):
        """Instancia."""
        super(anCaja, self).__init__()
        self.salida = [10, 70]
        self.v = sup
        self.usuario = us
        self.velocidad = .5
        self.caja = crear_caja(4)
        self.cajaOcupado = [0 for _ in range(4)]
        self.saliendo = [[copy.copy(self.caja[i][0]), 0] for i in range(4)]

    def salir_Caja(self):
        """Saliendo usuario."""
        for i in range(len(self.cajaOcupado)):
            if self.saliendo[i][1]:
                if self.saliendo[i][0][0] > self.salida[0]:
                    self.saliendo[i][0][0] -= self.velocidad
                if self.saliendo[i][0][0] <= self.salida[0]:
                    self.cajaOcupado[i] = 0
                    self.saliendo[i][0] = copy.copy(self.caja[i][0])
                    self.saliendo[i][1] = 0
                    self.caja[i][1] = 1
                    return 1
                self.crear_Usuario(self.saliendo[i][0])

    def agregar_caja(self, ncaja):
        """Agregar Usuario."""
        self.cajaOcupado[ncaja] = 1

    def mostrar_caja(self):
        """Prueba de cola."""
        for i, ocupado in enumerate(self.cajaOcupado):
            if ocupado:
                self.crear_Usuario(self.caja[i][0])

    def crear_Usuario(self, pos):
        """Entra un usuario."""
        self.v.blit(self.usuario, pos)


def crear_caja(ncola):
    """Crear caja."""
    primer = [[136, 70], 1]
    listpos = [primer]
    for i in range(1, ncola):
        pos = [[listpos[i - 1][0][0] + 150, 70], 1]
        listpos.append(pos)
    return listpos
