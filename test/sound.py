import random
import pygame
import time

class BGM():

    bgm_list = ["./test/monstruo.wav", "./test/new_spring.wav", "./test/お雑煮の香り.wav", "./test/竜宮城.wav", "./test/低音忠実性.wav"]
    current_song = None
    bgm_switch = False

    
    def pick_song(self):
        picked_random_number = random.randint(0,5)
        print("Random Number: ", picked_random_number)
        self.current_song = self.bgm_list[picked_random_number]
        return self.current_song


    def play_song(self, bgm_switch: bool):
        self.pick_song()
        self.bgm_switch = bgm_switch
        while bgm_switch == True:
            self.bgm_switch = bgm_switch
            pygame.init()
            pygame.mixer.init(44100,-16,2,512)
            sound = pygame.mixer.Sound(self.current_song)
            sound.set_volume(0.034)
            sound.play()

bgm = BGM().play_song(True)

time.sleep(5)

bgm = 0






