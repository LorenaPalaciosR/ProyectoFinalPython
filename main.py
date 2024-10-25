# -*- coding: utf-8 -*-

from scripts.data_processing import preprocess_data
from scripts.classification import classify_reviews
from scripts.visualization import plot_wordcloud, plot_sentiment_distribution

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
    
if __name__ == "__main__":
    main()
