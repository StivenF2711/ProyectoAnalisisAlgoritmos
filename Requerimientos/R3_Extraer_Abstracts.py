def extraer_y_guardar_abstracts():
    archivo_entrada = 'procesador_referencias/Archivos/referencias_limpias.txt'
    archivo_salida = 'procesador_referencias/Archivos/abstracts_extraidos.txt'
    abstracts = []
    dentro_de_abstract = False
    abstract_actual = []

    # Lectura y extracción de abstracts
    with open(archivo_entrada, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('AB  -'):
                dentro_de_abstract = True
                abstract_actual.append(line[5:].strip())
            elif line.startswith('ER  -'):
                if dentro_de_abstract:
                    abstracts.append(' '.join(abstract_actual))
                    abstract_actual = []
                dentro_de_abstract = False
            elif dentro_de_abstract and not line.startswith(('KW  -', 'SN  -', 'LA  -', 'J2  -', 'M3  -', 'DB  -', 'N1  -', 'TI  -')):
                abstract_actual.append(line.strip())

    # Guardado en archivo de salida
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        for abstract in abstracts:
            f.write(abstract + '\n\n')

    print(f"Abstracts extraídos y guardados en {archivo_salida}.")

# Uso del método

extraer_y_guardar_abstracts()
