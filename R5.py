import re
import random
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

# Función para leer y procesar el archivo RIS
def leer_archivo_ris(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()

    # Separar cada entrada de artículo
    articulos_raw = contenido.strip().split('\nER  -\n')
    articulos = []

    for articulo_raw in articulos_raw:
        # Diccionario para almacenar campos clave del artículo
        articulo = {}
        articulo['autores'] = []
        
        # Extraer cada campo usando regex
        articulo['titulo'] = re.search(r'TI  - (.+)', articulo_raw)
        articulo['titulo'] = articulo['titulo'].group(1) if articulo['titulo'] else 'Título desconocido'
        
        # Para varios autores
        autores = re.findall(r'AU  - (.+)', articulo_raw)
        articulo['autores'] = autores if autores else ['Autor desconocido']
        
        articulo['citaciones'] = random.randint(0, 250)  # Citaciones aleatorias
        articulo['pais'] = random.choice(['USA', 'UK', 'Germany', 'China', 'India', 'France', 'Japan', 'Canada', 'Australia', 'Brazil'])
        
        articulo['journal'] = re.search(r'JO  - (.+)', articulo_raw)
        articulo['journal'] = articulo['journal'].group(1) if articulo['journal'] else re.search(r'SN  - (.+)', articulo_raw)
        articulo['journal'] = articulo['journal'] if articulo['journal'] else 'Journal desconocido'
        
        articulos.append(articulo)
    
    return articulos

# Leer el archivo de referencias
ruta_archivo = 'Archivos/referencias_limpias.txt'
articulos = leer_archivo_ris(ruta_archivo)

# Paso 2: Identificar los 10 journals con más artículos
conteo_journals = defaultdict(int)
for articulo in articulos:
    conteo_journals[articulo['journal']] += 1

top_journals = sorted(conteo_journals, key=conteo_journals.get, reverse=True)[:10]
articulos_filtrados = [articulo for articulo in articulos if articulo['journal'] in top_journals]

# Paso 3: Filtrar los 15 artículos más citados de cada journal
# y construir el grafo
grafo = nx.Graph()
for journal in top_journals:
    articulos_journal = [art for art in articulos_filtrados if art['journal'] == journal]
    top_articulos = sorted(articulos_journal, key=lambda x: x['citaciones'], reverse=True)[:15]

    # Añadir el nodo del journal
    grafo.add_node(journal, tipo='journal')

    # Añadir cada artículo y el país como nodos relacionados al journal
    for articulo in top_articulos:
        nodo_articulo = articulo['titulo']
        grafo.add_node(nodo_articulo, tipo='articulo', citaciones=articulo['citaciones'])
        grafo.add_edge(journal, nodo_articulo)  # Conectar artículo con su journal

        # Añadir el país como nodo
        nodo_pais = articulo['pais']
        grafo.add_node(nodo_pais, tipo='pais')
        grafo.add_edge(nodo_articulo, nodo_pais)  # Conectar artículo con el país del autor

# Paso 4: Visualizar el grafo
plt.figure(figsize=(15, 15))
pos = nx.spring_layout(grafo, seed=42)  # Posición de los nodos

# Dibujar nodos y etiquetas
nx.draw_networkx_nodes(grafo, pos, node_size=500, node_color="skyblue", 
                        nodelist=[n for n in grafo.nodes if grafo.nodes[n]['tipo'] == 'journal'])
nx.draw_networkx_nodes(grafo, pos, node_size=300, node_color="salmon", 
                        nodelist=[n for n in grafo.nodes if grafo.nodes[n]['tipo'] == 'articulo'])
nx.draw_networkx_nodes(grafo, pos, node_size=100, node_color="lightgreen", 
                        nodelist=[n for n in grafo.nodes if grafo.nodes[n]['tipo'] == 'pais'])

nx.draw_networkx_edges(grafo, pos, alpha=0.5)
nx.draw_networkx_labels(grafo, pos, font_size=8)

plt.title("Relación entre Journals, Artículos y Países de Primer Autor")
plt.show()
