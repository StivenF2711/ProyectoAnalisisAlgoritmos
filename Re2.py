import re

def filtrar_datos_y_guardar(ruta_archivo, ruta_salida):
    datos = []  # Lista para almacenar los datos extraídos
    
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()

    # Dividimos el archivo en varios documentos separados por 'ER  -', que marca el final de cada uno
    documentos = contenido.split("ER  -")
    
    for i, documento in enumerate(documentos):
        # Extraer primer autor
        primer_autor = re.search(r"AU\s+-\s+([^\n]+)", documento)
        primer_autor = primer_autor.group(1) if primer_autor else " "

        # Extraer año de publicación
        año_publicacion = re.search(r"PY\s+-\s+(\d{4})", documento)
        año_publicacion = año_publicacion.group(1) if año_publicacion else " "

        # Extraer tipo de producto
        tipo_producto = re.search(r"TY\s+-\s+([^\n]+)", documento)
        tipo_producto = tipo_producto.group(1) if tipo_producto else " "
        
        # Extraer journal
        journal = re.search(r"JO\s+-\s+([^\n]+)", documento)
        journal = journal.group(1) if journal else " "

        # Guardar los datos en un diccionario
        datos.append({
            'Primer Autor': primer_autor,
            'Año Publicación': año_publicacion,
            'Tipo Producto': tipo_producto,
            'Journal': journal
        })

    # Guardar los datos en un archivo de texto
    with open(ruta_salida, 'w', encoding='utf-8') as archivo_salida:
        archivo_salida.write("Primer Autor\tAño Publicación\tTipo Producto\tJournal\t\n")
        for dato in datos:
            archivo_salida.write(f"{dato['Primer Autor']}\t{dato['Año Publicación']}\t{dato['Tipo Producto']}\t{dato['Journal']}\t\n")

    print(f"Datos guardados exitosamente en {ruta_salida}")

ruta_archivo = "referencias_limpias.txt"  # Archivo de entrada
ruta_salida = "datos_extraidos.txt"  # Archivo donde se guardarán los datos procesados

filtrar_datos_y_guardar(ruta_archivo, ruta_salida)

