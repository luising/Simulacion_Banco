"""Simulacion de Banco."""
import random

fw = open('procedimiento.txt', 'w')
fw1 = open('estadoActual.txt', 'w')
fw2 = open('resultadosFinales.txt', 'w')


# Declaracion de variables
usuarios = []
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
caja = []
cajainicial = {
	'disponible': True,
	'#_usuarios_usaron': 0,
	'ts_actual': 0,
	'ts_actual_mas_reloj': 0,
	't_s_total': 0,
	't_ocio': 0
}


def generar_tll():
	"""Generar tll."""
	tll = random.lognormvariate(3.05653, 1.5459)
	while tll > 219 or tll < 9:
		tll = random.lognormvariate(3.05653, 1.5459)
	return tll


for _ in range(Ncajas):
	caja.append(cajainicial)

# Funcion que genera el TLL en base a la distribucion lognormal

# Funcion que genera el TS en base a la distribucion lognormal
def generar_ts():
	ts = random.lognormvariate(2.84104, 1.04311)
	while ts > 120 or ts < 36:
		ts = random.lognormvariate(2.84104, 1.04311)
	return ts

# Avisa cuando sera el tiempo de salida
def aviso_ts(ts):
	return 'El tiempo de llegada del siguiente usuario es: ' +str(ts)


# Empieza la simulacion
for i in range(0, tiempo_maximo):
	reloj = i
	#si no existe tiempo de llegada, lo crea
	if tll == 0:
		tll = generar_tll()
		tll_entero = round(tll)
		tll_mas_reloj = tll_entero + reloj


	#Si el tiempo de llegada + reloj es igual al reloj, 'llega' el usuario
	#y genera otro tiempo de llegada
	if tll_mas_reloj == reloj:
		cola.append(1)

		usuarios.append({
				'tll' : tll,
				'tll_mas_reloj' : tll_mas_reloj,
				'ts_actual': 0,
				'ts_actual_mas_reloj': 0,
				'tiempo_de_cola': 0,
				'tiempo_en_cola': reloj,
				'en_cola' : True,
				'activo' : True
			})
		tll = generar_tll()
		tll_entero = round(tll)
		tll_mas_reloj = tll_entero + reloj
		
		fw.write ('\n')
		fw.write ('-------------------Llega un usuario a la cola------------------------ \n')
		fw.write ('El usuario llego al segundo: ' + str(reloj) +'\n')
		fw.write ('La cola actual es de :' +str(len(cola)) +'\n')
		fw.write (aviso_tll(tll) +'\n')
		fw.write ('--------------------------------------------------------------------- \n')

	#Si la cola es diferente a 0, trata de pasar a los usuarios a una caja
	if len(cola) != 0:
		for k in range(0,4):
			#Checa si la caja i esta disponible
			if caja[k]['disponible']:
				fw.write ('\n')
				fw.write ('-------------------Sale un usuario de la cola------------------------\n')
				caja[k]['disponible'] = False
				caja[k]['ts_actual'] = generar_ts()
				caja[k]['ts_actual_mas_reloj'] = round(caja[k]['ts_actual']) + reloj
				caja[k]['#_usuarios_usaron'] += 1
				caja[k]['t_s_total'] += caja[k]['ts_actual']
				usuarios[0]['ts_actual'] = caja[k]['ts_actual']
				usuarios[0]['ts_actual_mas_reloj'] = caja[k]['ts_actual_mas_reloj']
				usuarios[0]['tiempo_en_cola'] = reloj - usuarios[0]['tiempo_en_cola']
				usuarios[0]['tiempo_de_cola'] = usuarios[0]['tiempo_en_cola']
				fw.write ('El usuario sale de la cola al segundo: '+str(reloj) +'\n')
				fw.write ('Sale de la cola el usuario que llego al segundo '+str(usuarios[0]['tll_mas_reloj'])+ ' y pasa a la caja['+str(k)+']\n')
				fw.write ('El usuario paso: '+str(usuarios[0]['tiempo_en_cola'])+' segundos en la cola \n')
				usuarios_no_en_cola.append(usuarios[0])
				usuarios.pop(0)
				cola.pop(0)
				fw.write ('--------------------------------------------------------------------- \n')
				break

	for j in range (0,4):
		if caja[j]['ts_actual_mas_reloj'] == reloj:
			caja[j]['disponible'] = True
			for h in range (0,len(usuarios_no_en_cola)):
				if usuarios_no_en_cola[h]['activo'] and usuarios_no_en_cola[h]['ts_actual_mas_reloj'] == reloj:
					usuarios_no_en_cola[h]['activo'] = False
					fw.write ('\n')
					fw.write ('--------- Termina el servicio de un usuario------------------------ \n')
					fw.write ('El usuario sale del servicio al segundo: '+str(usuarios_no_en_cola[h]['ts_actual_mas_reloj']) +'\n')
					fw.write ('La caja['+str(j)+'] se libera, el usuario tardo en salir: '+str(usuarios_no_en_cola[h]['ts_actual'])+' segundos. \n')
					fw.write ('--------------------------------------------------------------------- \n')
					break

	#Probabilidad que salga de la cola el usuario, en caso que tenga prisa
	if len(cola) != 0:
		salida_random = random.uniform(0, 100.00)
		if salida_random >= 0 and salida_random <= 8.33:
			fw.write ('\n')
			fw.write ('-------- Un usuario saldra de la cola, se tiene que ir ------ \n')
			fw.write ('Numero de usuarios en la cola: '+str(len(cola)) +'\n')
			usuarios_que_salieron_de_la_cola += 1
			usuarios[-1]['activo'] = False
			usuarios[-1]['tiempo_en_cola'] = reloj - usuarios[-1]['tiempo_en_cola']
			t_cola_salio = usuarios[-1]['tiempo_en_cola']
			fw.write ('Paso un total de : ' +str(t_cola_salio)+ ' segundos en la cola. \n')
			usuarios_no_en_cola.append(usuarios[-1])
			usuarios.pop()
			cola.pop()
			fw.write ('Sale de la cola \n')
			fw.write ('Numero de usuarios en la cola (despues de salir): '+str(len(cola)) +'\n')
			fw.write ('--------------------------------------------------------------------- \n')

	#Impresiones de estado
	fw1.write ('////////////// FINAL DEL CICLO ACTUAL ///////////////////// \n')
	fw1.write ('Ciclo actual: '+str(reloj) +'\n')
	fw1.write ('\n')
	fw1.write ('Tamanio de cola: '+str(len(cola)) +'\n')

	#Checa si las cajas no hacen nada, en caso que si, aumenta su ocio
	fw1.write ('\n')
	fw1.write ('Cajas disponibles: \n')
	for g in range (0,4):
		if caja[g]['disponible']:
			caja[g]['t_ocio'] += 1
			#Impresiones de estado
			fw1.write ('Caja['+str(g)+'] disponible \n')

	fw1.write ('\n')
	fw1.write ('Cajas no disponibles (estan siendo usadas) \n')
	for f in range (0,4):
		if caja[f]['disponible'] == False:
			fw1.write ('Caja['+str(f)+'] no disponible \n')
	fw1.write ('////////////// /////////////////// ///////////////////// \n')

