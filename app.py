from flask import Flask, render_template, redirect, request, url_for
import data as d
from data_fechas import leer_fechas

app = Flask(__name__,template_folder='views/templates')

@app.route('/')
def inicio():
    data = d.leer_datos()
    return render_template('index.html', data = data, bandera = True)

@app.route('/agregar-nota', methods=['GET', 'POST'])
def agregar_nota():
    if request.method == 'POST':
        ingles = request.form['ingles']
        espanol = request.form['espanol']
        d.agregar_nota(ingles, espanol)
        return redirect(url_for('inicio'))
    return render_template('agregar_nota.html')

@app.route('/nota-aleatoria', methods=['GET', 'POST'])
def nota_aleatoria():
    data = d.obtener_nota_aleatoria()
    if data:
        notas = [d.obtener_nota_aleatoria() for _ in range(5)] #generando 5 notas
        if request.method == 'POST':
            puntaje = 0
            respuestas = request.form.getlist('respuesta')
            correctas = request.form.getlist('correcta') #obteniendo las respuestas correctas que el usuario no ve
            print(respuestas,'\n',correctas)
            for i in range(len(correctas)):
                if respuestas[i] == correctas[i]: #comparando por indice
                    puntaje += 1
            return render_template('puntaje.html', puntaje = puntaje)
        else:

            return render_template('nota_aleatoria.html', aleatorio = notas)
    return render_template('nota_aleatoria.html', mensaje = "")

@app.route('/eliminar-nota/<string:id>', methods=['GET', 'POST'])
def eliminar_nota(id):
    d.eliminar_nota_id(id)
    return redirect(url_for('inicio'))

@app.route('/editar-nota/<string:id>', methods=['GET', 'POST'])
def editar_nota(id):
    nota = d.buscar_nota_por_id(id)
    if request.method == 'POST':
        nota_actualizada = {
            "id": id,
            "ingles": request.form['ingles'],
            "espanol": request.form['espanol'],
            "fecha": nota['fecha']
        }
        d.actualizar_nota(nota_actualizada)
        return redirect(url_for('inicio'))
    return render_template('editar_nota.html', nota = nota)

@app.route('/nota-por-fecha')
def nota_por_fecha():
    data_fechas = leer_fechas()
    return render_template('nota_por_fecha.html', data_fechas = data_fechas)

if __name__ == '__main__':
    app.run(debug=True)