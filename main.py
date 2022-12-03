import os
import json
import pickle
import numpy 

import fugashi
from functions.function_selector import selector
#from renshuu import *                               #Executa o arquivo de ML por completo
from functions import voice

from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

from pathlib import Path

#Vai ser utilizado para separas as palavras em japonês nos padrões
tagger = fugashi.Tagger()

#Aqui eu utilizei essas funções path para pegar o endereço do JSON poder usar na open()
data_folder = Path("D:/REP_programas_Python/nagonbot/kokoro JSON/")
file_to_open = data_folder / "kokoro.json"


#Abre o arquivo JSON, o enconding="utf8" é necessário por conta dos caracteres japoneses
kokoro = json.loads(open(file_to_open, encoding="utf8").read()) #Recebe o arquivo em JSON como, essencialmente, um dicionário em Python


words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('nagonmodel.h5')
os.system('cls')


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

#Com base na classe da mensagem prevista, essa função retorna uma resposta adequada
def get_response(kokoro_list, kokoro_json):
    tag = kokoro_list[0]['koko']               
    list_of_kokoro = kokoro_json['kokoro']
    for i in list_of_kokoro:
        if i['tag'] == tag:
            return selector.select(tag,koe,i)

koe = voice()


#Loop principal para o funcionamento do chatbot com opção de desligá-lo　se a tag for de despedida
while True:
    message = input("\n自分:\n")
    ints = predict_class(message)
    res = get_response(ints, kokoro)
    koe.voice_answer(res)
    if ints[0]['koko']  in ["さようなら" , "寝るさようなら"]:
        break