"""Simulacion Banco Banorte."""
from objetos.usuario import Usuario
from objetos.tiempo import Time
from objetos.cola import Cola
import animacion.animacion as an
from tools.savetxt import svtxt


def comprobar_Cliente_LLegando():
    """Compobar si ya llego un cliente."""
    global num_Clientes
    if t.tiempo_llegada == t.reloj:
        c.cola += 1
        num_Clientes += 1
        c.listUsuario.append(Usuario(t.tll, t.tiempo_llegada, t.reloj))
        st.wllegaUsuario(t.tll, t.reloj, c.cola)
        anim.an_entrando_cola()
        t.update_TLL()


def comprobar_Cola():
    """Comprobar si hay un cliente en cola."""
    global num_Deposito, num_Retiro, num_Pago
    if c.cola > 0:
        for i, caja in enumerate(c.listcaja):
            # Comprobar si la caja i esta disponible
            if caja.atributos['disponible']:
                caja.setUsuario(t.reloj)
                op = caja.atributos["tipo"][0]
                if op == "deposito":
                    num_Deposito += 1
                elif op == "retiro":
                    num_Retiro += 1
                elif op == "pago":
                    num_Pago += 1
                c.listUsuario[0].solicitarPedido(
                                    caja.atributos['ts_actual'],
                                    caja.atributos['ts_actual_mas_reloj'],
                                    t.reloj)
                st.wSaleUsuarioCola(
                        t.reloj,
                        t.tiempo_llegada,
                        i,
                        c.listUsuario[0].atributos['tiempo_en_cola'])
                c.listcaja[i] = caja
                anim.an_cola_caja(i)
                c.update_cola()
                return


def atenderCliente():
    """Atendiendo cliente."""
    for i, caja in enumerate(c.listcaja):
        if caja.atributos['ts_actual_mas_reloj'] == t.reloj:
            caja.atributos['disponible'] = True
            for j, usuario in enumerate(c.listUsuarioAtentiendo):
                if (usuario.atributos['activo'] and
                        usuario.atributos['ts_actual_mas_reloj'] == t.reloj):
                    anim.an_salir_caja(i)
                    usuario.atributos['activo'] = False
                    st.wUsuarioAtendido(
                                usuario.atributos['ts_actual_mas_reloj'],
                                usuario.atributos['ts_actual'],
                                i)
                    c.listUsuarioAtentiendo[j] = usuario
                    c.listcaja[i] = caja
                    st.wFinCiclo(t.reloj, c.cola)
                    break


def actualizarTiempoOcio():
    """Actualizar ocio."""
    listOcio = []
    listOcupado = []
    for i, caja in enumerate(c.listcaja):
        if caja.atributos['disponible']:
            caja.atributos['t_ocio'] += 1
            c.listcaja[i] = caja
            listOcio.append(i)
        else:
            listOcupado.append(i)
        st.wCajaOcio(listOcio, listOcupado)


def obtenerPromedioUsuario():
    """Variable Endogenas."""
    total_Atendidos = len(c.listUsuarioAtentiendo)
    for i, usuario in enumerate(c.listUsuarioAtentiendo):
        t.tiempo_llegada_promedio += usuario.atributos['tll']
        t.tiempo_cola_promedio += usuario.atributos['tiempo_en_cola']
    t.tiempo_llegada_promedio = t.tiempo_llegada_promedio / total_Atendidos
    t.tiempo_cola_promedio = t.tiempo_cola_promedio / total_Atendidos
    listColumn[0] = [total_Atendidos,
                     "{0:.1f}".format(t.tiempo_llegada_promedio),
                     t.tiempo_cola_promedio]
    st.wTiempoPromedio(
                total_Atendidos,
                t.tiempo_llegada_promedio,
                t.tiempo_cola_promedio)


def obtenerPromedioCajas():
    """Variable Endogenas."""
    for i, caja in enumerate(c.listcaja):
        n_usuario = caja.atributos['#_usuarios_usaron']
        if n_usuario < 1:
            pC = 0
        else:
            pC = caja.atributos['t_s_total'] / n_usuario
        usuarios_totales_caja = caja.atributos['#_usuarios_usaron']
        t.tiempo_ocio_promedio += caja.atributos['t_ocio']
        t.t_s_promedio_total += pC
        st.WPromedioCaja(
                    i,
                    usuarios_totales_caja,
                    caja.atributos['t_ocio'],
                    caja.atributos['t_s_total'],
                    pC)


def obtenerPromedioOcio():
    """Obtener Promedio Ocio."""
    t.tiempo_ocio_promedio = t.tiempo_ocio_promedio / 4
    t.t_s_promedio_total = t.t_s_promedio_total / 4
    st.WPromedioOcio(
                t.tiempo_ocio_promedio,
                t.t_s_promedio_total)
    listColumn[1] = ["{0:.1f}".format(t.tiempo_ocio_promedio),
                     "{0:.1f}".format(t.t_s_promedio_total)]
    st.close()


def get_Estado():
    """Act gui."""
    pData = {
        "reloj": t.reloj,
        "# Clientes": num_Clientes,
        "# Depositos": num_Deposito,
        "# Retiros": num_Retiro,
        "# Pago": num_Pago,
        "nuevo cliente en": t.tiempo_llegada
    }
    listtemp = [x.atributos for x in c.listcaja]
    anim.pData = pData
    anim.pLi = listtemp


# inicializar cola
c = Cola(caja=4)
# inicializar tiempo
t = Time(max=60)
# inicializar archivos
st = svtxt()
# crear tiempo de llegada
st.wGeneraTll(t.tll)
# inicilaizar Animacion
anim = an.anim()

num_Clientes = 0
num_Deposito = 0
num_Retiro = 0
num_Pago = 0

listColumn = [[] for _ in range(2)]
# -------------inicio de la simulacion ----------
for i in range(1, t.tiempo_maximo):
    t.reloj = i
    get_Estado()
    comprobar_Cliente_LLegando()
    comprobar_Cola()
    atenderCliente()
    actualizarTiempoOcio()

obtenerPromedioUsuario()
obtenerPromedioCajas()
obtenerPromedioOcio()
anim.pantalla_fin(listColumn)
print("terminado")
