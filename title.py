# !/usr/bin/env python
# -*- coding: utf-8 *-*
import sys
import pygame
from pygame.locals import *

import state
import game
import random
import screen
#import help
import surface_manager
from utile import *
from config import *
from color import *


POS_CENTER = -0.5


class Title(state.State):

    ## TODO : this class is not very clear, we need to factorize things 

    """
    attributes:
        display : the display surface for the title
        background : the background help_image
        font_manager : the font that we use to display
        help_font_manager : the font_manager for the help message
        title_font_manager : 
        title : 
        title_rect :
        title_color :
        start_game : 
        start_game_rect :
        help :
        help_rect :
        help_image :
        help_image_rect :
        exit_game :
        exit_game_rect :
        current_choice :
        show_help :
        timer :
        music : the music plays while waiting on the screen
    """
    def __init__(self,screen):
        self.display = pygame.display.get_surface()

        ## load the background image
        self.screen = screen
        self.background = load_image(getTitleBackground())
        self.background = pygame.transform.scale(self.background,(screen.width,screen.height))
        
        ## load the music and starts playing
        self.music = load_sound(getTitleSound())
        self.music.play(loops=-1)

        ## load font
        self.font_manager = load_font(getTitleFont(),getTitleFontSize())
        self.help_font_manager = load_font(getTitleHelpFont(),getTitleHelpFontSize())
        self.title_font_manager = load_font(getTitleTitleFont(),getTitleTitleFontSize())

        ## replace 1 with the map of choices also 3
        self.current_choice = Choice(1,3)

        ## initialize the menu
        
        self.title = self.title_font_manager.render("RUN!", True, whiteColor())
        self.title_rect = getPygameRect(self.title,self.display,-2)

        self.start_game = self.font_manager.render("START", True, whiteColor())
        self.start_game_rect = getPygameRect(self.start_game,self.display,-1)

        self.help = self.font_manager.render("HELP", True, blackColor())
        self.help_rect = getPygameRect(self.help,self.display,0)

        self.exit_game = self.font_manager.render("EXIT", True, blackColor())
        self.exit_game_rect = getPygameRect(self.exit_game, self.display,1)

        self.help_image = load_image(getTitleHelpImage())
        self.help_image_rect = getPygameRect(self.help_image,self.display,POS_CENTER)

        self.show_help = False

        self.timer = pygame.time.Clock()

       

    def exit(self):
        self.music.stop()
        self.display.blit(self.background, (0, 0))
        pygame.display.flip()


    ## not well define with the help message
    def reason(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_RETURN:
                if self.current_choice.choice == 1:
                    return game.Game(self.screen)
                elif self.current_choice.choice == 2:
                    return Help(self.screen)
                elif self.current_choice.choice == 3:
                    pygame.quit()
                    sys.exit()
                if event.key == K_DOWN:
                    self.next()
                if event.key == K_UP:
                    self.previous()

    def act(self):
        self.timer.tick(40)
        self.animate_title()

        self.display.blit(self.background, (0, 0))

        if self.show_help:
            self.displayHelpMessage()
        else:
            self.display.blit(self.title, self.title_rect)
            self.display.blit(self.start_game, self.start_game_rect)
            self.display.blit(self.help, self.help_rect)
            self.display.blit(self.exit_game, self.exit_game_rect)

        pygame.display.update()

    def next(self):
        self.current_choice.next()
        self.updateMenuColor()      

    def previous(self):
        self.current_choice.prev()
        self.updateMenuColor()

    def animate_title(self):
        color = random.randint(1, 2)
        if color == 1:
            self.title = self.title_font_manager.render("RUN!", True, whiteColor())
        else:
            self.title = self.title_font_manager.render("RUN!", True, blackColor())

    def updateMenuColor(self):
        self.start_game = self.font_manager.render("START", True, self.current_choice.color(1))
        self.help = self.font_manager.render("HELP", True,self.current_choice.color(2))
        self.exit_game = self.font_manager.render("EXIT", True,self.current_choice.color(3))

    def displayHelpMessage(self):
        self.display.blit(self.help_image, self.help_image_rect)



class Choice():

    firstChoice = 1

    def __init__(self,choice,numberOfChoices):
        self.choice = choice
        self.numberOfChoices = numberOfChoices
    def next(self):
        if self.choice == self.numberOfChoices:
            self.choice = Choice.firstChoice
        else:
            self.choice += 1

    def prev(self):
        if self.choice == Choice.firstChoice:
            self.choice = self.numberOfChoices
        else:
            self.choice -= 1

    def color(self,position):
        if self.choice == position:
            return whiteColor()
        return blackColor()


class Help(state.State):

    def __init__(self,screen):
        self.display = pygame.display.get_surface()
        ## load the background image
        self.screen = screen
        self.background = load_image(getHelpBackground())
        self.background = pygame.transform.scale(self.background,(screen.width,screen.height))

        ## load the font to write the text
        self.help_font_manager = load_font(getHelpFont(),getHelpFontSize())
        message = fileToString(getHelpMessage())
        assert message != "" and message != None
        ## TODO :  replace this value
        self.help_message_rect = pygame.Rect((0,0),(500,500))
        self.help_message = render_textrect(message, self.help_font_manager,self.help_message_rect, whiteColor(), (48, 48, 48))

        #self.help_message = self.help_font_manager.render(message,True,whiteColor())
         

    def exit(self):
        pygame.display.flip()


    def reason(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_RETURN:
                return Title(self.screen)

    def act(self):        
        self.display.blit(self.background, (0, 0))
        self.display.blit(self.help_message,self.help_message_rect)
        pygame.display.flip()


def fileToString(name):
    ## get the text
    f = open(name,'r')
    try:
        lines = f.readlines()
    finally:
        f.close()
    message = ""
    for line in lines:
        message += line
    return message