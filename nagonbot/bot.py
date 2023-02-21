import os
from nagonbot.bin.tools.basic_sentence_functions import Sentence
from nagonbot.bin.tools.voice import Voice
#from nagonbot.bin.tools.bgm import BGM
from nagonbot.bin.training.json_reader import Json_Reader
from nagonbot.bin.training.model import Model
from nagonbot.bin.training.training import ModelTraining
from nagonbot.bin.training.csv_to_json import KokoroUpdaterC
import logging


class Main():

    bgm_switch = False
    bgm_is_playing = False
    outside_run = False

    def __init__(self):
        KokoroUpdaterC()
        model_training = ModelTraining()
        if model_training.outside_run:
            self.outside_run = True
        os.environ['WDM_LOG'] = "false"
        logging.getLogger('WDM').setLevel(logging.NOTSET)
        json_file = Json_Reader()
        model = Model()
        os.system('cls')
        Voice().start()
        return self.main(json_file, model)

    def main(self, json_file, model):        
        while True:
            """ if self.bgm_is_playing == False:
                BGM().play_song(self.bgm_switch)
                if self.bgm_switch == True:
                    self.bgm_is_playing = True """
            message = input("\n自分:\n")
            ints = Sentence().predict_class(message, model.model, model.classes, json_file.tagger, model.words)
            response = Sentence().get_response(ints, json_file.kokoro)
            Voice().voice_answer(response)
            if ints[0]['koko']  in ["さようなら" , "寝るさようなら"]:
                break
            """ if ints[0]['koko'] == "BGM_ON":
                if self.bgm_switch == False:
                    self.bgm_switch = True
            if ints[0]['koko'] == "BGM_OFF":
                if self.bgm_switch == True:
                    self.bgm_switch = False
                    if self.bgm_is_playing:
                        self.bgm_is_playing = False """

if __name__ == '__main__':
    Main()