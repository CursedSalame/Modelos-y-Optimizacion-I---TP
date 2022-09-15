from random import random, seed, shuffle
from sys import argv
from math import inf

PATH_LECTURA = "modelosTP2.txt"
PATH_ESCRITURA = "modelosTP2_Result.txt"
PATH_MEJOR_LAVADO = "metadata_mejorlavadoTP2.txt"
INCOMPATIBILIDAD = "e"
TIEMPO_LAVADO = "n"

def leer_archivo(incompatibilidades, tiempos_de_lavado):
	with open(PATH_LECTURA) as f:
		for linea in f:
			parseada = linea.split()
			if parseada[0] == INCOMPATIBILIDAD:
				parseada[1], parseada[2] = int(parseada[1]), int(parseada[2])
				if parseada[1] not in incompatibilidades:
					incompatibilidades[parseada[1]] = set()
				incompatibilidades[parseada[1]].add(parseada[2])
				if parseada[2] not in incompatibilidades:
					incompatibilidades[parseada[2]] = set()
				incompatibilidades[parseada[2]].add(parseada[1])
			elif parseada[0] == TIEMPO_LAVADO:
				parseada[1], parseada[2] = int(parseada[1]), int(parseada[2])
				if parseada[1] not in incompatibilidades:
					incompatibilidades[parseada[1]] = set()
				tiempos_de_lavado[parseada[1]] = parseada[2]

def leer_archivo_de_lavado():
	try:
		with open(PATH_MEJOR_LAVADO) as f:
			res = int(f.readline().split(":")[1])
		return res
	except IOError:
		return inf

def actualizar_lavado(minimo_valor, semilla, cuanto_ejecutar):
	print()
	print(f"Nuevo minimo encontrado! => {minimo_valor}")
	print(f"Con la semilla: {semilla}")
	print(f"El la ejecucion n° {cuanto_ejecutar}")
	print()
	with open(PATH_MEJOR_LAVADO, "w") as f:
		f.write(f"El minimo de tiempo de lavado es: {minimo_valor}\n")
		f.write(f"Logrado con la semilla: {semilla}\n")


def agregar_prenda_a_lavado(incompatibilidades, prenda, lavado):
	for prenda_lavandose in lavado:
		if prenda[0] in incompatibilidades[prenda_lavandose[0]]:
			return False
	lavado.append(prenda)
	return True

def obtener_lavados(incompatibilidades, prendas_ordenadas):
	lavados = []
	for prenda in prendas_ordenadas:
		agregar_nuevo_lavado = True
		for lavado in lavados:
			if agregar_prenda_a_lavado(incompatibilidades, prenda, lavado):
				agregar_nuevo_lavado = False
				break
		if agregar_nuevo_lavado:
			lavados.append([prenda])
	return lavados

def guardar_lavados(lavados):
	resultado_final = {}
	for nro_lavado in range(len(lavados)):
		for prenda_lavada in lavados[nro_lavado]:
			resultado_final[prenda_lavada[0]] = nro_lavado
	orden_final = sorted(resultado_final)
	with open(PATH_ESCRITURA, "w") as f:
		for prenda in orden_final:
			f.write(f"{prenda} {resultado_final[prenda] + 1}\n")

def obtener_tiempo_total(lavados):
	return sum(max(lavado, key = lambda prenda : prenda[1])[1] for lavado in lavados)

def obtener_prendas_ordenadas(tiempos_de_lavado):
	prendas_orden_inicial = sorted(list(tiempos_de_lavado.items()), key = lambda x: x[1])
	prendas_por_mezclar = []
	prendas_orden_final = []
	while(len(prendas_orden_inicial) > 0):
		prenda_actual = prendas_orden_inicial.pop(-1)
		prendas_por_mezclar.append(prenda_actual)
		tiempo_actual = prenda_actual[1]
		while(len(prendas_orden_inicial) > 0 and prendas_orden_inicial[-1][1] == tiempo_actual):
			prendas_por_mezclar.append(prendas_orden_inicial.pop(-1))
		shuffle(prendas_por_mezclar)
		prendas_orden_final.extend(prendas_por_mezclar)
		prendas_por_mezclar.clear()
	return prendas_orden_final

def parse_argv():
	if len(argv) == 2:
		if "." in argv[1]:
			return argv[1], 1
		elif argv[1].isdigit():
			return random(), int(argv[1])
	return random(), 1

def main():
	semilla, cuanto_ejecutar = parse_argv()
	seed(float(semilla))

	incompatibilidades = {}
	tiempos_de_lavado = {}
	try:
		leer_archivo(incompatibilidades, tiempos_de_lavado)
	except IOError:
		print("No se encontró el archivo")
		return

	mejor_tiempo_lavado = leer_archivo_de_lavado()

	for i in range(cuanto_ejecutar):
		if cuanto_ejecutar > 4 and i % (cuanto_ejecutar // 4) == 0:
			print(f" - Ejecucion n° {i}, {25 * i // (cuanto_ejecutar // 4)}%")
		prendas_ordenadas = obtener_prendas_ordenadas(tiempos_de_lavado)
		lavados = obtener_lavados(incompatibilidades, prendas_ordenadas)
		tiempo_lavado_actual = obtener_tiempo_total(lavados)
		if tiempo_lavado_actual < mejor_tiempo_lavado:
			guardar_lavados(lavados)
			actualizar_lavado(tiempo_lavado_actual, semilla, i + 1)
			mejor_tiempo_lavado = tiempo_lavado_actual
		if cuanto_ejecutar == 1:
			print(f"El mejor tiempo fue {tiempo_lavado_actual}; con la semilla: {semilla}")
		semilla = random()
		seed(semilla)
	print(" - Ejecucion finalizada!")

main()