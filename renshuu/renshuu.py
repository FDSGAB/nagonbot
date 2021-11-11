import os
import random
import json
import pickle
import numpy 

import nltk 
from nltk.corpus import knbc                #Japanese language import
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

from pathlib import Path

#Aqui eu utilizei essas funções path para pegar o endereço do JSON poder usar na open()
data_folder = Path("D:/REP_programas_Python/NagonBot.py/kokoro JSON/")
file_to_open = data_folder / "kokoro.json"


#Abre o arquivo JSON, o enconding="utf8" é necessário por conta dos caracteres japoneses
kokoro = json.loads(open(file_to_open, encoding="utf8").read()) #Recebe o arquivo em JSON como, essencialmente, um dicionário em Python


#Cria as listas de controle 
words = []              #Palavras que serão utilizadas
classes = []            #Classes que serão utilizadas
documents = []          #Combinações 'pertences'
ignore_letters = ['。', '、', '！', '？', '「', '」']   #Caracteres que serão ignorados



for koko in kokoro['kokoro']:                   
    for pattern in koko['patterns']:
        #word_list = nltk.word_tokenize(pattern, language='japanese')    #ERRO AQUIII
        #word_list = knbc.words(pattern)                                 #tokenize e knbc n funcionam, procurar mais sobre depois :/
        word_list = pattern
        words.append(word_list)
        documents.append((word_list, koko['tag']))
        if koko['tag'] not in classes:
            classes.append(koko['tag'])

print(documents)