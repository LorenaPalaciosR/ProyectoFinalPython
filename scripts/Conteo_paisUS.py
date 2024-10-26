#pip install pandas
import pandas as pd

# Cargar el dataset
def preprocess_data3(file_path):
    """
    Función para cargar un archivo CSV y contar el número de reseñas del país 'US'.
    """
    try:
        # Cargar los datos con manejo de errores
        df = pd.read_csv(file_path, delimiter=',', encoding='utf-8', on_bad_lines='skip')
        
        # Verificar si la columna 'Country' existe en el DataFrame
        if 'Country' in df.columns:
            # Filtrar las reseñas que sean del país 'US'
            conteo_us = df[df['Country'] == 'US'].shape[0]
            
            # Mostrar los resultados
            print(f"Conteo de reseñas para US: {conteo_us}")
        else:
            print("Error: La columna 'Country' no existe en el archivo CSV.")
    
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
    
    return df