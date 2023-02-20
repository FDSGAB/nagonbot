import random
import pygame
import os

class BGM():

    sound_directory = "./nagonbot/bin/data/sound/"
    bgm_list = []
    current_song = "./nagonbot/bin/data/sound/monstruo.wav"
    bgm_switch = False

    def __init__(self):
        self.bgm_list = os.listdir('./nagonbot/bin/data/sound')
    
    def pick_song(self):
        picked_random_number = random.randint(0, len(self.bgm_list)-1)
        song_name = self.bgm_list[picked_random_number]
        print("\n曲:", song_name)
        self.current_song = self.sound_directory + self.bgm_list[picked_random_number]


    def play_song(self, switch: bool):
        if switch == True and self.bgm_switch == True:
            return
        self.bgm_switch = switch
        if self.bgm_switch:
            self.pick_song()
            pygame.init()
            pygame.mixer.init(44100,-16,2,512)
            sound = pygame.mixer.Sound(self.current_song)
            sound.set_volume(0.034)
            sound.play(loops=-1)
        else:
            pygame.init()
            pygame.mixer.init(44100,-16,2,512)
            sound = pygame.mixer.Sound(self.current_song)
            sound.set_volume(0.034)
            sound = pygame.mixer.pause()


if __name__ == "__main__":
    """ bgm_switch = False

    while True:
        BGM().play_song(bgm_switch)
        switch = input("Turn on switch? (y/n) \n")
        if switch == "y":
            bgm_switch = True
        else:
            bgm_switch = False
     """
    print(os.listdir('./nagonbot/bin/data/sound'))







