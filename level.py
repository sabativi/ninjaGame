# !/usr/bin/env python
# -*- coding: utf-8 *-*
import pygame
import random
import time

import state
import platform
import enemy
import powerup
import surface_manager
from utile import *
from config import *

### TODO : do the same as platform for ennemies and powerup

class Level(state.State):
    surface_manager = pygame.sprite.RenderUpdates()
    def __init__(self):
        self.timer = pygame.time.Clock()
        self.display = pygame.display.get_surface()
        self.current_platforms = []
        self.num_of_platforms = 4
        self.background = load_image(getLevelImage())
        self.display.blit(self.background, (0, 0))
        ## create the starting platform
        new_platform = platform.Platform(getLevelPlatformImage(),True)
        surface_manager.add(new_platform)
        self.current_platforms.append(new_platform)
        self.time_since_last_powerup = time.clock()
        self.time_since_last_enemyspawn = time.clock()
        self.bonus = None

    def exit(self):
        surface_manager.empty()

    def act(self):
        self.timer.tick(60)
        self.check_platforms()

        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.movePlatformsLeft()
            if self.bonus != None:
                self.moveShirukenPULeft()
        elif keys[K_RIGHT]:
            self.movePlatformsRight()
            if self.bonus != None:
                self.moveShirukenPURight()
                

        ## we can choose the distance between the number of platforms
        if self.weShouldAddPlatform():
            new_platform = platform.Platform(getLevelPlatformImage())
            surface_manager.add(new_platform)
            self.current_platforms.append(new_platform)
       
        if self.weShouldAddPowerUp():
            self.bonus = powerup.ShurikenPU()
            surface_manager.add(self.bonus)
            self.time_since_last_powerup = time.clock()

        if self.weShouldAddEnemy():
            self.ennemies = enemy.Enemy()
            surface_manager.add(self.ennemies)
            self.time_since_last_enemyspawn = time.clock()

    """
    check if the platform is still on the screen
    otherwise delete it
    """
    def check_platforms(self):
        for platform in self.current_platforms:
            if not surface_manager.has(platform):
                self.current_platforms.remove(platform)

    """
    move all the current platforms to the left
    """
    def movePlatformsRight(self):
        ## si la position du joueur est 
        for platform in self.current_platforms:
            platform.moveRight()

    """
    move all the current platforms
    """
    def movePlatformsLeft(self):
        for platform in self.current_platforms:
            platform.moveLeft()

    def moveShirukenPULeft(self):
        self.bonus.moveLeft()

    def moveShirukenPURight(self):
        self.bonus.moveRight()

    #################################################################################
    # these are functions that are only used to make main function cleaner ##########

    """
    Return a bool to know if a new Platform should be constructed
    """
    def weShouldAddPlatform(self):
        ## we can choose the distance between platforms
        DISTANCE_BETWEEN_PLATFORM = random.randint(100, 200)
        if (len(self.current_platforms) < self.num_of_platforms) \
             and ((self.current_platforms[-1].pos_x +\
                 self.current_platforms[-1].rect.width) \
                 <= (self.display.get_width() - DISTANCE_BETWEEN_PLATFORM)):
            return True
        return False

    """
    Return a bool to know if a new PowerUp should be displayed
    """
    def weShouldAddPowerUp(self):
        ## we can choose the time between two powerups
        TIME_BETWEEN_POWERUP = 1
        if time.clock() >= self.time_since_last_powerup + TIME_BETWEEN_POWERUP:
            return True
        return False
        

    """
    Return a bool to know if a new Ennemy should be displayed
    """
    def weShouldAddEnemy(self):
        ## we can choose the time between two ennemies
        TIME_BETWEEN_ENEMY = 0.2
        if time.clock() >= self.time_since_last_enemyspawn + TIME_BETWEEN_ENEMY:
            return True
        return False
