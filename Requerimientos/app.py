import os
from flask import Flask, render_template, redirect, request, url_for, flash
from R1_Procesar_Datos import limpiar_referencias
from R2_Extraer_Datos import ExtraerDatos
from R2_Graficar_Datos import DataVisualizer
from R3_Extraer_Abstracts import extraer_y_guardar_abstracts
from R4_Generar_Nube_Palabras import generar_nube_palabras_base64
from R5_Generar_Nodos_Journals import generar_grafo_base64

visualizer = DataVisualizer()

# Cambié el nombre de 'app' a 'application' para que Vercel lo reconozca
application = Flask(__name__)
application.secret_key = 'your_secret_key'
UPLOAD_FOLDER = 'procesador_referencias/Archivos'
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ruta principal (sin la lógica de limpieza de referencias)
@application.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


# Rutas para procesar los archivos y demás funcionalidades
@application.route('/procesar', methods=['POST'])
def procesar_archivos_route():
    if request.method == 'POST':
        try:
            limpiar_referencias()
            flash("El procesamiento R1 se completó correctamente.")
        except Exception as e:
            flash(f"Hubo un error al procesar los datos: {str(e)}")

        return render_template('R1limpieza_referencias.html')    

@application.route('/extraer', methods=['POST'])
def extraer_datos_route():
    if request.method == 'POST':
        try:
            ExtraerDatos()
            flash("Los datos fueron extraídos exitosamente.")
        except Exception as e:
            flash(f"Hubo un error al extraer los datos: {str(e)}")

        return render_template('R2datos_extraidos.html')   

@application.route('/graficar', methods=['GET', 'POST'])
def graficar_route():
    if request.method == 'POST':
        selected_field = request.form.get('selected_field')
        if selected_field:
            plot_url = visualizer.graficar(selected_field)
            if plot_url:
                return render_template('R2graficar.html', plot_url=plot_url, field=selected_field)
            else:
                flash("No se encontró el campo seleccionado en los datos.")
        else:
            flash("Por favor selecciona un campo para graficar.")
    return render_template('R2graficar.html', plot_url=None)

@application.route('/mostrar_nube', methods=['GET'])
def mostrar_nube_palabras_route():
    image_base64 = generar_nube_palabras_base64()
    return render_template('R4nube_palabras.html', image_base64=image_base64)

@application.route('/mostrar_grafo', methods=['GET'])
def mostrar_grafo_route():
    graph_base64 = generar_grafo_base64()
    return render_template('R5grafo.html', graph_base64=graph_base64)

# Cambié 'app.run()' a no hacer nada porque Vercel se encarga de eso.
# 'application' debe ser exportado para que Vercel lo pueda utilizar.
