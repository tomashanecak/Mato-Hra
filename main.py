import pygame, sys
from old_player import Player
from settings import *
from world import World
from game_map import level_map

pygame.init()
screen = pygame.display.set_mode((screen_dimensions))
pygame.display.set_caption(name)
clock = pygame.time.Clock()

world = World(level_map, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    world.display()
    pygame.display.update()
    clock.tick(60)
