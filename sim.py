"""Simulacion Banco Banorte."""
from caja import Caja
from usuario import Usuario
import generadorVariables as gv
from savetxt import svtxt

# Declaracion de variables
listUsuario = []
usuarios_no_en_cola = []
cola = []
tiempo_maximo = 1500
tll = 0
usuarios_que_salieron_de_la_cola = 0
tiempo_llegada_promedio = 0
tiempo_cola_promedio = 0
tiempo_ocio_promedio = 0
t_s_promedio_total = 0
Ncajas = 4
listcaja = []
for _ in range(Ncajas):
    listcaja.append(Caja())
# inicialisar archivos
st = svtxt()
# crear tiempo de llegada
tll = gv.generate_tll()
tll_entero = round(tll)
tiempo_llegada = tll_entero + 0
st.wGeneraTll(tll)
# -------------inicio de la simulacion ----------
for i in range(tiempo_maximo):
    reloj = i
    if tiempo_llegada == reloj:
        cola.append(1)
        listUsuario.append(Usuario)
        st.wllegaUsuario(tll, reloj, cola)
        tll = gv.generate_tll()
        tll_entero = round(tll)
        tiempo_llegada = tll_entero + reloj
        print(tiempo_llegada)


print(listcaja[0].atributos["disponible"])
