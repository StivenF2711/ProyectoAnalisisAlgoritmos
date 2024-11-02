from collections import Counter
import re

def cargar_sinonimos(nombre_archivo):
    sinonimos = {}
    
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                # Elimina espacios en blanco y divide cada línea en palabras usando "-" como delimitador
                palabras = linea.strip().split('-')
                
                # Agrega cada palabra como clave en el diccionario
                for palabra in palabras:
                    palabra_normalizada = palabra.strip().lower()  # Normaliza la palabra
                    sinonimos[palabra_normalizada] = palabra_normalizada  # Almacena solo el sinónimo

        return sinonimos
    
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None


def extraer_abstracts(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            # Lee cada línea y almacena cada abstract en una lista
            abstracts = [linea.strip() for linea in archivo if linea.strip()]
        return abstracts
    
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None


def contar_frecuencia_terminos(abstracts, terminos):
    # Inicializa un diccionario para almacenar la frecuencia de cada término
    frecuencias = {termino: 0 for termino in terminos}
    
    # Procesa cada abstract
    for abstract in abstracts:
        for termino in terminos:
            # Actualiza la frecuencia total de cada término en todos los abstracts
            frecuencias[termino] += len(re.findall(re.escape(termino), abstract, re.IGNORECASE))
    
    return frecuencias


def guardar_frecuencias(nombre_archivo, frecuencias):
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            for termino, frecuencia in frecuencias.items():
                archivo.write(f"{termino}: {frecuencia}\n")
        print(f"Frecuencias guardadas en {nombre_archivo}.")
    except Exception as e:
        print(f"Error al guardar las frecuencias: {e}")


# Carga los sinónimos desde el archivo
nombre_archivo_sinonimos = "sinonimos.txt"
sinonimos = cargar_sinonimos(nombre_archivo_sinonimos)

# Llama a la función para extraer los abstracts y contar las frecuencias
nombre_archivo_abstracts = "abstracts_extraidos.txt"
texto = extraer_abstracts(nombre_archivo_abstracts)

# Verifica que texto no sea None antes de contar frecuencias
if texto is not None:
    frecuencias = contar_frecuencia_terminos(texto, sinonimos)
    print(frecuencias)
    
    # Guarda las frecuencias en un archivo
    nombre_archivo_resultados = "frecuencias_resultados.txt"
    guardar_frecuencias(nombre_archivo_resultados, frecuencias)
else:
    print("No se pudieron extraer los abstracts.")
