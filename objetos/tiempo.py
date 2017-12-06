"""Clase Tiempo."""
import tools.generadorVariables as gv


class Time(object):
    """docstring for Time."""

    def __init__(self, max):
        """Intancia."""
        super(Time, self).__init__()
        self.tiempo_maximo = max
        self.tll = 0
        self.usuarios_que_salieron_de_la_cola = 0
        self.tiempo_llegada_promedio = 0
        self.tiempo_cola_promedio = 0
        self.tiempo_ocio_promedio = 0
        self.t_s_promedio_total = 0
        self.reloj = 0
        self.update_TLL()

    def update_TLL(self):
        """Actualizar tiempo de llegada."""
        self.tll = gv.generate_tll()
        self.tiempo_llegada = round(self.tll) + self.reloj
