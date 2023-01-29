import random
import pygame

class BGM():

    bgm_list = ["./sound/monstruo.wav", "./sound/new_spring.wav", "./sound/お雑煮の香り.wav", "./sound/竜宮城.wav", "./sound/低音忠実性.wav"]
    current_song = "./sound/お雑煮の香り.wav"
    bgm_switch = False

    def start(self):
        self.pick_song()
    
    def pick_song(self):
        picked_random_number = random.randint(0,len(self.bgm_list)-1)
        song_name = self.bgm_list[picked_random_number]
        print("\n曲:", song_name[8:len(song_name)-4])
        self.current_song = self.bgm_list[picked_random_number]


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
    bgm_switch = False

    while True:
        BGM().play_song(bgm_switch)
        switch = input("Turn on switch? (y/n) \n")
        if switch == "y":
            bgm_switch = True
        else:
            bgm_switch = False
    







