def extraer_abstracts(archivo):
    abstracts = []
    with open(archivo, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    current_abstract = []
    dentro_de_abstract = False
    
    # Leer línea por línea y detectar el comienzo y fin de los abstracts
    for line in lines:
        if line.startswith('AB  -'):  # Marca el inicio del abstract
            dentro_de_abstract = True
            current_abstract.append(line[5:].strip())  # Tomar el abstract y quitar el 'AB  -'
        elif line.startswith('ER  -'):  # Marca el fin de una entrada
            if dentro_de_abstract:
                abstracts.append(' '.join(current_abstract))  # Unir el abstract y agregarlo a la lista
                current_abstract = []  # Reiniciar para el siguiente abstract
            dentro_de_abstract = False
        elif dentro_de_abstract:
            current_abstract.append(line.strip())  # Continuar leyendo el abstract si estamos dentro de él

    return abstracts

# Uso del método
archivo_referencias = 'Archivos/referencias_limpias.txt'
abstracts = extraer_abstracts(archivo_referencias)

# Guardar los abstracts en un archivo separado
output_path = 'Archivos/abstracts_extraidos.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    for abstract in abstracts:
        f.write(abstract + '\n\n')  # Separar los abstracts con una línea vacía

# Mostrar el resultado
print(f"Abstracts extraídos y guardados en {output_path}. Contenido:")
with open(output_path, 'r', encoding='utf-8') as f:
    print(f.read())
