import pygame
import random
import surface_manager
from utile import *
from config import *

class Platform(pygame.sprite.Sprite):
    """
    attributes :
        display
        image
        pos_x
        pos_y
        rect
    """
    def __init__(self, img_location,first = False):
        super(Platform, self).__init__()
        self.display = pygame.display.get_surface()
        self.surface_manager = surface_manager
        self.image = load_image(img_location)
        if first:
            ## if this is the first Platform that we create we put a certain size
            self.rect = pygame.Rect(0, 0, self.image.get_width(), self.image.get_height())
            self.pos_x = 0
            self.pos_y = self.display.get_height() - 100
        else:
            ## change the size of the platform here
            self.image = pygame.transform.scale(self.image,
                (random.randint(500, 1000), self.image.get_height()))
            self.rect = pygame.Rect(0, 0, self.image.get_width(), self.image.get_height())
            ## position of the platform
            self.pos_x = self.display.get_width()
            self.pos_y = random.randint(self.display.get_height() - self.rect.height*5,
                self.display.get_height() - self.rect.height)

    def moveRight(self):
        self.pos_x -= getGamePixelMove()

    def moveLeft(self):
        self.pos_x += getGamePixelMove()

    def update(self):
        if self.pos_x < 0 - self.rect.width:
            surface_manager.remove(self)
            return
        else:
            self.rect.topleft = (self.pos_x, self.pos_y)
