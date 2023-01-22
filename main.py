import os
from renshuu import *                               #Executa o arquivo de ML por completo
from functions.basic_sentence_functions import Sentence
from functions.voice import Voice
from kokoro.kokorowoyomu import Json_Reader
from model import Model
import logging


#pre-setup
os.environ['WDM_LOG'] = "false"
logging.getLogger('WDM').setLevel(logging.NOTSET)
json_file = Json_Reader()
model = Model()
sentence = Sentence()
os.system('cls')
koe = Voice()

#Loop principal para o funcionamento do chatbot com opção de desligá-lo　se a tag for de despedida
def main():
    while True:
        message = input("\n自分:\n")
        ints = sentence.predict_class(message, model.model, model.classes, json_file.tagger, model.words)
        response = sentence.get_response(koe, ints, json_file.kokoro)
        koe.voice_answer(response)
        if ints[0]['koko']  in ["さようなら" , "寝るさようなら"]:
            break

if __name__ == '__main__':
    main() 