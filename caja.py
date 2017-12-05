"""Clase caja."""


class Caja(object):
    """docstring for Caja."""

    def __init__(self):
        """Instancia de caja."""
        super(Caja, self).__init__()
        self.atributos = {
            'disponible': True,
            '#_usuarios_usaron': 0,
            'ts_actual': 0,
            'ts_actual_mas_reloj': 0,
            't_s_total': 0,
            't_ocio': 0
        }
