from flask import Flask, render_template,abort,request
app = Flask(__name__)

from lxml import etree
doc = etree.parse('libros.xml')


## Muestra la pagina de inicio.
@app.route('/',methods=["GET","POST"])
def inicio():
	nombre = "Guillermo Vizcaino"
	return render_template("inicio.html",nombre=nombre)

## Redireccion a la pagina donde se muestran los ejemplos de los calculos de potencias.
@app.route('/pag_ej_potencias')
def pag_ej_potencias():
	return render_template("pag_ej_potencias.html")

## Redireccion a la pagina donde se muestran los ejemplos de calcular las letras de una palabra.
@app.route('/pag_ej_calcletras')
def pag_ej_calcletras():
	return render_template("pag_ej_calcletras.html")

## Calcula la potencia escrita en la (URL).
@app.route('/potencia/<int:base>/<exponente>')
def calculo_potencias(base,exponente):

	exponente=int(exponente)

	if exponente < 0:
		resultado= 1 / base ** abs(exponente)
		return render_template("pag_calc_potencia.html",bas=base,expo=abs(exponente),res=resultado)

	elif exponente == 0:
		return render_template("pag_calc_potencia.html",bas=base,expo=exponente,res=1)

	elif exponente > 1:
		resultado=base**exponente
		return render_template("pag_calc_potencia.html",bas=base,expo=exponente,res=resultado)

	else:
		abort(404)

## Calcula la potencia del numero indicado en la pagina de los ejemplos de las potencias.
@app.route('/potencia/<base>')
def calculo_ejemplo_potencias(base):

	try:
		lista=[]
		base=int(base)

		for i in range (0,21):
			dic={"exponente":i,"resultado":base**i}
			lista.append(dic)

	except:
		abort(404)

	return render_template("pag_ej_potencias.html",lista=lista,base=base)

## Calcula cuantas letras hay en una palabra (URL).
@app.route('/cuenta/<palabra>/<caracter>')
def cuenta_letras(palabra,caracter):

	if len(caracter) == 0:
		abort(404)

	else:
		num_car=palabra.count(caracter)
		return render_template("pag_calc_nletras.html",palabra=palabra,caracter=caracter,ncaracteres=num_car)

