# !/usr/bin/env python
# -*- coding: utf-8 *-*

# Import modules
import os
import sys

from config import *
# Import pygame module, check if it exists
try:
    import pygame
except ImportError:
    sys.exit("pygame library must be installed, go to"+\
                "http://www.pygame.org/download.shtml")
from pygame.locals import *
from pygame.compat import *
"""
In case of no font or no sound, we only provide a Warning, the code provides
a way to not raise Error while nothing is available
"""
if not pygame.font:
    print "Warning, fonts disabled"
if not pygame.mixer:
    print "Warning, sound disabled"

"""
This function loads an image in the data directory with the choosen name
You can add a colorKey function which will find any pixel in the image
with the same value as colorKey and make them fully transparent. So that you
do not have background in your image
"""
def load_image(name,colorKey=None):
    fullname=os.path.join(getImageDir(),name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print "cannot load image :%s", fullname
        raise SystemExit(str(geterror()))
    if image.get_alpha():
        image=image.convert_alpha()
    else:
        image=image.convert()
        if colorKey is not None:
            if colorKey is -1:
                colorKey = image.get_at((0,0))
            image.set_colorkey(colorKey,RLEACCEL)
    return image

"""
This function loads a sound file in the data directory with the choosen name
"""
def load_sound(name):
    class NoneSound:
        def play(self):
            pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname=os.path.join(getSoundDir(),name)
    try:
        sound=pygame.mixer.Sound(fullname)
    except pygame.error:
        print "cannot load sound: %s",fullname
    return sound


"""
This function loads a font file in the data directory with the choosen name
"""
def load_font(name,size):
    class NoneFont:
        def render(self):
            pass
    if not pygame.font or not pygame.font.get_init():
        return NoneFont()
    fullname=os.path.join(getFontDir(),name)
    try:
        font = pygame.font.Font(fullname,size)
    except pygame.error:
        print "cannot load font: %s",fullname
    return font
