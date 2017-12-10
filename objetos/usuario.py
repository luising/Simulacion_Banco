"""Clase usuario."""


class Usuario(object):
    """docstring for Usuario."""

    def __init__(self, tll, tiempo_llegada, reloj):
        """Intancia del objeto."""
        super(Usuario, self).__init__()
        self.atributos = {
            'tll': tll,
            'tll_mas_reloj': tiempo_llegada,
            'ts_actual': 0,
            'ts_actual_mas_reloj': 0,
            'tiempo_en_cola': reloj,
            'en_cola': True,
            'activo': True
        }

    def solicitarPedido(self, ts, tsplus, reloj):
        """Usuario sera atendiendo."""
        c_usuario = self.atributos
        c_usuario['ts_actual'] = ts
        c_usuario['ts_actual_mas_reloj'] = tsplus
        c_usuario['tiempo_en_cola'] = reloj - c_usuario['tiempo_en_cola']
        self.atributos = c_usuario