## Calculador de multiples cosas para las palabras (boton).
@app.route('/cuentamultiple',methods=["POST"])
def calc_mul_pal():
	palabra=request.form.get("palabra")

	## ABECEDARIO
	abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
	## Para las vocales
	vocales=[]
	l_vocales=""
	## Para las consonantes
	consonantes=[]
	l_consonantes=""
	## Para los numeros
	numeros=[]
	l_numeros=""
	## Para los caracteres especiales
	car_especial=[]
	l_carespecial=""

	# covon -> consonante o vocal o numero
	for covon in palabra:
		if covon.lower() not in abecedario:
			try:
				if int(covon) == 1 or int(covon) == 2 or int(covon) == 3 or int(covon) == 4 or int(covon) == 5 or int(covon) == 6 or int(covon) == 7 or int(covon) == 8 or int(covon) == 9 or int(covon) == 0:
					if int(covon) not in numeros:
						numeros.append(int(covon))
			except ValueError:
				if covon not in car_especial:
					car_especial.append(covon)
		else:
			if covon.lower() == "a" or covon.lower() == "e" or covon.lower() == "i" or covon.lower() == "o" or covon.lower() == "u":
				if covon.lower() not in vocales:
					vocales.append(covon)
			else:
				if covon.lower() not in consonantes:
					consonantes.append(covon)


	for v in sorted(vocales):
		l_vocales=l_vocales+v+", "

	l_vocales=l_vocales[:len(l_vocales)-2]

	for c in sorted(consonantes):
		l_consonantes=l_consonantes+c+", "

	l_consonantes=l_consonantes[:len(l_consonantes)-2]

	for n in sorted(numeros):
		l_numeros=l_numeros+str(n)+", "

	l_numeros=l_numeros[:len(l_numeros)-2]

	for ce in car_especial:
		l_carespecial=l_carespecial+ce+", "

	l_carespecial=l_carespecial[:len(l_carespecial)-2]



	## long_pal (longitud de la palabra), nvoc (numero de vocales), lvoc (letras vocales),
	## ncon (numero de consonantes), lcon (letras consonantes ordenadas).


	if len(vocales) == 0:
		if len(consonantes) == 0:
			if len(numeros) == 0 and len(car_especial)!=0:
				## nce -> numero de caracteres especiales //  lce -> lista caracteres especiales
				return render_template("pag_ej_calcletras.html",palabra=palabra,long_pal=len(palabra),nce=len(car_especial),lce=l_carespecial)
			elif len(car_especial) == 0 and len(numeros) != 0:
				## nn -> numero de numeros //  lnum -> lista de numeros
				return render_template("pag_ej_calcletras.html",palabra=palabra,long_pal=len(palabra),nn=len(numeros),lnum=l_numeros)
			else:
				return render_template("pag_ej_calcletras.html",palabra=palabra,long_pal=len(palabra),nce=len(car_especial),lce=l_carespecial,nn=len(numeros),lnum=l_numeros)
		else:
			if len(numeros) == 0 and len(car_especial)!=0:
					## nce -> numero de caracteres especiales //  lce -> lista caracteres especiales // ncon -> numero de consonantes // lcon -> lista de consonantes
					return render_template("pag_ej_calcletras.html",palabra=palabra,long_pal=len(palabra),ncon=len(consonantes),lcon=l_consonantes,nce=len(car_especial),lce=l_carespecial)
			elif len(car_especial) == 0 and len(numeros) != 0:
				## nn -> numero de numeros //  lnum -> lista de numeros
				return render_template("pag_ej_calcletras.html",palabra=palabra,long_pal=len(palabra),ncon=len(consonantes),lcon=l_consonantes,nn=len(numeros),lnum=l_numeros)
			elif len(car_especial) != 0 and len(numeros) != 0:
				return render_template("pag_ej_calcletras.html",palabra=palabra,long_pal=len(palabra),ncon=len(consonantes),lcon=l_consonantes,nce=len(car_especial),lce=l_carespecial,nn=len(numeros),lnum=l_numeros)
			else:
				return render_template("pag_ej_calcletras.html",palabra=palabra,long_pal=len(palabra),ncon=len(consonantes),lcon=l_consonantes)

	elif len(consonantes) == 0:
		if len(vocales) == 0:
			if len(numeros) == 0 and len(car_especial)!=0:
				## nce -> numero de caracteres especiales //  lce -> lista caracteres especiales
				return render_template("pag_ej_calcletras.html",palabra=palabra,long_pal=len(palabra),nce=len(car_especial),lce=l_carespecial)
			elif len(car_especial) == 0 and len(numeros) != 0:
				## nn -> numero de numeros //  lnum -> lista de numeros
				return render_template("pag_ej_calcletras.html",palabra=palabra,long_pal=len(palabra),nn=len(numeros),lnum=l_numeros)
			else:
				return render_template("pag_ej_calcletras.html",palabra=palabra,long_pal=len(palabra),nce=len(car_especial),lce=l_carespecial,nn=len(numeros),lnum=l_numeros)
		else:
			if len(numeros) == 0 and len(car_especial)!=0:
					## nce -> numero de caracteres especiales //  lce -> lista caracteres especiales nvoc -> numero de vocales // lvoc -> lista de vocales
					return render_template("pag_ej_calcletras.html",palabra=palabra,long_pal=len(palabra),nvoc=len(vocales),lvoc=l_vocales,nce=len(car_especial),lce=l_carespecial)
			elif len(car_especial) == 0 and len(numeros) != 0:
				## nn -> numero de numeros //  lnum -> lista de numeros
				return render_template("pag_ej_calcletras.html",palabra=palabra,long_pal=len(palabra),nvoc=len(vocales),lvoc=l_vocales,nn=len(numeros),lnum=l_numeros)
			elif len(car_especial) != 0 and len(numeros) != 0:
				return render_template("pag_ej_calcletras.html",palabra=palabra,long_pal=len(palabra),nvoc=len(vocales),lvoc=l_vocales,nce=len(car_especial),lce=l_carespecial,nn=len(numeros),lnum=l_numeros)
			else:
				return render_template("pag_ej_calcletras.html",palabra=palabra,long_pal=len(palabra),nvoc=len(vocales),lvoc=l_vocales)
				
	else:
		if len(numeros) == 0 and len(car_especial)!=0:
			## nce -> numero de caracteres especiales //  lce -> lista caracteres especiales nvoc -> numero de vocales // lvoc -> lista de vocales
			return render_template("pag_ej_calcletras.html",palabra=palabra,long_pal=len(palabra),nvoc=len(vocales),lvoc=l_vocales,ncon=len(consonantes),lcon=l_consonantes,nce=len(car_especial),lce=l_carespecial)
		elif len(car_especial) == 0 and len(numeros) != 0:
			## nn -> numero de numeros //  lnum -> lista de numeros
			return render_template("pag_ej_calcletras.html",palabra=palabra,long_pal=len(palabra),nvoc=len(vocales),lvoc=l_vocales,ncon=len(consonantes),lcon=l_consonantes,nn=len(numeros),lnum=l_numeros)
		else:
			return render_template("pag_ej_calcletras.html",palabra=palabra,long_pal=len(palabra),nvoc=len(vocales),lvoc=l_vocales,ncon=len(consonantes),lcon=l_consonantes,nce=len(car_especial),lce=l_carespecial,nn=len(numeros),lnum=l_numeros)

#



app.run(debug=True)
