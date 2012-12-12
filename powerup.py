import pygame
import random

import game
import player
import level
import surface_manager
from utile import *
from config import *

class PowerUp(pygame.sprite.DirtySprite):
    """
    attributes
        display
        dirty
        image
        rect
        pos_x
        pos_y
        bonus_sound
    """
    def __init__(self, img):
        super(PowerUp, self).__init__()
        self.display = pygame.display.get_surface()
        self.image = load_image(img)
        self.rect = pygame.Rect((0, 0), (self.image.get_width(), self.image.get_height()))
        self.pos_x = self.display.get_width()
        self.pos_y = random.randint(150, 400)
        self.bonus_sound = load_sound(getPowerUpBonusSound())
        self.dirty = 1

    def is_consumed(self):
        collidelist = pygame.sprite.spritecollide(self, surface_manager.surface_list, False)

        for item in collidelist:
            if type(item) is player.Player:
                return True

        return False

    def moveRight(self):
        self.pos_x -= 12

    def moveLeft(self):
        self.pos_x += 12

class ShurikenPU(PowerUp):

    def __init__(self):
        super(ShurikenPU, self).__init__(getPowerUpShirukenImage())

    def update(self):
        if self.pos_x < 0 - self.rect.width:
            surface_manager.remove(self)

        if self.is_consumed():
            self.add_bonus()
            surface_manager.remove(self)

       # self.pos_x -= 12

        self.rect.topleft = (self.pos_x, self.pos_y)
        self.dirty = 1

    def add_bonus(self):
        self.bonus_sound.play()
        game.Game.player.shurikens += 50
