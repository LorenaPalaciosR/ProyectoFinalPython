# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def plot_wordcloud(df, sentiment, output_path):
    
    text = " ".join(str(review) for review in df[df['Sentiment_Title'] == sentiment]['Review Text'])
    wordcloud = WordCloud(width=800, height=400, max_words=50, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='hanning')
    plt.axis("off")
    plt.title(f"WordCloud - {sentiment}")
    plt.savefig(output_path)
    plt.show()

def plot_sentiment_distribution(df):
    
    df['Sentiment_Title'].value_counts().plot(kind='bar', color=['green', 'red', 'orange'])
    plt.title('Distribución de Sentimientos por Título')
    plt.xlabel('Sentimientos')
    plt.ylabel('Cantidad')
    plt.show()

