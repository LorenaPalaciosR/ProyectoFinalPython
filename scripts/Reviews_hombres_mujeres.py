#pip install pandas
import pandas as pd

# Cargar el dataset
# Reemplaza 'tu_archivo.csv' con el nombre de tu archivo CSV
df = pd.read_csv('Amazon_Reviews.csv')

# Contar reseñas por género
conteo_genero = df['gender'].value_counts()

# Mostrar los resultados
print('Conteo de reseñas por género:')
print(conteo_genero)

