import pandas as pd
import os
import random as rd

BASEDIR = os.getcwd() # Current Path
csv_file = f"{BASEDIR}/wordle/word_list.csv"

def game_settings():
    # yalnızca 5 harfli kelimeler kalsın
    df = pd.read_csv(csv_file)
    df = df[df["Words"].str.len() == 5]
    df.to_csv(csv_file, index=False)



def get_word():
    word_list = pd.read_csv(csv_file) # csv den kelimeleri aldı
    word_list = word_list["Words"].tolist()  # Kelimelerin olduğu liste 
    len_words = len(word_list) # Mevcut kelime sayısı
    word = word_list[rd.randint(0,len_words-1)]
    return word.lower()
