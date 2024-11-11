import os
from flask import Flask, render_template, redirect, request, url_for, flash
from R1_Procesar_Datos import limpiar_referencias
from R2_Extraer_Datos import ExtraerDatos

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
    
if __name__ == '__main__':
    app.run(debug=True)
