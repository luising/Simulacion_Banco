"""Clase interfaz."""
from animacion.gui_text import Text


class gui(object):
    """docstring for gui."""

    def __init__(self, superficie):
        """Instancia."""
        super(gui, self).__init__()
        self.tx = Text(superficie)
        self.Dpanel = {
            "reloj": 0
        }
        self.lco = self.generate_coord()

    def panel(self, newData=0):
        """Dato del panel."""
        if type(newData) != int:
            self.Dpanel = newData
        it = 0
        for key, item in self.Dpanel.items():
            self.tx.write(key + ": " + str(item), (660, it))
            it += 20

    def caja(self, listCaja):
        """Dato de la caja."""
        if len(listCaja) > 0:
            for i, pos in enumerate(self.lco):
                self.writeCaja(pos, listCaja[i])

    def generate_coord(self):
        """Gen."""
        primer = (136, 30)
        dpuno = [(116, 200), (116, 220), (116, 240),
                 (116, 260), (116, 280), (116, 300)]
        pfi = 200
        listpos = []
        for i in range(4):
            if i == 0:
                pos = primer[:]
            else:
                pos = (listpos[i - 1][0][0] + 130, listpos[i - 1][0][1] - 5)
            r = [pos]
            for j in range(7):
                if i == 0:
                    try:
                        r.append(dpuno[j])
                    except Exception:
                        pass
                else:
                    d = (listpos[i - 1][0][0] + 130, pfi)
                    pfi += 20
                    r.append(d)
            pfi = 200
            listpos.append(r)
        return listpos

    def an_mov_Fin(self, listEndogena):
        """mover."""
        it = 10
        for i in range(len(listEndogena)):
            if i == 0:
                ta = "total Atendidos: " + str(listEndogena[i][0])
                self.tx.write(ta, (50, it))
                it += 30
                ta = "promedio de tiempo llegada : " + str(listEndogena[i][1])
                self.tx.write(ta, (50, it))
                it += 30
                ta = "promedio de tiempo cola : " + str(listEndogena[i][2])
                self.tx.write(ta, (50, it))
                it += 30
            if i == 1:
                ta = "promedio de tiempo ocio  : " + str(listEndogena[i][0])
                self.tx.write(ta, (450, it))
                it += 30
                ta = "promedio de tiempo salida : " + str(listEndogena[i][1])
                self.tx.write(ta, (450, it))
                it += 30
            it = 10

    def writeCaja(self, pos, pcaja):
        """mostrar_caja."""
        if pcaja["disponible"]:
            self.tx.write("disponible", pos[0], (255, 255, 0))
        else:
            nom, tiempo = pcaja["tipo"]
            tiempo = str("{0:.1f}".format(tiempo))
            self.tx.write(nom + ":" + tiempo, pos[0], self.tx.amarillo)
        num = pcaja["#_usuarios_usaron"]
        self.tx.write("atendidos: " + str(num), pos[1], (255, 255, 0))
        num = pcaja["t_ocio"]
        self.tx.write(" ocio: " + str(num), pos[2], (255, 255, 0))
        num = pcaja["t_s_total"]
        num = str("{0:.1f}".format(num))
        self.tx.write(" atendido: " + str(num), pos[3], (255, 255, 0))
        num = pcaja["deposito"]
        self.tx.write(" deposito: " + str(num), pos[4], (255, 255, 0))
        num = pcaja["retiro"]
        self.tx.write(" retiro: " + str(num), pos[5], (255, 255, 0))
        num = pcaja["pago"]
        self.tx.write(" pago: " + str(num), pos[6], (255, 255, 0))
