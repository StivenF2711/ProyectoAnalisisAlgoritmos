import streamlit as st
import subprocess

# Interfaz de usuario de Streamlit
def main():
    st.title("Aplicación de Proyecto con Streamlit")
    
    menu = ["Inicio", "Limpiar Referencias RIS", "Ejecutar R1_Procesar_Datos.py", "Acerca de"]
    choice = st.sidebar.selectbox("Selecciona una opción", menu)
    
    if choice == "Inicio":
        st.subheader("Bienvenido a la aplicación")
        st.write("Esta aplicación permite ejecutar scripts y limpiar referencias RIS.")
    
    elif choice == "Limpiar Referencias RIS":
        st.subheader("Limpiar Referencias RIS")
        # Aquí va el código para limpiar referencias (como en tu ejemplo anterior)
    
    elif choice == "Ejecutar R1_Procesar_Datos.py":
        st.subheader("Ejecutar procesamiento de datos")
        if st.button("Ejecutar R1_Procesar_Datos.py"):
            # Ejecutar el script R1_Procesar_Datos.py usando subprocess
            st.write("Ejecutando R1_Procesar_Datos.py...")
            try:
                # Esto ejecutará el script desde el terminal
                result = subprocess.run(["python", "R1_Procesar_Datos.py"], capture_output=True, text=True)
                st.write("Resultado de la ejecución:")
                st.write(result.stdout)  # Imprimir la salida estándar del script
                if result.stderr:
                    st.write("Errores:")
                    st.write(result.stderr)  # Imprimir errores si los hubiera
            except Exception as e:
                st.write(f"Ocurrió un error al ejecutar el script: {e}")
    
    elif choice == "Acerca de":
        st.subheader("Sobre esta aplicación")
        st.write("Esta aplicación fue desarrollada utilizando Streamlit y Python para ejecutar scripts y limpiar referencias RIS.")

if __name__ == "__main__":
    main()
