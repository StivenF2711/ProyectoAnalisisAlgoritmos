import base64
import io
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generar_nube_palabras_base64():
    file_path = 'procesador_referencias/Archivos/frecuencias_resultados.txt'
    
    # Lee los abstracts desde el archivo
    with open(file_path, 'r', encoding='utf-8') as file:
        abstracts = file.readlines()

    # Filtra los abstracts que son iguales a "0"
    abstracts_filtrados = [abstract for abstract in abstracts if abstract.strip() != "0"]
    
    # Une todos los abstracts filtrados en una sola cadena de texto
    texto_completo = " ".join(abstracts_filtrados)

    # Genera la nube de palabras
    wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis',
                            max_words=100, collocations=False).generate(texto_completo)

    # Guarda la imagen en un objeto de bytes
    img = io.BytesIO()
    wordcloud.to_image().save(img, format='PNG')
    img.seek(0)
    
    # Convierte la imagen a base64
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return plot_url
