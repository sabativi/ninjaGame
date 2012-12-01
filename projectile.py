import pygame
import level
import surface_manager
import math
from config import *
from utile import *

class Projectile(pygame.sprite.DirtySprite):
    def __init__(self, player):
        super(Projectile, self).__init__()
        self.display = pygame.display.get_surface()
        self.image = load_image(getProjectileImage())
        self.rect = pygame.Rect((0, 0), (self.image.get_width(), self.image.get_height()))
        self.pos_x = player.pos_x + self.image.get_width()
        self.pos_y = player.pos_y + 50
        mouse_pos_x,mouse_pos_y = pygame.mouse.get_pos()
        self.angle = math.atan2(float(mouse_pos_y-self.pos_y),(mouse_pos_x-self.pos_x))
        ## NOTE : we can choose the velocity of the shuriken
        self.velocity = 8
        self.dirty = 1

    def update(self):
        if self.pos_x > self.display.get_width():
            surface_manager.remove(self)
        self.pos_x += math.cos(self.angle)*self.velocity
        self.pos_y += math.sin(self.angle)*self.velocity

        self.rect.topleft = (self.pos_x, self.pos_y)
        self.dirty = 1
