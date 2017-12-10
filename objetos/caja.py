"""Clase caja."""
import tools.generadorVariables as gv


class Caja(object):
    """docstring for Caja."""

    def __init__(self):
        """Instancia de caja."""
        super(Caja, self).__init__()
        self.atributos = {
            'disponible': True,
            'tipo': ("", 0),
            '#_usuarios_usaron': 0,
            'ts_actual': 0,
            'ts_actual_mas_reloj': 0,
            't_s_total': 0,
            'deposito': 0,
            'retiro': 0,
            'pago': 0,
            't_ocio': 0
        }

    def setUsuario(self, reloj):
        """Agregar cliente atendiendo."""
        c_caja = self.atributos
        c_caja['disponible'] = False
        c_caja['tipo'] = gv.generate_request()
        c_caja['ts_actual'] = c_caja['tipo'][1]
        c_caja[c_caja['tipo'][0]] += 1
        c_caja['ts_actual_mas_reloj'] = round(c_caja['ts_actual']) + reloj
        c_caja['#_usuarios_usaron'] += 1
        c_caja['t_s_total'] += c_caja['ts_actual']
        self.atributos = c_caja
