import os
from flask import Flask, render_template, redirect, request, url_for, flash
from R1_Procesar_Datos import limpiar_referencias
from R2_Extraer_Datos import ExtraerDatos
from R2_Graficar_Datos import DataVisualizer
from R3_Extraer_Abstracts import extraer_y_guardar_abstracts
#from R3_Contar_Sinonimos import ejecutar_proceso_completo
from R4_Generar_Nube_Palabras import generar_nube_palabras_base64
from R5_Generar_Nodos_Journals import generar_grafo_base64


visualizer = DataVisualizer()

app = Flask(__name__)
app.secret_key = 'your_secret_key'
UPLOAD_FOLDER = 'procesador_referencias/Archivos'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ruta principal (sin la lógica de limpieza de referencias)
@app.route('/', methods=['GET', 'POST'])
def index():
    # Solo renderiza la página principal
    return render_template('index.html')


# Ruta para procesar los archivos
@app.route('/procesar', methods=['POST'])
def procesar_archivos_route():
    if request.method == 'POST':
        try:
            # Ejecutar la función de limpieza de referencias
            limpiar_referencias()
            flash("El procesamiento R1 se completó correctamente.")
        except Exception as e:
            flash(f"Hubo un error al procesar los datos: {str(e)}")

        return render_template('R1limpieza_referencias.html')    


# Ruta para extraer los datos
@app.route('/extraer', methods=['POST'])
def extraer_datos_route():
    if request.method == 'POST':
        try:
            # Llamar a la función para extraer los datos
            ExtraerDatos()
            flash("Los datos fueron extraídos exitosamente.")
        except Exception as e:
            flash(f"Hubo un error al extraer los datos: {str(e)}")

        return render_template('R2datos_extraidos.html')   

@app.route('/graficar', methods=['GET', 'POST'])
def graficar_route():
    if request.method == 'POST':
        selected_field = request.form.get('selected_field')
        if selected_field:
            # Llamar al método graficar del visualizador
            plot_url = visualizer.graficar(selected_field)
            if plot_url:
                return render_template('R2graficar.html', plot_url=plot_url, field=selected_field)
            else:
                flash("No se encontró el campo seleccionado en los datos.")
        else:
            flash("Por favor selecciona un campo para graficar.")
    return render_template('R2graficar.html', plot_url=None)

# Nueva ruta para contar sinónimos
@app.route('/contar_sinonimos', methods=['POST'])
def contar_sinonimos_route():
    try:
        #ejecutar_proceso_completo()  # Llama al método de proceso completo
        flash("El conteo de sinónimos se completó exitosamente.")
        return render_template('R3contar_sinonimos.html')
    except Exception as e:
        flash(f"Hubo un error en el conteo de sinónimos: {str(e)}")
        
    return render_template('R3contar_sinonimos.html', frecuencias=None)

@app.route('/extraer_abstracts', methods=['POST'])
def extraer_abstracts_route():
    try:
        extraer_y_guardar_abstracts()  # Ejecuta el proceso de extracción de abstracts
        flash("Los abstracts fueron extraídos y guardados exitosamente.")
    except Exception as e:
        flash(f"Hubo un error al extraer los abstracts: {str(e)}")

    return render_template('R3extraer_abstracts.html')  # Puede renderizar la misma página o una específica


@app.route('/mostrar_nube', methods=['GET'])
def mostrar_nube_palabras_route():
    image_base64 = generar_nube_palabras_base64()
    return render_template('R4nube_palabras.html', image_base64=image_base64)

@app.route('/mostrar_grafo', methods=['GET'])
def mostrar_grafo_route():
    graph_base64 = generar_grafo_base64()
    return render_template('R5grafo.html', graph_base64=graph_base64)

if __name__ == '__main__':
    app.run(debug=True)
