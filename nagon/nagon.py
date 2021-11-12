import os
import random
import json
import pickle
import numpy 

import nltk 
from nltk.corpus import knbc                #Japanese language import
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

from pathlib import Path

#Aqui eu utilizei essas funções path para pegar o endereço do JSON poder usar na open()
data_folder = Path("D:/REP_programas_Python/NagonBot.py/kokoro JSON/")
file_to_open = data_folder / "kokoro.json"


#Abre o arquivo JSON, o enconding="utf8" é necessário por conta dos caracteres japoneses
kokoro = json.loads(open(file_to_open, encoding="utf8").read()) #Recebe o arquivo em JSON como, essencialmente, um dicionário em Python


documents = pickle.load(open('documents.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('nagonmodel.h5')

def clean_up_sentece(sentence):
    return sentence

def bag_of_words(sentence):
    sentence_words = clean_up_sentece(sentence)
    bag = [0] * len(sentence)
    i = 0
    for w in sentence_words:
        if sentence_words == sentence:
            bag[i] = 1
            i = i + 1
    return numpy.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(numpy.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'kokoro': classes[r[0]], 'probability': str(r[1])})
    return return_list


def get_response(kokoro_list, kokoro_json):
    tag = kokoro_list[0]['kokoro']
    list_of_kokoro = kokoro_json['kokoro']
    for i in list_of_kokoro:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result
print("ナゴンが起きた！")

while True:
    message = input("")
    ints = predict_class(message)
    res = get_response(ints, kokoro)
    print(res)
"""
**************************NAO FUNCIONA**************************

"""