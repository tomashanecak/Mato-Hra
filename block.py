import pygame,sys
from settings import *
from game_map import *
from assets import *

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(assets["block"]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (size, size))

        self.rect = self.image.get_rect(topleft = pos)

    def update(self, shift_amount):
        self.rect.x += shift_amount


