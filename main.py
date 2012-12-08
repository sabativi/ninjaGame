# !/usr/bin/env python
# -*- coding: utf-8 *-*
import pygame

import state
import title
import screen
from config import *



class initGame():
    def __init__(self,vidInfo):
    	resolution = screen.Screen(vidInfo)
        self.sm = state.StateMachine(self, title.Title(resolution))

    def start(self):
        while True:
            self.sm.update()

if __name__ == "__main__":
	pygame.init()
	## the game will be played in fullscreen mode
	display = pygame.display.set_mode((800,600))
	pygame.display.set_caption("Run! Space to Jump - Use the mouse to Throw")
	g = initGame(pygame.display.Info())
	g.start()
