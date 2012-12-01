# !/usr/bin/env python
# -*- coding: utf-8 *-*
import sys
import pygame
from pygame.locals import *

import state
import game
import surface_manager
from utile import *
from config import *
from color import *

class Title(state.State):
    """
    attributes:
        display
        background
        font_manager
        help_font_manager
        title_font_manager
        title
        title_rect
        title_color
        start_game
        start_game_rect
        help
        help_rect
        help_image
        help_image_rect
        exit_game
        exit_game_rect
        current_choice
        show_help
        timer
        music
    """
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.background = load_image(getTitleBackground())
        self.font_manager = load_font(getTitleFont(),getTitleFontSize())
        self.help_font_manager = load_font(getTitleHelpFont(),getTitleHelpFontSize())
        self.title_font_manager = load_font(getTitleTitleFont(),getTitleTitleFontSize())

        self.title = self.title_font_manager.render("RUN!", True, whiteColor())
        self.title_rect = pygame.Rect((self.display.get_width()/2 - self.title.get_width()/2,
             self.display.get_height()/2 - self.title.get_height()*2),
                (self.title.get_width(), self.title.get_height()))
        self.title_color = "white"

        self.start_game = self.font_manager.render("START", True, whiteColor())
        self.start_game_rect = pygame.Rect(
            (self.display.get_width()/2 - self.start_game.get_width()/2,
                 self.display.get_height()/2 - self.start_game.get_height()),
                    (self.start_game.get_width(), self.start_game.get_height()))

        self.help = self.font_manager.render("HELP", True, blackColor())
        self.help_rect = pygame.Rect((self.display.get_width()/2 - self.help.get_width()/2,
             self.display.get_height()/2), (self.help.get_width(), self.help.get_height()))

        self.help_image = load_image(getTitleHelpImage())
        self.help_image_rect = pygame.Rect(
            (self.display.get_width()/2 - self.help_image.get_width()/2,
                 self.display.get_height()/2 - self.help_image.get_height()/2),
                      (self.help_image.get_width(), self.help_image.get_height()))

        self.exit_game = self.font_manager.render("EXIT", True, blackColor())
        self.exit_game_rect = pygame.Rect(
            (self.display.get_width()/2 - self.exit_game.get_width()/2,
                 self.display.get_height()/2 + self.exit_game.get_height()),
                    (self.exit_game.get_width(), self.exit_game.get_height()))

        self.current_choice = 1

        self.show_help = False

        self.timer = pygame.time.Clock()

        self.music = load_sound(getTitleSound())
        self.music.play(loops=-1)

    def exit(self):
        self.music.stop()
        self.display.blit(self.background, (0, 0))
        pygame.display.flip()

    def reason(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if self.show_help:
                        self.show_help = False
                    else:
                        if self.current_choice == 1:
                            return game.Game()
                        elif self.current_choice == 2:
                            self.show_help = True
                        elif self.current_choice == 3:
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
            self.display.blit(self.help_image, self.help_image_rect)
        else:
            self.display.blit(self.title, self.title_rect)
            self.display.blit(self.start_game, self.start_game_rect)
            self.display.blit(self.help, self.help_rect)
            self.display.blit(self.exit_game, self.exit_game_rect)

        pygame.display.update()

    def next(self):
        ## TODO : we should define black and white color
        ## NOTE : we could set the next choice randomly
        if self.current_choice == 1:
            self.start_game = self.font_manager.render("START", True, blackColor())
            self.help = self.font_manager.render("HELP", True, whiteColor())
            self.exit_game = self.font_manager.render("EXIT", True,blackColor())
            self.current_choice = 2
        elif self.current_choice == 2:
            self.start_game = self.font_manager.render("START", True, blackColor())
            self.help = self.font_manager.render("HELP", True, blackColor())
            self.exit_game = self.font_manager.render("EXIT", True,whiteColor())
            self.current_choice = 3
        else:
            self.start_game = self.font_manager.render("START", True,whiteColor())
            self.help = self.font_manager.render("HELP", True, blackColor())
            self.exit_game = self.font_manager.render("EXIT", True, blackColor())
            self.current_choice = 1

    def previous(self):
        if self.current_choice == 1:
            self.start_game = self.font_manager.render("START", True, blackColor())
            self.help = self.font_manager.render("HELP", True,blackColor())
            self.exit_game = self.font_manager.render("EXIT", True, whiteColor())
            self.current_choice = 3
        elif self.current_choice == 2:
            self.start_game = self.font_manager.render("START", True, whiteColor())
            self.help = self.font_manager.render("HELP", True, blackColor())
            self.exit_game = self.font_manager.render("EXIT", True,blackColor())
            self.current_choice = 1
        else:
            self.start_game = self.font_manager.render("START", True, blackColor())
            self.help = self.font_manager.render("HELP", True,whiteColor())
            self.exit_game = self.font_manager.render("EXIT", True,blackColor())
            self.current_choice = 2

    def animate_title(self):
        if self.title_color == "white":
            self.title = self.title_font_manager.render("RUN!", True,blackColor())
            self.title_color = "black"
        else:
            self.title = self.title_font_manager.render("RUN!", True,whiteColor())
            self.title_color = "white"

