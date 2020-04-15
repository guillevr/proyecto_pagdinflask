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




app.run(debug=True)
