# -*- coding: utf-8 -*-

from scripts.data_processing import preprocess_data
from scripts.classification import classify_reviews
from scripts.visualization import plot_wordcloud, plot_sentiment_distribution
from scripts.Rating1 import preprocess_data2
from scripts.Conteo_paisUS import preprocess_data3


def main():
    # Cargar y preprocesar los datos
    df = preprocess_data('data/Amazon_Reviews.csv')
    
    # Clasificar las reviews
    df = classify_reviews(df)
    
    # Guardar los resultados
    df.to_csv('results/sentiment_analysis.csv', index=False)
    
    # Generar nubes de palabras
    plot_wordcloud(df, 'Positive', 'results/wordclouds/positive.png')
    plot_wordcloud(df, 'Negative', 'results/wordclouds/negative.png')
    plot_wordcloud(df, 'Neutral', 'results/wordclouds/neutral.png') 
    
    # Mostrar la distribución de sentimientos
    plot_sentiment_distribution(df)
    df_procesado = preprocess_data2('data/Amazon_Reviews.csv')
    df_procesado2 = preprocess_data3('data/Amazon_Reviews.csv')
    
    
if __name__ == "__main__":
    main()
