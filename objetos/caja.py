"""Clase caja."""
import tools.generadorVariables as gv


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

    def setUsuario(self, reloj):
        """Agregar cliente atendiendo."""
        c_caja = self.atributos
        c_caja['disponible'] = False
        c_caja['ts_actual'] = gv.generate_ts()
        c_caja['ts_actual_mas_reloj'] = round(c_caja['ts_actual']) + reloj
        c_caja['#_usuarios_usaron'] += 1
        c_caja['t_s_total'] += c_caja['ts_actual']
        self.atributos = c_caja
