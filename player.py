# !/usr/bin/env python
# -*- coding: utf-8 *-*

import time
import pygame
from pygame.locals import *

import level
import projectile
import enemy
import platform
import powerup
import surface_manager
from config import *
from utile import *

class Player(pygame.sprite.DirtySprite):

    """
    attributes :
        display : the current working surface
        frame_set : a set a frame reprensenting the ninja in different positions
        current_frame : the current frame displayed
        timer : a timer
        image : the pygame image object corresponding to the current frame
        rect : the bounded rect
        pos_x : the x-position of the player
        pos_y : the y-position of the player
        is_jumping : boolean to know if the player is jumping
        max_jump_height : the highest jump that the player can do
        current_jump : ??
        is_falling : boolean to know if the player is falling
        shurikens : the number of shurikens that the player gets
        throw_sound : the sound to play when player throws a shuriken
        dirty :
    """

    def __init__(self):
        super(Player, self).__init__()
        self.display = pygame.display.get_surface()
        frame_1 = load_image(getPlayerFrame(1))
        frame_2 = load_image(getPlayerFrame(2))
        frame_3 = load_image(getPlayerFrame(3))
        self.frame_set = [frame_1, frame_2, frame_3, frame_2]
        self.current_frame = 0
        self.timer = time.clock()
        self.image = self.frame_set[self.current_frame]
        self.rect = self.image.get_rect()
        self.pos_x = 0
        self.pos_y = self.display.get_height() - (100 + self.rect.height)
        self.is_jumping = False
        self.max_jump_height = 256
        self.current_jump = 0
        self.is_falling = True
        self.shurikens = 50
        self.throw_sound = load_sound(getThrowSound())

        ## TODO : change this, this is awful
        self.first = True

    ## this function is here for the first moment of the game
    ## TODO : choose a good starting point not 300
    def startGame(self):
        self.pos_x += 10

        self.current_frame = (self.current_frame + 1)  % getNumberFramePlayer()
        self.image = self.frame_set[self.current_frame]

        self.dirty = 1
        ## we update the current rect by only updating the lefttop point
        self.rect.topleft = (self.pos_x, self.pos_y)

    def update(self):
        ## NOTE : we go to the next position if we have waited more
        ## than .05 s and we are not jumping
        
        if self.first:
            while self.pos_x < 100:
                self.startGame()
            self.first = False

        if time.clock() >= self.timer + .001 and not self.is_jumping:
            self.current_frame = (self.current_frame + 1)  % getNumberFramePlayer()
            self.image = self.frame_set[self.current_frame]
            self.timer = time.clock()

        if self.on_platform():
            self.is_jumping = False
            self.is_falling = False
            self.current_jump = 0

        if self.is_falling:
            self.pos_y += 8

        self.dirty = 1
        ## we update the current rect by only updating the lefttop point
        self.rect.topleft = (self.pos_x, self.pos_y)

    def jump(self):
        if self.current_jump <= self.max_jump_height and not self.is_falling:
            self.is_jumping = True
            self.current_frame = 0
            self.image = self.frame_set[self.current_frame]
            self.pos_y -= 10
            self.dirty = 1
            self.current_jump += 10
            if self.current_jump >= self.max_jump_height:
                self.is_falling = True

    def stop_jumping(self):
        self.jumping = False
        self.is_falling = True

    def throw_shuriken(self):
        if self.shurikens > 0:
            self.throw_sound.play()
            surface_manager.add(projectile.Projectile(self))
            self.shurikens -= 1

    ## check if you are on platform
    def on_platform(self):
        collidelist = pygame.sprite.spritecollide(self,surface_manager.surface_list, False)

        for item in collidelist:
            if type(item) is enemy.Enemy:
                continue
            if type(item) is platform.Platform or \
                type(item) is platform.StartingPlatform:
                if (self.pos_y + self.rect.height) <= (item.pos_y + 8) and\
                    (self.pos_x + self.rect.width) >= item.pos_x:
                    return True
        return False
