# -*- coding: utf-8 -*-
import pandas as pd
import re

def preprocess_data(file_path):
   
    df = pd.read_csv(file_path, delimiter=',', encoding='utf-8', on_bad_lines='skip')
    

    def convert_rating(rating_text):
        if isinstance(rating_text, str):  
            match = re.search(r'(\d) out of 5 stars', rating_text)
            if match:
                return int(match.group(1))
        return None

    df['Rating'] = df['Rating'].apply(convert_rating)
    df['Review Date'] = pd.to_datetime(df['Review Date'], errors='coerce') 
    
    
    
    return df


