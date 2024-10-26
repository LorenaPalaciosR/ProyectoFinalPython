# -*- coding: utf-8 -*-

def classify_review(text, positive_words, negative_words, neutral_words):
    
    text_lower = str(text).lower()
    if any(word in text_lower for word in positive_words):
        return 'Positive'
    elif any(word in text_lower for word in negative_words):
        return 'Negative'
    elif any(word in text_lower for word in neutral_words):
        return 'Neutral'

def classify_reviews(df):
   
    positive_words = ["great", "good", "love", "best", "always"]
    negative_words = ["worst", "not", "bad", "terrible", "never", "garbage"]
    neutral_words = ["amazon","service", "customer", "order", "prime"]
    
    df['Sentiment_Title'] = df['Review Title'].apply(classify_review, args=(positive_words, negative_words, neutral_words))
    df['Sentiment_Text'] = df['Review Text'].apply(classify_review, args=(positive_words, negative_words, neutral_words))
    
    return df
