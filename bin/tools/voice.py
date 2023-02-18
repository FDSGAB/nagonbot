from gtts import gTTS
import os
from playsound import playsound

class Voice():

    def __repr__(self):
        return "TTS class that is configurated to use google translate's japanese voice as the default voice."

    def start2(self):
        print("\nナゴン:\nハローワールド")
        self.say("ハローワールド")
        #print("\nナゴン:\nわ、起きちゃった")
        #self.say("わ、起きちゃった")

    def say(self, message):
        my_aud = gTTS(text = message, lang = 'ja') #converts the text into speech
        my_aud.save('./bin/temp/demo.mp3') #save the file with .mp3 extension
        playsound(sound = './bin/temp/demo.mp3', block = False) #to play it
        os.remove('./bin/temp/demo.mp3')

    def voice_answer(self, answer: str):
        print("\nナゴン:\n" + answer)
        self.say(answer)
