# !/usr/bin/env python
# -*- coding: utf-8 *-*

import pygame
from pygame.locals import *

import state
import surface_manager
import title
import hud
from utile import *
from config import *
from color import *


class HighScoresFile():

    def __init__(self):
        self.filename = getHighScoresFile()

    def createHighScoresFile(self):
        f = open(self.filename,'w')
        f.write('')
        f.close()

    def getBestScores(self):
        if os.path.isfile(self.filename):
            f = open(self.filename,'r')
            stringBuffer = f.read()
            listScores = stringBuffer.split(';')
            listScores.remove('')
            for i,elem in enumerate(listScores):
                listScores[i]=int(listScores[i])
            return listScores
        else:
            self.createHighScoresFile()
            return []

    def writeNewScores(self,high_scores):
        f = open(self.filename,'w')
        stringToWrite=''
        for score in high_scores:
            if score != "":
                stringToWrite+=str(score)+';'
        f.write(stringToWrite)
        f.close()


class HighScores(state.State):
    """
    attributes:
        display : the current working surface
        background : the background image
        header_manager : the title score
        header
        header_rect
        font_manager : the font used to display scores
        music : the music while displaying the HighScores windows
    """
    high_scores = []
    def __init__(self,score):
        self.display = pygame.display.get_surface()
        displayWidth = self.display.get_width()
        displayHeight = self.display.get_height()
        self.background = load_image(getHighScoresImage())
        self.background = pygame.transform.scale(self.background,(displayWidth,displayHeight))

        high_score_file = HighScoresFile()
        HighScores.high_scores = high_score_file.getBestScores()

        HighScores.high_scores.append(score)

        HighScores.high_scores=sorted(HighScores.high_scores,reverse=True)

        if len(HighScores.high_scores) > 10:
            del HighScores.high_scores[10:]

        high_score_file.writeNewScores(HighScores.high_scores)

        self.header_manager = load_font(getHighScoresHeaderManagerFont(),
                                        getHighScoresHeaderManagerFontSize())
        self.header = self.header_manager.render("YOUR SCORES:%d"% hud.Hud.game.score, True, (255, 255, 255))
        self.header_rect = pygame.Rect(
            (self.display.get_width()/2 -self.header.get_width()/2, 0),
                (self.header.get_width(), self.header.get_height()))

        self.font_manager = load_font(getHighScoresFontManagerFont(),
                                    getHighScoresFontManagerFontSize())
        self.music = load_sound(getHighScoresMusic())
        self.music.play(loops=-1)



    def exit(self):
        self.music.stop()

    def reason(self):
        keys = pygame.key.get_pressed()
        if keys[K_RETURN]:
            return title.Title()

    def act(self):
        self.display.blit(self.background, (0, 0))
        self.display.blit(self.header, self.header_rect)

        for y, score in enumerate(HighScores.high_scores):
            self.display.blit(self.font_manager.render("%d    %d" % (y+1, int(score)), True, whiteColor()), (self.display.get_width()/2 - 64, (self.header_rect.top + self.header.get_height()) + (32*(y+1))))

        pygame.display.update()
        pygame.event.clear()







