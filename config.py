import pygame
import os
from sound import Sound


class Config:

    def __init__(self):
        self.landed = Sound(os.path.join(f'assets/sounds/piece_land.wav'))
        self.row_complete = Sound(os.path.join(f'assets/sounds/row_complete.wav'))
        self.level_up = Sound(os.path.join(f'assets/sounds/level_up.wav'))

    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(f'assets/sounds/music.wav'))
        pygame.mixer.music.set_volume(.2)
        pygame.mixer.music.play(-1)



