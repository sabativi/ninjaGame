import pygame
import random
import state
import level
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
    def __init__(self, img_location):
        super(Platform, self).__init__()
        self.display = pygame.display.get_surface()
        self.surface_manager = surface_manager
        self.image = load_image(img_location)
        ## NOTE : it is here that we can choose the size of the plaform
        ## TODO : change this
        self.image = pygame.transform.scale(self.image,
            (random.randint(500, 1000), self.image.get_height()))
        self.rect = pygame.Rect(0, 0, self.image.get_width(), self.image.get_height())
        ## position of the platform
        self.pos_x = self.display.get_width()
        self.pos_y = random.randint(self.display.get_height() - self.rect.height*5,
            self.display.get_height() - self.rect.height)

    def update(self):
        if self.pos_x < 0 - self.rect.width:
            surface_manager.remove(self)
            return
        else:
            self.pos_x -= 12
            self.rect.topleft = (self.pos_x, self.pos_y)


## NOTE : the first platform can not have a small size, that is why we write
## an other class

## NOTE : should we use an attribute to specify if it is the first platform ?
class StartingPlatform(pygame.sprite.Sprite):
    """
    attributes :
        display
        image
        pos_x
        pos_y
        rect
    """
    def __init__(self, img_location):
        super(StartingPlatform, self).__init__()
        self.display = pygame.display.get_surface()
        self.image =  load_image(img_location)
        self.rect = pygame.Rect(0, 0, self.image.get_width(), self.image.get_height())
        self.pos_x = 0
        self.pos_y = self.display.get_height() - 100

    def update(self):
        if self.pos_x < 0 - self.rect.width:
            surface_manager.remove(self)
            return
        else:
           self.pos_x -= 12
           self.rect.topleft = (self.pos_x, self.pos_y)
