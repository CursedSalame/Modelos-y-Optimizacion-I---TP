PATH_LECTURA = "modelosTP2.txt"
PATH_ESCRITURA = "modelosTP2_Result.txt"
INCOMPATIBILIDAD = "e"
TIEMPO_LAVADO = "n"

def leer_archivo(incompatibilidades, tiempos_de_lavado):
	with open(PATH_LECTURA) as f:
		for linea in f:
			parseada = linea.split()
			if parseada[0] == INCOMPATIBILIDAD:
				if parseada[1] not in incompatibilidades:
					incompatibilidades[parseada[1]] = set()
				incompatibilidades[parseada[1]].add(parseada[2])
			elif parseada[0] == TIEMPO_LAVADO:
				if parseada[1] not in incompatibilidades:
					incompatibilidades[parseada[1]] = set()
				tiempos_de_lavado[parseada[1]] = parseada[2]

def agregar_prenda_a_lavado(incompatibilidades, prenda, lavado):
	for prenda_lavandose in lavado:
		if prenda in incompatibilidades[prenda_lavandose]:
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
			resultado_final[prenda_lavada] = nro_lavado
	orden_final = sorted(resultado_final, key = lambda x : int(x))
	with open(PATH_ESCRITURA, "w") as f:
		for prenda in orden_final:
			f.write(f"{prenda} {resultado_final[prenda] + 1}\n")


def main():
	incompatibilidades = {}
	tiempos_de_lavado = {}
	try:
		leer_archivo(incompatibilidades, tiempos_de_lavado)
	except IOError:
		print("No se encontró el archivo")
		return

	# Magia de Python para transformar el diccionario de tiempos de lavado en
	# una lista ordenada de prendas
	prendas_ordenadas = sorted(list(tiempos_de_lavado.items()), reverse = True, key = lambda x: int(x[1]))
	prendas_ordenadas = list(map(lambda x : x[0], prendas_ordenadas))
	
	lavados = obtener_lavados(incompatibilidades, prendas_ordenadas)
	guardar_lavados(lavados)


main()