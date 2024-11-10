import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, ttk

class DataVisualizer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()
        self.fields = ["Año Publicación", "Tipo Producto", "Journal", "Publisher", "Base Datos"]
        
        # Crear la ventana de la interfaz
        self.root = Tk()
        self.root.title("Visualizador de Datos")
        self.root.geometry("600x400")
        
        Label(self.root, text="Selecciona un campo para graficar los 15 resultados más repetidos:").pack(pady=10)
        
        # Menú desplegable
        self.field_combo = ttk.Combobox(self.root, values=self.fields)
        self.field_combo.pack(pady=5)
        self.field_combo.bind("<<ComboboxSelected>>")
        
        # Botón para ejecutar la opción de imprimir
        Button(self.root, text="Imprimir", command=self.imprimir_resultados).pack(pady=10)
        
        Button(self.root, text="Cerrar", command=self.root.quit).pack(pady=20)
        
        self.root.mainloop()
    
    def load_data(self):
        # Leer el archivo de texto en un DataFrame
        try:
            data = pd.read_csv(self.file_path, sep='\t')
            return data
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return pd.DataFrame()
    
    def update_chart(self, event):
        selected_field = self.field_combo.get()
        
        if selected_field in self.data.columns:
            self.graficar(selected_field)
    
    def imprimir_resultados(self):
        selected_field = self.field_combo.get()
        
        if selected_field in self.data.columns:
            self.graficar(selected_field)
    
    def graficar(self, selected_field):
        # Filtrar los valores donde el campo no sea "No encontrado"
        filtered_data = self.data[self.data[selected_field] != "No encontrado"]
        
        # Contar los valores más comunes en el campo seleccionado
        top_values = filtered_data[selected_field].value_counts().nlargest(15)
        
        # Ordenar por año si es "Año Publicación"
        if selected_field == "Año Publicación":
            top_values = top_values.sort_index()
        
        # Crear la gráfica
        plt.figure(figsize=(10, 6))
        top_values.plot(kind='bar', color='skyblue')
        plt.title(f"Top 15 más frecuentes para {selected_field}")
        plt.xlabel(selected_field)
        plt.ylabel("Frecuencia")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# Ruta del archivo
file_path = 'procesador_referencias/Archivos/datos_extraidos.txt'
DataVisualizer(file_path)
