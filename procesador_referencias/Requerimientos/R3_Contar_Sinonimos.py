from collections import Counter
import re

def cargar_sinonimos(nombre_archivo):
    sinonimos = {}
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                if "-TL" in linea or ":" in linea:
                    continue
                palabras = [palabra.strip().lower() for palabra in linea.strip().split('-')]
                clave = palabras[0]
                sinonimos[clave] = palabras
        return sinonimos
    except FileNotFoundError:
        print("El archivo de sinónimos no se encontró.")
        return None


def extraer_abstracts(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            abstracts = re.split(r'\n{2,}', contenido.strip())
            abstracts = [re.sub(r'\s+', ' ', abstract).strip() for abstract in abstracts if abstract.strip()]
        return abstracts
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
        return []
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
        return []


def contar_frecuencia_terminos(abstracts, sinonimos):
    frecuencias = {clave: 0 for clave in sinonimos}
    for abstract in abstracts:
        abstract_normalizado = abstract.lower()
        for clave, lista_sinonimos in sinonimos.items():
            for sinonimo in lista_sinonimos:
                coincidencias = re.findall(r'\b' + re.escape(sinonimo) + r'\b', abstract_normalizado)
                frecuencias[clave] += len(coincidencias)
    return frecuencias


def guardar_frecuencias(nombre_archivo, frecuencias):
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            for termino, frecuencia in frecuencias.items():
                archivo.write(f"{termino}: {frecuencia}\n")
        print(f"Frecuencias guardadas en {nombre_archivo}.")
    except Exception as e:
        print(f"Error al guardar las frecuencias: {e}")


def imprimir_frecuencias(frecuencias):
    print("\n--- Frecuencia de Sinónimos en los Abstracts ---")
    for sinonimo, frecuencia in frecuencias.items():
        print(f"{sinonimo}: {frecuencia}")


def ejecutar_proceso_completo():
    nombre_archivo_sinonimos = "procesador_referencias/Archivos/sinonimos.txt"
    nombre_archivo_abstracts = "procesador_referencias/Archivos/abstracts_extraidos.txt"
    nombre_archivo_resultados = "procesador_referencias/Archivos/frecuencias_resultados.txt"
    
    # Cargar los sinónimos
    sinonimos = cargar_sinonimos(nombre_archivo_sinonimos)
    if sinonimos is None:
        return
    
    # Extraer los abstracts
    abstracts = extraer_abstracts(nombre_archivo_abstracts)
    if not abstracts:
        print("No se pudieron extraer los abstracts.")
        return
    
    # Contar frecuencias
    frecuencias = contar_frecuencia_terminos(abstracts, sinonimos)
    
    # Imprimir y guardar resultados
    imprimir_frecuencias(frecuencias)
    guardar_frecuencias(nombre_archivo_resultados, frecuencias)

# Llamada a la función principal para ejecutar todo el proceso
ejecutar_proceso_completo()
