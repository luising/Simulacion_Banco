"""Clase usuario."""


class Usuario(object):
    """docstring for Usuario."""

    def __init__(self, tll, tll_mas_reloj, reloj):
        """Intancia del objeto."""
        super(Usuario, self).__init__()
        self.atributos = {
            'tll': tll,
            'tll_mas_reloj': tll_mas_reloj,
            'ts_actual': 0,
            'ts_actual_mas_reloj': 0,
            'tiempo_de_cola': 0,
            'tiempo_en_cola': reloj,
            'en_cola': True,
            'activo': True
        }
