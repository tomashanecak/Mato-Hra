import pygame, sys
from settings import *
from assets import assets
from block import Block
from coin import Coin
from player import Player
from game_map import *

class World:
    def __init__(self, level_data, screen):
        
        self.screen = screen

        self.world_shift = 0

        self.sky_surf = pygame.image.load(assets["sky"]).convert_alpha()
        self.sky_surf = pygame.transform.scale(self.sky_surf, (width, height))
        self.sky_rect = self.sky_surf.get_rect(midbottom = (width/2, height))

        self.setup_level(level_data)
    
    def setup_level(self, level_map):
        self.blocks = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_i, row in enumerate(level_map):
            for col_i, col in enumerate(row):
                if col == "x":
                    x = col_i * block_size
                    y = row_i * block_size
                    block= Block((x,y), block_size)
                    self.blocks.add(block)
                if col == "c":
                    x = col_i * block_size
                    y = row_i * block_size
                    coin = Coin((x,y), block_size)
                    self.coins.add(coin)
                if col == "p":
                    x = col_i * block_size
                    y = row_i * block_size
                    player_s = Player((x,y), block_size)
                    self.player.add(player_s)

    def move_cam(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < (width / 4) and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > ((width/4) * 3) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8
    
    # def horizontal_collision(self):
    #     player = self.player.sprite

    #     player.rect.x += player.direction.x * player.speed

    #     for sprite in self.blocks.sprites():
    #         if sprite.rect.colliderect(player.rect):
    #             if player.direction.x < 0:
    #                 player.rect.left = sprite.rect.right
    #             elif player.direction.x > 0:
    #                 player.rect.right = sprite.rect.left
    
    # def vertical_collision(self):
    #     player = self.player.sprite

    #     player.phisics()

    #     for sprite in self.blocks.sprites():
    #         if sprite.rect.colliderect(player.rect):
    #             if player.direction.y > 0:
    #                 player.rect.bottom = sprite.rect.top
    #                 player.direction.y = 0
    #             elif player.direction.y < 0:
    #                 player.rect.top = sprite.rect.bottom
    #                 player.direction.y = 0

    def get_collisions(self):
        player = self.player.sprite

        hits = []
        for sprite in self.blocks.sprites():
            if sprite.rect.colliderect(player.rect):
                hits.append(sprite)
        return hits
    
    def horizontal_collision(self):
        player = self.player.sprite

        player.rect.x += player.direction.x * player.speed

        collisions = self.get_collisions()
        for tile in collisions:
            if player.direction.x > 0:
                player.rect.x = tile.rect.left - player.rect.width

                # DONE Fix Bug - If player hits wall while jumping block further movement
                if player.direction.y > 0:
                    player.block_movement = True
            if player.direction.x < 0:
                player.rect.x = tile.rect.right

                # DONE Fix Bug - If player hits wall while jumping block further movement
                if player.direction.y > 0:
                    player.block_movement = True
    
    def vertical_collision(self):
        player = self.player.sprite

        player.phisics()

        collisions = self.get_collisions()

        for tile in collisions:
            if player.direction.y > 0:
                player.direction.y = 0
                player.rect.bottom = tile.rect.top

                # DONE Fix Bug - Unblock the movement when player lands
                player.block_movement = False
            elif player.direction.y < 0:
                player.direction.y = 0
                player.rect.bottom = tile.rect.bottom + player.rect.height
                player.block_movement = True

    def check_coin_collision(self):
        collided_coins = pygame.sprite.spritecollide(self.player.sprite,self.coins,True)

        


    def display(self):
        self.screen.blit(self.sky_surf, self.sky_rect)
        self.blocks.update(self.world_shift)
        self.blocks.draw(self.screen)
        self.coins.update(self.world_shift)
        self.coins.draw(self.screen)
        self.move_cam()

        self.player.update()
        self.horizontal_collision()
        self.vertical_collision()
        self.player.draw(self.screen)

        self.check_coin_collision()
        
        