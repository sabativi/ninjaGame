# !/usr/bin/env python
# -*- coding: utf-8 *-*
import time
import random
import pygame

import level
import projectile
import game
import surface_manager
from utile import *
from config import *

class Enemy(pygame.sprite.DirtySprite):

    """
    attributes :
        display : the current working surface
        image : the image of the enemy
        rect : the bounded rect of the enemy,allows to know exactly what
                    size of the screen we should refresh
        pos_x : the x-position of the enemy
        pos_y : the y-position of the enemy
        velx : the x-speed of the enemy
        vely : the y-speed of the enemy
        is_hit : boolean to know if the enemy was hitten
        hit_sound : the sound to play in the case it was hitten
        dirty : the rendering is dependent on this flag,
                         see pygame.sprite.DirtySprite for more explanation
    """

    def __init__(self):
        super(Enemy, self).__init__()
        # INFO : get working surface
        self.display = pygame.display.get_surface()
        enemy_sprite = load_image(getEnemyFrame(1))
        # INFO : flip the image so that the enemy looks at the player
        self.image = pygame.transform.flip(enemy_sprite, True, False)
        self.rect = self.image.get_rect()
        paths = [[1000, -128, -12, 12], [1000, self.display.get_height()+128, -12, -12]]
        ## INFO : we choose a speed and a position for the current Enemy
        ## between the two choices in paths
        ## TODO : change to a random choice
        self.pos_x, self.pos_y, self.velx, self.vely = random.choice(paths)
        self.is_hit = False
        self.hit_sound = load_sound(getEnemyHitSound())
        self.dirty = 1

    def update(self):
        ## TODO : apparently an enemy will always come from two directions
        ## the shuriken of the player is only able to throw in one direction
        if self.pos_x < 0 - self.rect.width:
            surface_manager.remove(self)

        self.check_if_hit()

        if self.is_hit:
            self.pos_y += 10
            if self.pos_y >= self.display.get_height():
                surface_manager.remove(self)
        else:
            self.pos_x += self.velx
            self.pos_y += self.vely

        self.rect.topleft = (self.pos_x, self.pos_y)
        self.dirty = 1


    def check_if_hit(self):
        if self.is_hit:
            return

        collidelist = pygame.sprite.spritecollide(self,
                                surface_manager.surface_list, False)

        for item in collidelist:
            if type(item) is projectile.Projectile:
                surface_manager.remove(item)
                self.is_hit = True
                self.image = pygame.transform.flip(self.image, False, True)
                self.hit_sound.play()
                game.update_score()
