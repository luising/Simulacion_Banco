"""Clase para guardar en txt."""


class svtxt(object):
    """docstring for svtxt."""

    def __init__(self):
        """Instancia de la clase."""
        super(svtxt, self).__init__()
        self.fw = open('resultados/procedimiento.txt', 'w')
        self.fw1 = open('resultados/estadoActual.txt', 'w')
        self.fw2 = open('resultados/resultadosFinales.txt', 'w')

    def wGeneraTll(self, tll):
        """Guardar tll."""
        self.fw.write('\n')
        self.fw.write('-------------------Se genera un TLL---------------- \n')
        self.fw.write(aviso_tll(tll) + '\n')
        self.fw.write('--------------------------------------------------- \n')

    def wllegaUsuario(self, tll, reloj, cola):
        """Guardar llego un usuario."""
        self.fw.write('\n')
        self.fw.write('-------------------Llega un usuario a la cola------ \n')
        self.fw.write('El usuario llego al segundo: ' + str(reloj) + '\n')
        self.fw.write('La cola actual es de :' + str(cola) + '\n')
        self.fw.write(aviso_tll(tll) + '\n')
        self.fw.write('--------------------------------------------------- \n')

    def wSaleUsuarioCola(self, r, tr, k, utc):
        """Guardar usuario sera atendiendo."""
        m = """\n
            -------------------Sale un usuario de la cola-------\n
            El usuario sale de la cola al segundo: """ + str(r) + """'\n'
            Sale de la cola el usuario que llego al segundo """ + str(tr) + """
            y pasa a la caja[""" + str(k) + """] \n'
            El usuario paso: """ + str(utc) + """ segundos en la cola \n
            ----------------------------------------------------- \n"""
        self.fw.write(m)

    def wUsuarioAtendido(self, utr, uta, i):
        """Usuario atendido."""
        m = """\n
            ---------Termina el servicio de un usuario--------- \n
            El usuario sale del servicio al segundo: """ + str(utr) + """\n
            La caja[""" + str(i) + """] se libera, el usuario tardo en salir:
            """ + str(uta) + """ segundos. \n
            --------------------------------------------------- \n"""
        self.fw.write(m)

    def wFinCiclo(self, reloj, cola):
        """Mostrar datos de estado."""
        self.fw1.write('///////////// FINAL DEL CICLO ACTUAL //////////// \n')
        self.fw1.write('Ciclo actual: ' + str(reloj) + '\n')
        self.fw1.write('\n')
        self.fw1.write('Longitud de cola: ' + str(cola) + '\n')

    def wCajaOcio(self, ocio, ocupado):
        """Mostarar estado de las cajas."""
        self.fw1.write('\n')
        self.fw1.write('Cajas disponibles: \n')
        for i in ocio:
            self.fw1.write('Caja[' + str(i) + '] disponible \n')
        self.fw1.write('\n')
        self.fw1.write('Cajas no disponibles (estan siendo usadas) \n')
        for i in ocupado:
            self.fw1.write('Caja[' + str(i) + '] no disponible \n')
        self.fw1.write('////////////// /////////// ///////////////////// \n')

    def wTiempoPromedio(self, ta, tlp, tcp):
        """Mostrar tiempo promedio."""
        m = """\n\n
        Resultados finales de la simulacion
        El total de usuarios que pasaron por la cola fue de: """ + str(ta) + """
        \n\n\n
        EL tiempo de cola promedio de los usuarios fue de: """ + str(tcp) + """
        EL tiempo de llegada promedio de los usuarios fue de: """ + str(tlp)
        self.fw2.write(m)

    def WPromedioCaja(self, i, ut, co, tst, pc):
        """Mostrar caja promedio."""
        m = """\n
    	Caja[""" + str(i) + """]\n
            fue usada por un total de:""" + str(ut) + """ personas \n
    	    Tiempo de ocio fue de: """ + str(co) + """ segundos \n
    	    El tiempo de salida fue de: """ + str(tst) + """ segundos \n
            Promedio de tiempos de salida fue de: """ + str(pc) + """ segundos\n
        """
        self.fw2.write(m)

    def WPromedioOcio(self, top, tst):
        """Mostrar promedio de ocio."""
        self.fw2.write('\nEl tiempo de ocio promedio e: '+str(top)+' segundos')
        self.fw2.write('\nEl promedio de tiempo salida:'+str(tst)+'segundos')

    def close(self):
        """Cerrar archivos."""
        self.fw.close()
        self.fw1.close()
        self.fw2.close()

# Avisa cuando sera el tiempo de llegada
def aviso_tll(tll):
    """Mensaje de tiempo de llegada."""
    return 'El tiempo de llegada del siguiente cliente es: ' + str(tll)


def aviso_ts(ts):
    """Mensaje cuando sera el tiempo de salida."""
    return 'El tiempo de salida del siguiente cliente es: ' + str(ts)
