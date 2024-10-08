import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def leer_archivo_y_extraer_datos_multiples(ruta_archivo):
    datos = []  # Lista para almacenar los datos extraídos
    
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()

    # Dividimos el archivo en varios documentos separados por 'ER  -', que marca el final de cada uno
    documentos = contenido.split("ER  -")
    
    for i, documento in enumerate(documentos):
        # Extraer primer autor
        primer_autor = re.search(r"AU\s+-\s+([^\n]+)", documento)
        primer_autor = primer_autor.group(1) if primer_autor else "No encontrado"

        # Extraer año de publicación
        año_publicacion = re.search(r"PY\s+-\s+(\d{4})", documento)
        año_publicacion = año_publicacion.group(1) if año_publicacion else "No encontrado"

        # Extraer tipo de producto
        tipo_producto = re.search(r"TY\s+-\s+([^\n]+)", documento)
        tipo_producto = tipo_producto.group(1) if tipo_producto else "No encontrado"
        
        # Extraer afiliación del primer autor (no está explícito en el archivo, suponemos que no está)
        afiliacion_autor = re.search(r"DA\s+-\s+([^\n]+)", documento)
        afiliacion_autor = afiliacion_autor.group(1) if afiliacion_autor else "No encontrado"

        # Extraer journal
        journal = re.search(r"JO\s+-\s+([^\n]+)", documento)
        journal = journal.group(1) if journal else "No encontrado"

        # Extraer publisher
        publisher = re.search(r"PB\s+-\s+([^\n]+)", documento)
        publisher = publisher.group(1) if publisher else "No encontrado"
        
        # Extraer base de datos
        base_datos = re.search(r"DB\s+-\s+([^\n]+)", documento) 
        base_datos = base_datos.group(1) if base_datos else "No encontrado"

        # Citaciones (como no está directamente en el archivo, lo dejamos como 'No proporcionado')
        citaciones = "No proporcionado"

        # Guardar los datos en un diccionario
        datos.append({
            'Primer Autor': primer_autor,
            'Año Publicación': año_publicacion,
            'Tipo Producto': tipo_producto,
            'Afiliación Autor': afiliacion_autor,
            'Journal': journal,
            'Publisher': publisher,
            'Base de Datos': base_datos,
            'Citaciones': citaciones
        })

    return datos

# Ruta del archivo de texto con múltiples documentos
ruta_archivo = "referencias_limpias.txt"
datos = leer_archivo_y_extraer_datos_multiples(ruta_archivo)

# Convertir los datos en un DataFrame de pandas
df = pd.DataFrame(datos)

# Mostrar los primeros registros para verificar
print(df.head())

# Ejemplo de gráfico: Conteo de productos por año y tipo de producto
plt.figure(figsize=(10, 6))
sns.countplot(x='Año Publicación', hue='Tipo Producto', data=df)
plt.title('Distribución de productos por año y tipo de producto')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
