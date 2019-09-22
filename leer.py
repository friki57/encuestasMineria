def buscar_archivos(ruta):
	archivos_texto = []
	archivos       = os.listdir(ruta)
	for archivo in archivos:
		if archivo[-4:] == '.txt':
			archivos_texto.append(archivo)
	return archivos_texto
def categorizar(enc,pregunta):
	ret = "";
	antes = ret;
	for f in familia:
		if(ret==antes):
			if(f in enc[pregunta].lower()):
				ret += "familia "

	antes = ret;
	for f in arte:
		if(ret==antes):
			if(f in enc[pregunta].lower()):
				ret += "arte "

	antes = ret;
	for f in ocio:
		if(ret==antes):
			if(f in enc[pregunta].lower()):
				ret += "ocio "

	antes = ret;
	for f in social:
		if(ret==antes):
			if(f in enc[pregunta].lower()):
				ret += "social "

	antes = ret;
	for f in estudios:
		if(ret==antes):
			if(f in enc[pregunta].lower()):
				ret += "estudios "

	antes = ret;
	for f in deporteyejercicio:
		if(ret==antes):
			if(f in enc[pregunta].lower()):
				ret += "deporte_y_ejercicio "

	antes = ret;
	for f in animales:
		if(ret==antes):
			if(f in enc[pregunta].lower()):
				ret += "animales "

	antes = ret;
	for f in nosabenoresponde :
		if(ret==antes):
			if(f in enc[pregunta].lower()):
				ret += "no_sabe_no_responde "
	antes = ret;
	for f in naturaleza:
		if(ret==antes):
			if(f in enc[pregunta].lower()):
				ret += "naturaleza "
	antes = ret;
	for f in salud :
		if(ret==antes):
			if(f in enc[pregunta].lower()):
				ret += "salud "
	antes = ret;
	for f in trabajo :
		if(ret==antes):
			if(f in enc[pregunta].lower()):
				ret += "trabajo "

	# if ret=='':
	# 	print(enc)
	if(enc['opt']==True):
		ret+='Optimista'
	else:
		ret+='Pesimista'
	return ret;

def checkear(enc):
	import json
	enc = json.loads(enc)
	print('feliz')
	feliz = categorizar(enc,'feliz');
	print('triste')
	triste = categorizar(enc,'triste');
	print('preocupado')
	preocupado = categorizar(enc,'preocupado');

	tabla = {
	"feliz": feliz.split(' ')
	,
	"triste": triste.split(' '),
	"preocupado": preocupado.split(' ')
	}
	if tabla not in resultados:
		resultados.append(tabla);


def generarExcel(tabla,titulo):
	import xlsxwriter
	libro = xlsxwriter.Workbook(titulo+'.xlsx');
	hoja = libro.add_worksheet();
	fila = 0;
	columna = 0;
	hoja.write(fila,columna,titulo);
	fila += 1;
	cat = ['familia',	'arte',	'ocio',	'social',	'estudios',	'deporte_y_ejercicio',	'animales',	'naturaleza',	'salud',	'trabajo',	'no_sabe_no_responde']
	for c in cat:
		hoja.write(fila,columna,c)
		columna += 1
	hoja.write(fila,columna,'Estado')
	columna = 0;
	fila = 2;
	for c in cat:
		for t in tabla:
			if c in t[titulo]:
				hoja.write(fila,columna,'si')
			else:
				hoja.write(fila,columna,'no')
			hoja.write(fila,len(cat),t[titulo][-1])
			fila += 1
		columna += 1
		fila = 2
	libro.close();

import os;
textos = buscar_archivos("txts");
palabras = [];
resultados = [];


familia = ['papas','padres','madre', 'padre','hermanita','familia', 'familias','papá','mamá','herman','primo','prima','abuel','casa']
arte = ['musica','música','museo','bailar','baile','cantar','canto','canciones','guitarra','piano']
ocio = ['comer','dormir','videojuegos','television','televisión','tv','internet','películas','peliculas','celular','auto','free fire','fumar','viaje','viajar','computador','leer']
social = ['amigo','amiga','compañeros','fiesta','amigos','solo','sola','ayudar','personas','cañar','indiferen','discut','discusión','mentir','soledad','novi']
estudios = ['notas','universidad','colegio','clase','materia','exámenes','examen','exámen','carrera','estud','bachiller','tarea','exponer','profesion','profecion','profesión','instituto','hito','laboratorio','cole']
deporteyejercicio = ['deporte','ejercicio','fútbol','futbol','gym','gimnasio','voleibol','basket','basquet','camina','crossfit']
animales = ['animal','perr','gato','gata','toro']
nosabenoresponde = ['nada','ningun','ningún']
naturaleza = ['planta','viento','chiquitania','ambiente','planeta','amanecer','anochecer','atardecer','contamin','chaqueo','estrella']
salud = ['enfermedad','salud','cáncer','enfermar','hospital']
trabajo = ['lavar','trabaj','laburar','empleo','dinero','económic','econom','pobre','sueldo','deudas']


for text in textos:
	txt = open("txts/"+text,"r");
	enc = txt.read();
	checkear(enc);
	txt.close();
for r in resultados:
	if len(r['feliz'])>1:
		print(r['feliz']);
	if len(r['triste'])>1:
		print(r['triste']);
	if len(r['preocupado'])>1:
		print(r['preocupado']);

generarExcel(resultados,'feliz')
generarExcel(resultados,'triste')
generarExcel(resultados,'preocupado')
