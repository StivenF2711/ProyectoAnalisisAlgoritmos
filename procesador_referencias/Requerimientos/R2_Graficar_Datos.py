import pandas as pd
import matplotlib.pyplot as plt
import os

class DataVisualizer:
    def __init__(self, file_path):
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
        # Filtrar los valores donde el campo no sea "No encontrado"
        filtered_data = self.data[self.data[selected_field] != "No encontrado"]
        
        # Contar los valores más comunes en el campo seleccionado
        top_values = filtered_data[selected_field].value_counts().nlargest(15)
        
        # Ordenar por año si es "Año Publicación"
        if selected_field == "Año Publicación":
            top_values = top_values.sort_index()
        
        # Crear y guardar la gráfica
        plt.figure(figsize=(10, 6))
        top_values.plot(kind='bar', color='skyblue')
        plt.title(f"Top 15 más frecuentes para {selected_field}")
        plt.xlabel(selected_field)
        plt.ylabel("Frecuencia")
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        # Guardar el gráfico como imagen
        image_path = os.path.join("static", "graficos", f"{selected_field}_top15.png")
        plt.savefig(image_path)
        plt.close()  # Cerrar la figura para liberar memoria
        
        return image_path
