import os
#from renshuu import *                               #Executa o arquivo de ML por completo
from functions.basic_sentence_functions import Sentence
from functions.voice import Voice
from kokoro.kokorowoyomu import Json_Reader
from model import Model


json_file = Json_Reader()
model = Model()
sentence = Sentence()
os.system('cls')
koe = Voice()



#Loop principal para o funcionamento do chatbot com opção de desligá-lo　se a tag for de despedida
while True:
    message = input("\n自分:\n")
    ints = sentence.predict_class(message, model.model, model.classes, json_file.tagger, model.words)
    res = sentence.get_response(koe,ints, json_file.kokoro)
    koe.voice_answer(res)
    if ints[0]['koko']  in ["さようなら" , "寝るさようなら"]:
        break