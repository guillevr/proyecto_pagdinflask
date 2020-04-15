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


app.run(debug=True)
