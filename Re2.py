import re
import tkinter as tk
from tkinter import filedialog, messagebox

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

    messagebox.showinfo("Éxito", f"Datos guardados exitosamente en {ruta_salida}")

# Función para seleccionar archivos
def seleccionar_archivo_entrada():
    archivo_entrada = filedialog.askopenfilename(title="Seleccionar archivo de entrada", filetypes=[("Text files", "*.txt")])
    entrada_var.set(archivo_entrada)

def seleccionar_archivo_salida():
    archivo_salida = filedialog.asksaveasfilename(title="Seleccionar archivo de salida", defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    salida_var.set(archivo_salida)

def procesar_archivos():
    ruta_entrada = entrada_var.get()
    ruta_salida = salida_var.get()
    if ruta_entrada and ruta_salida:
        filtrar_datos_y_guardar(ruta_entrada, ruta_salida)
    else:
        messagebox.showwarning("Advertencia", "Selecciona los archivos de entrada y salida antes de continuar.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Procesador de Referencias")

# Variables para almacenar las rutas de los archivos
entrada_var = tk.StringVar()
salida_var = tk.StringVar()

# Crear los widgets de la interfaz
label_entrada = tk.Label(ventana, text="Archivo de entrada:")
label_entrada.pack(pady=5)

entrada_entry = tk.Entry(ventana, textvariable=entrada_var, width=50)
entrada_entry.pack(pady=5)

btn_seleccionar_entrada = tk.Button(ventana, text="Seleccionar archivo de entrada", command=seleccionar_archivo_entrada)
btn_seleccionar_entrada.pack(pady=5)

label_salida = tk.Label(ventana, text="Archivo de salida:")
label_salida.pack(pady=5)

salida_entry = tk.Entry(ventana, textvariable=salida_var, width=50)
salida_entry.pack(pady=5)

btn_seleccionar_salida = tk.Button(ventana, text="Seleccionar archivo de salida", command=seleccionar_archivo_salida)
btn_seleccionar_salida.pack(pady=5)

btn_procesar = tk.Button(ventana, text="Procesar archivos", command=procesar_archivos)
btn_procesar.pack(pady=20)

# Iniciar la ventana
ventana.mainloop()
