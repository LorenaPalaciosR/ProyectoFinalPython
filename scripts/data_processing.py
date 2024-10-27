# -*- coding: utf-8 -*-
import pandas as pd
import re

def preprocess_data(file_path):
   
    df = pd.read_csv(file_path, delimiter=',', encoding='utf-8', on_bad_lines='skip')  

    
    
    
    return df


