import pygame,sys
from settings import *
from game_map import *
from assets import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(assets["player"]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (size, size))

        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2(0,0)
        self.speed = player_speed
        self.gravity = gravity
        self.jump_height = jump_height
        self.jump_is_active = False
        self.block_movement = False

    def input(self):
        keys = pygame.key.get_pressed()

        if self.block_movement == False:
            if keys[pygame.K_RIGHT]:
                self.direction.x = 1
            elif keys[pygame.K_LEFT]:
                self.direction.x = -1
            else:
                self.direction.x = 0

            if keys[pygame.K_SPACE]:
                if self.direction.y == 0 and self.jump_is_active != True:
                    self.jump_is_active = True
                    self.jump()
            else: 
                self.jump_is_active = False
        else:
            self.direction.x = 0

    def phisics(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    
    def jump(self):
        self.direction.y = self.jump_height
    
    def update(self):
        self.input()
        self.rect.x += self.direction.x * self.speed
        self.phisics()
