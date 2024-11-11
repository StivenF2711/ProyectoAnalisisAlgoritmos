import base64
import io
from matplotlib import pyplot as plt
import pandas as pd


class DataVisualizer:
    def __init__(self):
        file_path = 'Archivos/datos_extraidos.txt'
        self.file_path = file_path
        self.data = self.load_data()
        self.fields = ["Año Publicación", "Tipo Producto", "Journal", "Publisher", "Base Datos"]
    
    def load_data(self):
        # Leer el archivo de texto en un DataFrame
        try:
            data = pd.read_csv(self.file_path, sep='\t')
            return data
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return pd.DataFrame()
    
    def graficar(self, selected_field):
        # Verificar que el campo exista en los datos
        if selected_field not in self.data.columns:
            return None

        # Filtrar los valores donde el campo no sea "No encontrado"
        filtered_data = self.data[self.data[selected_field] != "No encontrado"]
        
        # Contar los valores más comunes en el campo seleccionado
        top_values = filtered_data[selected_field].value_counts().nlargest(15)
        
        # Ordenar por año si es "Año Publicación"
        if selected_field == "Año Publicación":
            top_values = top_values.sort_index()

        # Crear la gráfica y guardarla en un objeto de bytes
        fig, ax = plt.subplots(figsize=(10, 6))
        top_values.plot(kind='bar', color='skyblue', ax=ax)
        ax.set_title(f"Top 15 más frecuentes para {selected_field}")
        ax.set_xlabel(selected_field)
        ax.set_ylabel("Frecuencia")
        ax.set_xticklabels(top_values.index, rotation=45)
        
        # Convertir la gráfica en una imagen de bytes
        img = io.BytesIO()
        plt.tight_layout()
        fig.savefig(img, format='png')
        img.seek(0)
        plt.close(fig)
        
        # Codificar la imagen en base64
        plot_url = base64.b64encode(img.getvalue()).decode('utf8')
        return plot_url

