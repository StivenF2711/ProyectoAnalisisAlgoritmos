import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import filedialog, messagebox

def leer_datos_y_graficar(ruta_datos):
    df = pd.read_csv(ruta_datos, sep='\t')
    df = df[df['Primer Autor'] != 'No encontrado']
    frecuencia_autores = df['Primer Autor'].value_counts()
    autores_top = frecuencia_autores.nlargest(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=autores_top.values, y=autores_top.index, palette='viridis')
    plt.title('Top 10 Autores por Número de Publicaciones')
    plt.xlabel('Número de Publicaciones')
    plt.ylabel('Autor')
    plt.show()

def graficar_documentos_por_año(ruta_datos):
    # Cargar el archivo CSV
    df = pd.read_csv(ruta_datos, sep='\t')
    
    # Filtrar valores que contengan "No encontrado"
    df_filtrado = df[df['Año Publicación'].notna()]  # Eliminar NaN
    df_filtrado = df_filtrado[~df_filtrado['Año Publicación'].str.contains("No encontrado", case=False, na=False)]  # Excluir "No encontrado"
    
    # Contar documentos por año y ordenar por año
    documentos_por_año = df_filtrado['Año Publicación'].value_counts().sort_index()
    
    # Graficar
    plt.figure(figsize=(10, 6))
    sns.barplot(x=documentos_por_año.index, y=documentos_por_año.values, palette='coolwarm')
    plt.title('Cantidad de Documentos por Año de Publicación')
    plt.xlabel('Año de Publicación')
    plt.ylabel('Cantidad de Documentos')
    plt.xticks(rotation=45)
    plt.show()

def graficar_cantidad_por_tipo_producto(ruta_datos):
    df = pd.read_csv(ruta_datos, sep='\t')
    documentos_por_tipo = df['Tipo Producto'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=documentos_por_tipo.values, y=documentos_por_tipo.index, palette='coolwarm')
    plt.title('Cantidad de Documentos por Tipo de Producto')
    plt.xlabel('Cantidad de Documentos')
    plt.ylabel('Tipo de Producto')
    plt.show()

def graficar_journals_mas_repetidos(ruta_datos, top_n=10):
    # Cargar el archivo CSV
    df = pd.read_csv(ruta_datos, sep='\t')
    
    # Filtrar valores que contengan "No encontrado"
    df_filtrado = df['Journal'].dropna()  # Elimina valores NaN
    df_filtrado = df_filtrado[~df_filtrado.str.contains("No encontrado", case=False, na=False)]  # Excluye los que contienen "No encontrado"

    # Obtener los journals más comunes
    journals_mas_comunes = df_filtrado.value_counts().nlargest(top_n)
    
    # Graficar
    plt.figure(figsize=(10, 6))
    sns.barplot(x=journals_mas_comunes.values, y=journals_mas_comunes.index)
    plt.title(f'Top {top_n} Journals Más Repetidos')
    plt.xlabel('Cantidad de Documentos')
    plt.ylabel('Journal')
    plt.show()


# Función para seleccionar el archivo
def seleccionar_archivo():
    archivo_datos = filedialog.askopenfilename(title="Seleccionar archivo de datos", filetypes=[("Text files", "*.txt")])
    archivo_var.set(archivo_datos)

# Función para ejecutar la gráfica correspondiente
def ejecutar_grafica(grafica_func):
    ruta_datos = archivo_var.get()
    if ruta_datos:
        grafica_func(ruta_datos)
    else:
        messagebox.showwarning("Advertencia", "Por favor, selecciona un archivo de datos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Graficador de Datos Bibliográficos")

# Variable para almacenar la ruta del archivo seleccionado
archivo_var = tk.StringVar()

# Crear los widgets de la interfaz
label_archivo = tk.Label(ventana, text="Archivo de datos:")
label_archivo.pack(pady=5)

archivo_entry = tk.Entry(ventana, textvariable=archivo_var, width=50)
archivo_entry.pack(pady=5)

btn_seleccionar_archivo = tk.Button(ventana, text="Seleccionar archivo", command=seleccionar_archivo)
btn_seleccionar_archivo.pack(pady=5)

# Botones para cada una de las funciones
btn_top_autores = tk.Button(ventana, text="Top 10 Autores por Publicaciones", command=lambda: ejecutar_grafica(leer_datos_y_graficar))
btn_top_autores.pack(pady=5)

btn_docs_por_año = tk.Button(ventana, text="Documentos por Año de Publicación", command=lambda: ejecutar_grafica(graficar_documentos_por_año))
btn_docs_por_año.pack(pady=5)

btn_docs_por_tipo = tk.Button(ventana, text="Cantidad de Documentos por Tipo de Producto", command=lambda: ejecutar_grafica(graficar_cantidad_por_tipo_producto))
btn_docs_por_tipo.pack(pady=5)

btn_top_journals = tk.Button(ventana, text="Top 10 Journals Más Repetidos", command=lambda: ejecutar_grafica(graficar_journals_mas_repetidos))
btn_top_journals.pack(pady=5)

# Iniciar la ventana
ventana.mainloop()
