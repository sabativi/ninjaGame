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

"""
This function loads a video 
"""

def load_movie(name):
    fullname = os.path.join(getVideoDir(), name)
    try:
        movie = pygame.movie.Movie(fullname)
    except pygame.error:
        print 'cannot load video : ', fullname
    
    return movie

"""
This function return a pygameRect to know where the current surface position is 
inside the backgroundSurface
"""
def getPygameRect(currentSurface,backgroundSurface,position):
    rectWidth = currentSurface.get_width()
    rectHeight = currentSurface.get_height()
    rectLeft = backgroundSurface.get_width()/2-currentSurface.get_width()/2
    rectTop = backgroundSurface.get_height()/2 + currentSurface.get_height()*position
    return pygame.Rect((rectLeft,rectTop),(rectWidth,rectHeight))



"""
I find this piece of code on internet, it helps when you want to display
a text on a multiline
"""


class TextRectException:
    def __init__(self, message = None):
        self.message = message
    def __str__(self):
        return self.message

def render_textrect(string, font, rect, text_color, background_color, justification=0):
    """Returns a surface containing the passed text string, reformatted
    to fit within the given rect, word-wrapping as necessary. The text
    will be anti-aliased.

    Takes the following arguments:

    string - the text you wish to render. \n begins a new line.
    font - a Font object
    rect - a rectstyle giving the size of the surface requested.
    text_color - a three-byte tuple of the rgb value of the
                 text color. ex (0, 0, 0) = BLACK
    background_color - a three-byte tuple of the rgb value of the surface.
    justification - 0 (default) left-justified
                    1 horizontally centered
                    2 right-justified

    Returns the following values:

    Success - a surface object with the text rendered onto it.
    Failure - raises a TextRectException if the text won't fit onto the surface.
    """
    
    final_lines = []

    requested_lines = string.splitlines()

    # Create a series of lines that will fit on the provided
    # rectangle.

    for requested_line in requested_lines:
        if font.size(requested_line)[0] > rect.width:
            words = requested_line.split(' ')
            # if any of our words are too long to fit, return.
            for word in words:
                if font.size(word)[0] >= rect.width:
                    raise TextRectException, "The word " + word + " is too long to fit in the rect passed."
            # Start a new line
            accumulated_line = ""
            for word in words:
                test_line = accumulated_line + word + " "
                # Build the line while the words fit.    
                if font.size(test_line)[0] < rect.width:
                    accumulated_line = test_line
                else:
                    final_lines.append(accumulated_line)
                    accumulated_line = word + " "
            final_lines.append(accumulated_line)
        else:
            final_lines.append(requested_line)

    # Let's try to write the text out on the surface.

    surface = pygame.Surface(rect.size)
    surface.fill(background_color)

    accumulated_height = 0
    for line in final_lines:
        if accumulated_height + font.size(line)[1] >= rect.height:
            raise TextRectException, "Once word-wrapped, the text string was too tall to fit in the rect."
        if line != "":
            tempsurface = font.render(line, 1, text_color)
            if justification == 0:
                surface.blit(tempsurface, (0, accumulated_height))
            elif justification == 1:
                surface.blit(tempsurface, ((rect.width - tempsurface.get_width()) / 2, accumulated_height))
            elif justification == 2:
                surface.blit(tempsurface, (rect.width - tempsurface.get_width(), accumulated_height))
            else:
                raise TextRectException, "Invalid justification argument: " + str(justification)
        accumulated_height += font.size(line)[1]

    return surface
