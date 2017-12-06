"""Clase Cola."""
from objetos.caja import Caja


class Cola(object):
    """docstring for Cola."""

    def __init__(self, caja):
        """intancia."""
        super(Cola, self).__init__()
        self.listUsuario = []
        self.listUsuarioAtentiendo = []
        self.cola = 0
        self.Ncajas = caja
        self.listcaja = []
        for _ in range(self.Ncajas):
            self.listcaja.append(Caja())

    def update_cola(self):
        """Actualizar cola usuario sera atendido."""
        self.listUsuarioAtentiendo.append(self.listUsuario[0])
        self.listUsuario.pop(0)
        self.cola -= 1
