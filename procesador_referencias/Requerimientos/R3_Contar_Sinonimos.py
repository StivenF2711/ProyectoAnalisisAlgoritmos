from collections import Counter
import re

def cargar_sinonimos(nombre_archivo):
    sinonimos = {}
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                # Si la línea contiene "-TL", se omite
                if "-TL" in linea or ":" in linea:
                    continue
                
                # Elimina espacios en blanco y divide cada línea en palabras usando "-" como delimitador
                palabras = [palabra.strip().lower() for palabra in linea.strip().split('-')]
                
                # La primera palabra de la lista será la clave principal, el resto serán sus sinónimos
                clave = palabras[0]
                sinonimos[clave] = palabras  # Almacena la lista de sinónimos
        
        return sinonimos
    
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None


def extraer_abstracts(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            # Lee todo el contenido del archivo
            contenido = archivo.read()
            
            # Usamos expresiones regulares para extraer los abstracts de forma más robusta
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


def imprimir_abstracts_y_sinonimos(abstracts, sinonimos, frecuencias):
    print("\n--- Frecuencia de Sinónimos en los Abstracts ---")
    for sinonimo, frecuencia in frecuencias.items():
        print(f"{sinonimo}: {frecuencia}")


# Cargar los sinónimos y abstracts
nombre_archivo_sinonimos = "procesador_referencias/Archivos/sinonimos.txt"
sinonimos = cargar_sinonimos(nombre_archivo_sinonimos)
print('r')
nombre_archivo_abstracts = "procesador_referencias/Archivos/abstracts_extraidos.txt"
texto = extraer_abstracts(nombre_archivo_abstracts)
print('r')
# Contar frecuencias
if texto:
    frecuencias = contar_frecuencia_terminos(texto, sinonimos)
    imprimir_abstracts_y_sinonimos(texto, sinonimos, frecuencias)
    
    # Guardar resultados
    nombre_archivo_resultados = "procesador_referencias/Archivos/frecuencias_resultados.txt"
    guardar_frecuencias(nombre_archivo_resultados, frecuencias)
else:
    print("No se pudieron extraer los abstracts.")