fw2.write ('')
fw2.write ('')
fw2.write ('Resultados finales de la simulacion \n')
fw2.write ('\n')
total_usuarios_no_en_cola = len(usuarios_no_en_cola)
fw2.write ('El total de usuarios que pasaron por la cola fue de: '+str(total_usuarios_no_en_cola) +'\n')
for i in range(0,total_usuarios_no_en_cola):
	tiempo_llegada_promedio += usuarios_no_en_cola[i]['tll']
	tiempo_cola_promedio += usuarios_no_en_cola[i]['tiempo_en_cola']

tiempo_llegada_promedio = tiempo_llegada_promedio / total_usuarios_no_en_cola
tiempo_cola_promedio = tiempo_cola_promedio / total_usuarios_no_en_cola

fw2.write ('EL tiempo de llegada promedio de los usuarios fue de: '+str(tiempo_llegada_promedio) +'\n')
fw2.write ('EL tiempo de cola promedio de los usuarios fue de: '+str(tiempo_cola_promedio) +'\n')


for i in range(0,4):
	fw2.write ('\n')
	fw2.write ('Caja['+str(i)+']\n')
	promedio_caja = caja[i]['t_s_total'] / caja[i]['#_usuarios_usaron']
	usuarios_totales_caja = caja[i]['#_usuarios_usaron']
	tiempo_ocio_promedio += caja[i]['t_ocio']
	t_s_promedio_total += promedio_caja
	fw2.write ('La caja['+str(i)+'] fue usada por un total de:'+str(usuarios_totales_caja)+' personas \n')
	fw2.write ('Tiempo de ocio de la caja['+str(i)+'] fue de: '+str(caja[i]['t_ocio'])+' segundos \n')
	fw2.write ('El tiempo de salida de la caja['+str(i)+'] fue de: '+str(caja[i]['t_s_total'])+' segundos \n')
	fw2.write ('Promedio de tiempos de salida de la caja['+str(i)+'] fue de: '+str(promedio_caja)+' segundos \n')

tiempo_ocio_promedio = tiempo_ocio_promedio / 4
fw2.write ('\n')
fw2.write ('El tiempo de ocio promedio en las cajas fue de: '+str(tiempo_ocio_promedio)+' segundos \n')

t_s_promedio_total = t_s_promedio_total / 4
fw2.write ('\n')
fw2.write ('El promedio de tiempos de salida de todas las cajas fue de: '+str(t_s_promedio_total)+' segundos \n')
fw2.write ('\n')
fw2.write ('Un total de: '+str(usuarios_que_salieron_de_la_cola)+' usuarios salieron de la cola \n')

fw.close()
fw1.close()
fw2.close()
print("terminado")
