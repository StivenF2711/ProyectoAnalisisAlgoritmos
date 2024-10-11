import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def leer_datos_y_graficar(ruta_datos):
    # Leer los datos del archivo en un DataFrame
    df = pd.read_csv(ruta_datos, sep='\t')

    # Eliminar autores con 'No encontrado' para mejorar el gráfico
    df = df[df['Primer Autor'] != 'No encontrado']

    # Contar la frecuencia de cada autor
    frecuencia_autores = df['Primer Autor'].value_counts()

    # Mostrar solo los 10 autores más frecuentes
    autores_top = frecuencia_autores.nlargest(10)

    # Crear el gráfico de los 10 principales autores
    plt.figure(figsize=(10, 6))
    sns.barplot(x=autores_top.values, y=autores_top.index, palette='viridis')
    plt.title('Top 10 Autores por Número de Publicaciones')
    plt.xlabel('Número de Publicaciones')
    plt.ylabel('Autor')
    plt.show()


def graficar_documentos_por_año(ruta_datos):

    df = pd.read_csv(ruta_datos, sep='\t')
    # Contar la cantidad de documentos por año de publicación
    documentos_por_año = df['Año Publicación'].value_counts().sort_index()

    # Crear el gráfico de barras por año
    plt.figure(figsize=(10, 6))
    sns.barplot(x=documentos_por_año.index, y=documentos_por_año.values, palette='coolwarm')
    plt.title('Cantidad de Documentos por Año de Publicación')
    plt.xlabel('Año de Publicación')
    plt.ylabel('Cantidad de Documentos')
    plt.xticks(rotation=45)  # Rotar las etiquetas del eje x para mejorar la legibilidad
    plt.show()

def graficar_cantidad_por_tipo_producto(ruta_datos):

    df = pd.read_csv(ruta_datos, sep='\t')
    # Contar la cantidad de documentos por tipo de producto
    documentos_por_tipo = df['Tipo Producto'].value_counts()

    # Crear el gráfico de barras por tipo de producto
    plt.figure(figsize=(10, 6))
    sns.barplot(x=documentos_por_tipo.values, y=documentos_por_tipo.index, palette='coolwarm')
    plt.title('Cantidad de Documentos por Tipo de Producto')
    plt.xlabel('Cantidad de Documentos')
    plt.ylabel('Tipo de Producto')
    plt.show()

def graficar_journals_mas_repetidos(ruta_datos, top_n=10):

    df = pd.read_csv(ruta_datos, sep='\t')
    # Contar la cantidad de documentos por journal
    journals_mas_comunes = df['Journal'].value_counts().nlargest(top_n)

    # Crear el gráfico de barras por journal
    plt.figure(figsize=(10, 6))
    sns.barplot(x=journals_mas_comunes.values, y=journals_mas_comunes.index)
    plt.title(f'Top {top_n} Journals Más Repetidos')
    plt.xlabel('Cantidad de Documentos')
    plt.ylabel('Journal')
    plt.show()

ruta_datos = "datos_extraidos.txt"  # Archivo generado con los datos extraídos

graficar_journals_mas_repetidos(ruta_datos, top_n=10)

#graficar_cantidad_por_tipo_producto(ruta_datos)

#graficar_documentos_por_año(ruta_datos)

#leer_datos_y_graficar(ruta_datos)
