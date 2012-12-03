# !/usr/bin/env python
# -*- coding: utf-8 *-*
import pygame
import random
import time

import state
import game
import platform
import enemy
import powerup
import surface_manager
from utile import *
from config import *

class Level(state.State):
    surface_manager = pygame.sprite.RenderUpdates()
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.current_platforms = []
        self.num_of_platforms = 4
        self.background = load_image(getLevelImage())
        self.display.blit(self.background, (0, 0))
        self.enter()

    def enter(self):
        new_platform = platform.StartingPlatform(getLevelPlatformImage())
        surface_manager.add(new_platform)
        self.current_platforms.append(new_platform)
        self.time_since_last_powerup = time.clock()
        self.time_since_last_enemyspawn = time.clock()

    def exit(self):
        surface_manager.empty()

    def act(self):
        self.check_platforms()

        ## we can choose the distance between the number of platforms
        DISTANCE_BETWEEN_PLATFORM = random.randint(100, 200)
        if (len(self.current_platforms) < self.num_of_platforms) \
            and ((self.current_platforms[-1].pos_x +\
                self.current_platforms[-1].rect.width) \
                <= (self.display.get_width() - DISTANCE_BETWEEN_PLATFORM)):
            new_platform = platform.Platform(getLevelPlatformImage())
            surface_manager.add(new_platform)
            self.current_platforms.append(new_platform)

        ## we can choose the time between two powerups
        TIME_BETWEEN_POWERUP = 1
        if time.clock() >= self.time_since_last_powerup + TIME_BETWEEN_POWERUP:
            surface_manager.add(powerup.ShurikenPU())
            self.time_since_last_powerup = time.clock()

        ## we can choose the time between two ennemies
        TIME_BETWEEN_ENEMY = 0.2
        if time.clock() >= self.time_since_last_enemyspawn + TIME_BETWEEN_ENEMY:
            surface_manager.add(enemy.Enemy())
            self.time_since_last_enemyspawn = time.clock()

    def check_platforms(self):
        for platform in self.current_platforms:
            if not surface_manager.has(platform):
                self.current_platforms.remove(platform)
