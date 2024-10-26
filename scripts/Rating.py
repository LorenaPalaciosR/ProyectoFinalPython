import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Amazon_Reviews.csv', encoding='latin1')  


df = df.dropna(subset=['Rating'])


df['Rating'] = df['Rating'].str.extract(r'(\d) out of 5 stars').astype(float)


df = df.dropna(subset=['Rating'])


df['Rating'] = df['Rating'].astype(int)


rating_counts = df['Rating'].value_counts().sort_index()

# Grafico
plt.figure(figsize=(8, 5))
rating_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Distribución de Ratings de las Reseñas')
plt.xlabel('Rating (1 a 5)')
plt.ylabel('Número de Reseñas')
plt.xticks(rotation=0)
plt.show()