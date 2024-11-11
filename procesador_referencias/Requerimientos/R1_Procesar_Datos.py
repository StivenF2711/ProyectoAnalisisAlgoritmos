import os

def extraer_identificador_unico(contenido):
    for linea in contenido.splitlines():
        if linea.startswith("DO  -"):  # DOI
            return linea.replace("DO  - ", "").strip()
        elif linea.startswith("ID  -"):  # Otro tipo de identificador
            return linea.replace("ID  - ", "").strip()
    return None

def leer_archivo_ris(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        return archivo.read()

def limpiar_referencias():
    # Lista de carpetas donde se encuentran los archivos RIS
    carpetas = [
        "procesador_referencias/Bases de datos/IEEE",
        "procesador_referencias/Bases de datos/jstor",
        "procesador_referencias/Bases de datos/SAGE",
        "procesador_referencias/Bases de datos/ScienceDirect",
        "procesador_referencias/Bases de datos/Scopus",
        "procesador_referencias/Bases de datos/Springer",
        "procesador_referencias/Bases de datos/Taylor & Francis"
    ]
    
    # Archivo de salida donde se guardarán los documentos procesados sin duplicados
    archivo_salida = "procesador_referencias/Archivos/referencias_limpias.txt"

    referencias_procesadas = set()  # Para almacenar identificadores únicos
    with open(archivo_salida, 'w', encoding='utf-8') as salida:
        for carpeta in carpetas:
            if not os.path.exists(carpeta):
                print(f"La carpeta {carpeta} no existe.")
                continue
            for archivo in os.listdir(carpeta):
                if archivo.endswith(".ris"):
                    ruta_archivo = os.path.join(carpeta, archivo)
                    contenido = leer_archivo_ris(ruta_archivo)
                    identificador = extraer_identificador_unico(contenido)

                    # Verificar si ya hemos procesado este identificador
                    if identificador and identificador not in referencias_procesadas:
                        salida.write(contenido + "\n\n")
                        referencias_procesadas.add(identificador)
                        print(f"Procesado: {identificador}")
                    elif identificador:
                        print(f"Duplicado encontrado: {identificador}, saltando...")
                    else:
                        print(f"Identificador único no encontrado en {archivo}, agregando de todos modos.")
                        salida.write(contenido + "\n\n")

# Ejecutar la limpieza
limpiar_referencias()
