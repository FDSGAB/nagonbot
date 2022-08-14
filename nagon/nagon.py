import os
import pyttsx3
import random
import json
import pickle
import numpy 

import fugashi
import nltk 
from nltk.corpus import knbc                #Japanese language import
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

from pathlib import Path

from datetime import datetime

#Comandos de texto para voz　(Aqui precisa achar Japones na maquina de destiono, so funciona nessa assim)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[2].id)
engine.setProperty("rate", 135)


tagger = fugashi.Tagger()

#Aqui eu utilizei essas funções path para pegar o endereço do JSON poder usar na open()
data_folder = Path("D:/REP_programas_Python/NagonBot.py/kokoro JSON/")
file_to_open = data_folder / "kokoro.json"


#Abre o arquivo JSON, o enconding="utf8" é necessário por conta dos caracteres japoneses
kokoro = json.loads(open(file_to_open, encoding="utf8").read()) #Recebe o arquivo em JSON como, essencialmente, um dicionário em Python


words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('nagonmodel.h5')


def clean_up_sentece(sentence):
    sentence_words = [word.surface for word in tagger(sentence)]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentece(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return numpy.array(bag)


#Função que tenta acertar a classe da mensagem enviada
def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(numpy.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i, r in enumerate(res) if r > 0.1]      

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'koko': classes[r[0]], 'probability': str(r[1])})
    return return_list


#Funções relacionadas a datas e tempo (retiradas do sistema)
def get_time (n):
    #Caso para devolver o horário
    if n == 0:
        str = "今は" + datetime.now().strftime("%H:%M") + "です。"
    #Caso para devolver a data
    if n == 1: 
        str = "今日は" + datetime.now().strftime("%Y-%m-%d") + "です。"
    #Caso para devolver o nome do dia da semana
    if n == 2:
        str = "ERROR"
        if int(datetime.now().strftime("%w")) == 0:
            str = "今日は日曜日です。"
        if int(datetime.now().strftime("%w")) == 1:
            str = "今日は月曜日です。"
        if int(datetime.now().strftime("%w")) == 2:
            str = "今日は火曜日です。"
        if int(datetime.now().strftime("%w")) == 3:
            str = "今日は水曜日です。"
        if int(datetime.now().strftime("%w")) == 4:
            str = "今日は木曜日です。"
        if int(datetime.now().strftime("%w")) == 5:
            str = "今日は金曜日です。"
        if int(datetime.now().strftime("%w")) == 6:
            str = "今日は土曜日です。"
    return str



#Com base na classe da mensagem prevista, essa função retorna uma resposta adequada
def get_response(kokoro_list, kokoro_json):
    tag = kokoro_list[0]['koko']               
    list_of_kokoro = kokoro_json['kokoro']
    for i in list_of_kokoro:
        if i['tag'] == tag:
            if tag == "時間":
                return get_time(0)
            if tag == "日付":
                return get_time(1)
            if tag == "曜日":
                return get_time(2)
            result = random.choice(i['responses'])
            break
    return result

#Mensagem para avisar que o programa está rodando
engine.say("わ、起きちゃった")
print("わ、起きちゃった")
engine.runAndWait()


#Loop principal para o funcionamento do chatbot com opção de desligá-lo
while True:
    message = input("")
    ints = predict_class(message)
    res = get_response(ints, kokoro)
    engine.say(res)
    print(res)
    engine.runAndWait()
    if message == "オフ":
        break