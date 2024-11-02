from collections import Counter

# Método para leer todos los sinónimos de un archivo
def leer_sinonimos(archivo_sinonimos):
    sinonimos = set()  # Usamos un conjunto para evitar duplicados

    with open(archivo_sinonimos, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Procesar el archivo de sinónimos línea por línea
    for line in lines:
        line = line.strip()
        if line and not line.endswith('-TL'):  # Solo añadimos líneas que no son títulos
            sinonimos.update([word.strip().lower() for word in line.split(',')])  # Añadir sinónimos al conjunto

    return sinonimos

# Método para leer abstracts de un archivo de texto
def leer_abstracts(archivo):
    abstracts = []
    with open(archivo, 'r', encoding='utf-8') as f:
        abstracts = f.readlines()
    
    return [abstract.strip() for abstract in abstracts if abstract.strip()]

# Método para contar cuántas veces aparecen los sinónimos en los abstracts
def validar_palabras_abstracts(abstracts, sinonimos):
    sinonimos_count = Counter()  # Usamos Counter para contar todas las palabras sinónimos

    # Procesar cada abstract
    for abstract in abstracts:
        words_in_abstract = abstract.lower().split()

        # Validar cada palabra en el abstract comparando con los sinónimos
        for synonym in sinonimos:
            count = words_in_abstract.count(synonym)
            if count > 0:
                sinonimos_count[synonym] += count

    return sinonimos_count

# Leer los sinónimos desde el archivo 'sinonimos.txt'
sinonimos = leer_sinonimos('sinonimos.txt')

# Leer los abstracts desde el archivo 'abstracts_extraidos.txt'
abstracts = leer_abstracts('abstracts_extraidos.txt')

# Validar las palabras de los abstracts con los sinónimos
resultado_validacion = validar_palabras_abstracts(abstracts, sinonimos)

# Guardar los resultados en un archivo de salida
output_path = 'resultado_validacion_sinonimos.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    for synonym, count in resultado_validacion.items():
        f.write(f"{synonym}: {count}\n")

# Mostrar el resultado final
print(f"Resultados de validación guardados en {output_path}. Contenido:")
with open(output_path, 'r', encoding='utf-8') as f:
    print(f.read())
