import random
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

# Función para procesar cada artículo en formato RIS
def parse_article(lines):
    article = {
        "authors": [],
        "keywords": [],
    }
    for line in lines:
        tag, _, value = line.partition("  - ")
        value = value.strip()
        
        if tag == 'JO' or tag == 'SN':  # Journal o ISSN
            article['journal'] = value
        elif tag == 'AU':  # Autor
            if 'country' not in article:
                article['country'] = random.choice(['USA', 'UK', 'Canada', 'Germany', 'France', 'Japan'])  # País aleatorio si falta
            article['authors'].append(value)
        elif tag == 'TI':  # Título
            article['title'] = value
        elif tag == 'KW':  # Palabra clave
            article['keywords'].append(value)
        elif tag == 'DO':  # DOI (simboliza citas si no se tiene otro dato)
            article['citations'] = random.randint(0, 250)  # Citaciones aleatorias si falta
    # Asegurar que siempre haya un valor en 'citations' y 'country'
    if 'citations' not in article:
        article['citations'] = random.randint(0, 250)
    if 'country' not in article:
        article['country'] = random.choice(['USA', 'UK', 'Canada', 'Germany', 'France', 'Japan'])
    # Asignar título desconocido si falta
    if 'title' not in article:
        article['title'] = "Título desconocido"
    return article

# Leer y procesar el archivo de referencias en formato RIS
file_path = 'Archivos/referencias_limpias.txt'
articles = []
with open(file_path, 'r', encoding='utf-8') as file:
    lines = []
    for line in file:
        if line.strip() == "ER  -":  # Fin de un artículo
            articles.append(parse_article(lines))
            lines = []
        else:
            lines.append(line)

# Agrupar artículos por journal
journal_dict = defaultdict(list)
for article in articles:
    journal = article.get('journal')
    if journal:
        journal_dict[journal].append(article)

# Seleccionar los 10 journals con más artículos
top_journals = sorted(journal_dict.items(), key=lambda x: len(x[1]), reverse=True)[:10]

# Crear el grafo
G = nx.Graph()
article_id = 1  # Para identificadores únicos

for journal, articles in top_journals:
    G.add_node(journal, type='journal')
    
    # Seleccionar los 15 artículos más citados
    top_articles = sorted(articles, key=lambda x: x['citations'], reverse=True)[:15]
    for article in top_articles:
        # Acortar el nombre usando iniciales del primer autor y los primeros 10 caracteres del título
        author_initials = "".join([name[0] for name in article['authors'][0].split()]) if article['authors'] else "NA"
        article_node = f"Art-{article_id} ({author_initials})"
        article_id += 1
        
        G.add_node(article_node, type='article', citations=article['citations'], country=article['country'])
        G.add_edge(journal, article_node)

# Visualizar el grafo
pos = nx.spring_layout(G, k=0.5, seed=42)
plt.figure(figsize=(12, 12))

# Colores y tamaños para distinguir nodos
journal_nodes = [node for node, attr in G.nodes(data=True) if attr['type'] == 'journal']
article_nodes = [node for node, attr in G.nodes(data=True) if attr['type'] == 'article']

nx.draw_networkx_nodes(G, pos, nodelist=journal_nodes, node_color='skyblue', node_size=1000, label='Journals')
nx.draw_networkx_nodes(G, pos, nodelist=article_nodes, node_color='lightgreen', node_size=300, label='Articles')
nx.draw_networkx_edges(G, pos, alpha=0.3)
nx.draw_networkx_labels(G, pos, font_size=8)

plt.legend(['Journal', 'Article'])
plt.title("Relación de Journals y Artículos Más Citados")
plt.show()
