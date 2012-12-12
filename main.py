# !/usr/bin/env python
# -*- coding: utf-8 *-*
import pygame

import state
import title
from config import *



class initGame():
    def __init__(self,caption):
    	pygame.init()
    	self.display = pygame.display.set_mode((800,600))
    	pygame.display.set_caption(caption)
        self.sm = state.StateMachine(self, title.Title())

    def start(self):
        while True:
            self.sm.update()

if __name__ == "__main__":
	g = initGame("Run Ninja")
	g.start()
