from wordcloud import WordCloud
import matplotlib.pyplot as plt

def leer_abstracts(file_path):
    # Lee los abstracts desde el archivo y los devuelve como una lista de strings
    with open(file_path, 'r', encoding='utf-8') as file:
        abstracts = file.readlines()
    return abstracts

def generar_nube_palabras(abstracts):
    # Une todos los abstracts en una sola cadena de texto
    texto_completo = " ".join(abstracts)

    # Genera la nube de palabras
    wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis',
                        max_words=100, collocations=False).generate(texto_completo)

    # Muestra la nube de palabras
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

# Ruta al archivo de texto con los abstracts
file_path = 'Archivos/datos_extraidos.txt'

# Lee los abstracts y genera la nube de palabras
abstracts = leer_abstracts(file_path)
generar_nube_palabras(abstracts)
