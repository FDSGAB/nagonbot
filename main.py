import os
#from training import *
from functions.basic_sentence_functions import Sentence
from functions.voice import Voice
from kokoro.json_reader import Json_Reader
from model import Model
import logging
from sound import BGM

class Main():

    bgm_switch = False
    bgm_is_playing = False

    def __init__(self):
        os.environ['WDM_LOG'] = "false"
        logging.getLogger('WDM').setLevel(logging.NOTSET)
        json_file = Json_Reader()
        model = Model()
        sentence = Sentence()
        os.system('cls')
        voice = Voice()
        return self.main(json_file,model,sentence,voice)

    def main(self,json_file,model,sentence,voice):        
        while True:
            if self.bgm_is_playing == False:
                BGM().play_song(self.bgm_switch)
                if self.bgm_switch == True:
                    self.bgm_is_playing = True
            message = input("\n自分:\n")
            ints = sentence.predict_class(message, model.model, model.classes, json_file.tagger, model.words)
            response = sentence.get_response(voice, ints, json_file.kokoro)
            voice.voice_answer(response)
            if ints[0]['koko']  in ["さようなら" , "寝るさようなら"]:
                break
            if ints[0]['koko'] == "BGM_ON":
                if self.bgm_switch == False:
                    self.bgm_switch = True
            if ints[0]['koko'] == "BGM_OFF":
                if self.bgm_switch == True:
                    self.bgm_switch = False
                    if self.bgm_is_playing:
                        self.bgm_is_playing = False

if __name__ == '__main__':
    Main()
    