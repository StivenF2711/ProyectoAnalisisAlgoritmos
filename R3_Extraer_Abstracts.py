def extraer_abstracts(archivo):
    abstracts = []
    dentro_de_abstract = False  # Indica si estamos dentro de un abstract
    abstract_actual = []

    with open(archivo, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('AB  -'):
                dentro_de_abstract = True
                abstract_actual.append(line[5:].strip())  # Tomar el texto del abstract después de 'AB  -'
            elif line.startswith('ER  -'):  # Marca el fin de la entrada actual
                if dentro_de_abstract:
                    abstracts.append(' '.join(abstract_actual))  # Guarda el abstract completo
                    abstract_actual = []  # Reinicia para el siguiente abstract
                dentro_de_abstract = False
            elif dentro_de_abstract and not line.startswith(('KW  -', 'SN  -', 'LA  -', 'J2  -', 'M3  -', 'DB  -', 'N1  -', 'TI  -')):
                # Solo agregar líneas que no contengan otras etiquetas
                abstract_actual.append(line.strip())

    return abstracts

# Uso del método
archivo_referencias = 'Archivos/referencias_limpias.txt'
abstracts = extraer_abstracts(archivo_referencias)

# Guardar los abstracts en un archivo separado
output_path = 'Archivos/abstracts_extraidos.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    for abstract in abstracts:
        f.write(abstract + '\n\n')  # Separa cada abstract con una línea vacía

# Mostrar el resultado
print(f"Abstracts extraídos y guardados en {output_path}. Contenido:")
with open(output_path, 'r', encoding='utf-8') as f:
    print(f.read())
