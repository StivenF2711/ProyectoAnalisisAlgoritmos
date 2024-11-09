import re
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import pandas as pd

# Función para filtrar y guardar datos
def filtrar_datos_y_guardar_completo(ruta_archivo, ruta_salida):
    datos = []
    
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()

    documentos = contenido.split("ER  -")
    
    for documento in documentos:
        # Extraer datos
        primer_autor = re.search(r"AU\s+-\s+([^\n]+)", documento)
        año_publicacion = re.search(r"PY\s+-\s+(\d{4})", documento)
        tipo_producto = re.search(r"TY\s+-\s+([^\n]+)", documento)
        journal = re.search(r"JO\s+-\s+([^\n]+)", documento)
        afiliacion = re.search(r"AF\s+-\s+([^\n]+)", documento)
        publisher = re.search(r"PB\s+-\s+([^\n]+)", documento)
        base_datos = re.search(r"DB\s+-\s+([^\n]+)", documento)
        citaciones = re.search(r"CR\s+-\s+(\d+)", documento)

        datos.append({
            'Primer Autor': primer_autor.group(1) if primer_autor else "No encontrado",
            'Año Publicación': int(año_publicacion.group(1)) if año_publicacion else "No encontrado",
            'Tipo Producto': tipo_producto.group(1) if tipo_producto else "No encontrado",
            'Journal': journal.group(1) if journal else "No encontrado",
            'Afiliación': afiliacion.group(1) if afiliacion else "No encontrado",
            'Publisher': publisher.group(1) if publisher else "No encontrado",
            'Base Datos': base_datos.group(1) if base_datos else "No encontrado",
            'Citaciones': int(citaciones.group(1)) if citaciones else 0
        })

    with open(ruta_salida, 'w', encoding='utf-8') as archivo_salida:
        archivo_salida.write("Primer Autor\tAño Publicación\tTipo Producto\tJournal\tAfiliación\tPublisher\tBase Datos\tCitaciones\n")
        for dato in datos:
            archivo_salida.write(
                f"{dato['Primer Autor']}\t{dato['Año Publicación']}\t{dato['Tipo Producto']}\t"
                f"{dato['Journal']}\t{dato['Afiliación']}\t{dato['Publisher']}\t"
                f"{dato['Base Datos']}\t{dato['Citaciones']}\n"
            )
    
    messagebox.showinfo("Éxito", f"Datos completos y estadísticas guardados exitosamente en {ruta_salida}")



def procesar_archivos():
    ruta_entrada = "Archivos/referencias_limpias.txt"
    ruta_salida = "Archivos/datos_extraidos.txt"  # Archivo de salida predefinido
    if ruta_entrada:
        filtrar_datos_y_guardar_completo(ruta_entrada, ruta_salida)
    else:
        messagebox.showwarning("Advertencia", "Selecciona el archivo de entrada antes de continuar.")

procesar_archivos()

