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

def limpiar_referencias(carpetas, archivo_salida):
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

# Lista de carpetas donde se encuentran los archivos RIS
carpetas = [
    "C:/Users/Stiven Fajardo/Documents/GitHub/ProyectoAnalisisAlgoritmos/Bases de datos/IEEE",
    "C:/Users/Stiven Fajardo/Documents/GitHub/ProyectoAnalisisAlgoritmos/Bases de datos/jstor",
    "C:/Users/Stiven Fajardo/Documents/GitHub/ProyectoAnalisisAlgoritmos/Bases de datos/SAGE",
    "C:/Users/Stiven Fajardo/Documents/GitHub/ProyectoAnalisisAlgoritmos/Bases de datos/ScienceDirect",
    "C:/Users/Stiven Fajardo/Documents/GitHub/ProyectoAnalisisAlgoritmos/Bases de datos/Scopus",
    "C:/Users/Stiven Fajardo/Documents/GitHub/ProyectoAnalisisAlgoritmos/Bases de datos/Springer",
    "C:/Users/Stiven Fajardo/Documents/GitHub/ProyectoAnalisisAlgoritmos/Bases de datos/Taylor & Francis"
]

# Archivo de salida donde se guardarán los documentos procesados sin duplicados
archivo_salida = "C:/Users/Stiven Fajardo/Documents/GitHub/ProyectoAnalisisAlgoritmos/Bases de datos/referencias_limpias.txt"

# Ejecutar la limpieza
limpiar_referencias(carpetas, archivo_salida)
