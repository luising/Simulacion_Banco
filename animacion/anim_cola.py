"""Animacion de la cola."""


class anCola(object):
    """docstring for anCola."""

    def __init__(self, sup, us):
        """Intancia."""
        super(anCola, self).__init__()
        posInicial = [10, 400]
        self.v = sup
        self.usuario = us
        self.cola = []
        self.caja = crear_caja(4)
        self.velocidad = 1
        self.movimientoCola = [[posInicial[:], 0] for _ in range(4)]
        self.entrando = [580, 400]

    def agregar_cola(self):
        """Agregar Usuario."""
        if len(self.cola) < 1:
            self.cola.append([10, 400])
        else:
            pos = [self.cola[-1][0] + 72, 400]
            self.cola.append(pos)

    def mover_Usuario(self):
        """MoverUsuario."""
        for i in range(len(self.movimientoCola)):
            pos = self.movimientoCola[i][0]
            if self.movimientoCola[i][1]:
                self.movimientoCola[i][0] = self.atender_cliente(pos, i)
                if type(self.movimientoCola[i][0]) == int:
                    self.movimientoCola[i][1] = 0
                    self.movimientoCola[i][0] = [10, 400]
                    return 1
            self.crear_Usuario(self.movimientoCola[i][0])

    def entrando_cola(self):
        """Entrando la simulacion."""
        if len(self.cola) > 1:
            u = self.cola[-1][0]
        else:
            u = 10
        if self.entrando[0] > u:
            self.entrando[0] -= self.velocidad
        else:
            self.entrando = [580, 400]
            return 1
        self.crear_Usuario(self.entrando)

    def atender_cliente(self, pos, ncaja):
        """Atender cliente."""
        if pos[0] < self.caja[ncaja][0][0]:
            pos[0] += self.velocidad
        if pos[1] > self.caja[ncaja][0][1]:
            pos[1] -= self.velocidad
        if pos == self.caja[ncaja][0]:
            return 1
        return pos

    def mostrar_cola(self):
        """Prueba de cola."""
        for pos in self.cola:
            self.crear_Usuario(pos)

    def crear_Usuario(self, pos):
        """Entra un usuario."""
        self.v.blit(self.usuario, pos)

    def sacar_cola(self):
        """Eliminar uno de la cola."""
        self.cola.pop()


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
