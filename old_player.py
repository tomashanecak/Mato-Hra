import pygame, sys
from settings import *
from assets import assets

class Player:
    def __init__(self, screen):

        self.screen = screen

        self.speed = 5
        # self.gravity = 0

        self.isJump = False
        self.jumpCount = 10

        self.player_surf = pygame.image.load(assets["player"]).convert_alpha()
        self.player_surf = pygame.transform.scale(self.player_surf, (50,50))
        self.player_rect = self.player_surf.get_rect(midbottom = (100, 550))

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.move("move_right")
        elif keys[pygame.K_LEFT]:
            self.move("move_left")
        elif keys[pygame.K_SPACE]:
            self.move("jump")

    def move(self, action):
        if action == "move_right":
            self.player_rect.x += self.speed
        elif action == "move_left":
            self.player_rect.x -= self.speed
        elif action == "jump":
            self.isJump = True

    # def phisics(self):
    #     if self.player_rect.colliderect(self.collidable_objects):
    #         self.player_rect.bottom = self.collidable_objects.top + 100

    #     ## Implement gravity for jumping (PHYSICS)
    #     self.gravity += 1
    #     self.player_rect.y += self.gravity

    def jump(self):
        # Check if mario is jumping and then execute the
        # jumping code.
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= self.jumpCount**2 * 0.1 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10
            

    def display(self):
        # self.phisics()
        self.input()
        self.jump()
        self.screen.blit(self.player_surf, self.player_rect)

    