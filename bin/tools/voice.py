from gtts import gTTS
import os
from playsound import playsound
import random

class Voice():

    greetings_list = ['ハローワールド', 'わ、起きちゃった']

    def __repr__(self):
        return "TTS class that is configurated to use google translate's japanese voice as the default voice."

    def start(self):
        picked_random_number = random.randint(0, len(self.greetings_list)-1)
        greeting = self.greetings_list[picked_random_number]
        print("\nナゴン:\n" + greeting)
        self.say(greeting)

    def say(self, message):
        my_aud = gTTS(text = message, lang = 'ja') #converts the text into speech
        my_aud.save('./bin/temp/demo.mp3') #save the file with .mp3 extension
        playsound(sound = './bin/temp/demo.mp3', block = True) #to play it
        os.remove('./bin/temp/demo.mp3')

    def voice_answer(self, answer: str):
        print("\nナゴン:\n" + answer)
        self.say(answer)
