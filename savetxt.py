"""Clase para guardar en txt."""
import showEstate as se


class svtxt(object):
    """docstring for svtxt."""

    def __init__(self):
        """Instancia de la clase."""
        super(svtxt, self).__init__()
        self.fw = open('procedimiento.txt', 'w')
        self.fw1 = open('estadoActual.txt', 'w')
        self.fw2 = open('resultadosFinales.txt', 'w')

    def wGeneraTll(self, tll):
        """Guardar tll."""
        self.fw.write('\n')
        self.fw.write('-------------------Se genera un TLL---------------- \n')
        self.fw.write(se.aviso_tll(tll) + '\n')
        self.fw.write('--------------------------------------------------- \n')

    def wllegaUsuario(self, tll, reloj, cola):
        """Guardar llego un usuario."""
        self.fw.write('\n')
        self.fw.write('-------------------Llega un usuario a la cola------ \n')
        self.fw.write('El usuario llego al segundo: ' + str(reloj) + '\n')
        self.fw.write('La cola actual es de :' + str(len(cola)) + '\n')
        self.fw.write(se.aviso_tll(tll) + '\n')
        self.fw.write('--------------------------------------------------- \n')
