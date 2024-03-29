# !/usr/bin/env python
# -*- coding: utf-8 *-*
import time
import pygame

import state
import level
import surface_manager
import color
from utile import *
from config import *

class Hud(state.State):
	"""
	Hud = Head up display
	It is here that we display informations that you can see on the top of the screen
	attributes:
		display : the current working surface
		font_manager : the font manager uses to display
		shuriken_element :
		fps_element : here to display the framerate of the game
		score_element :
	static attributes:
		player
		timer
		game
	"""
	timer = None
	player = None
	game = None
	def __init__(self, game, player, timer):
		self.display = pygame.display.get_surface()

		Hud.player = player
		Hud.timer = timer
		Hud.game = game

		self.font_manager = load_font(getHudFont(),getHudFontSize())

		self.shuriken_element = ShurikenElement(self.font_manager)
		self.fps_element = FPSElement(self.font_manager)
		self.score_element = ScoreElement(self.font_manager)

		surface_manager.add(self.shuriken_element)
		surface_manager.add(self.fps_element)
		surface_manager.add(self.score_element)

	def act(self):
		pass



class ShurikenElement(pygame.sprite.DirtySprite):
	"""
	attributes:
		image : the image
		font_manager : the font uses to display
		rect : the bounded rect of the image
		dirty : the rendering is dependent on this flag,
                    see pygame.sprite.DirtySprite for more explanation
	"""
	def __init__(self, font_manager):
		super(ShurikenElement, self).__init__()
		self.font_manager = font_manager
		##whiteColor = color.white
		self.image = self.font_manager.render(
			"SHURIKENS: %d" % Hud.player.shurikens, True,(255,255,255))
		self.rect = pygame.Rect((0, 0),
			(self.image.get_width(),self.image.get_height()))
		self.dirty = 1


	def update(self):
		self.image =  self.font_manager.render(
			"SHURIKENS: %d" % Hud.player.shurikens, True, (255, 255, 255))
		self.dirty = 1



class FPSElement(pygame.sprite.DirtySprite):
	"""
	attributes:
		display : the current working surface
		font_manager : the font manager uses to display
		image : the image
		rect : the bounded rect of the image
		dirty : the rendering is dependent on this flag,
                        see pygame.sprite.DirtySprite for more explanation
	"""
	def __init__(self, font_manager):
		super(FPSElement, self).__init__()
		self.display = pygame.display.get_surface()
		self.font_manager = font_manager
		self.image = self.font_manager.render(
			"FPS: %2.1f" % Hud.timer.get_fps(), True, (255, 255, 255))
		self.rect = pygame.Rect(
        		(self.display.get_width() - self.image.get_width() - 15, 0),
         			(self.image.get_width(), self.image.get_height()))
		self.dirty = 1


	def update(self):
		self.image =  self.font_manager.render(
			"FPS: %2.1f" % Hud.timer.get_fps(), True, (255, 255, 255))
		self.dirty = 1



class ScoreElement(pygame.sprite.DirtySprite):
	"""
	attributes :
		display : the current working surface
		font_manager : the font manager uses to display
		image : the image
		rect : the bounded rect of the image
		dirty : the rendering is dependent on this flag,
                    see pygame.sprite.DirtySprite for more explanation
	"""
	def __init__(self, font_manager):
		super(ScoreElement, self).__init__()
		self.display = pygame.display.get_surface()
		self.font_manager = font_manager
		self.image = self.font_manager.render(
			"SCORE: %d" % Hud.game.score, True, (255, 255, 255))
		self.rect = pygame.Rect(
			(self.display.get_width()/2 - self.image.get_width()/2, 0),
				(self.image.get_width(), self.image.get_height()))
		self.dirty = 1


	def update(self):
		self.image =  self.font_manager.render(
			"SCORE: %d" % Hud.game.score, True, (255, 255, 255))
		self.dirty = 1



class ComboElement(pygame.sprite.DirtySprite):
	"""
	attributes
		display : the current working surface
		font_manager : the font manager uses to display
		image : the image
		rect : the bounded rect of the image
		pos_x :
		pos_y
		delay
		has_shown
		dirty : the rendering is dependent on this flag,
						 see pygame.sprite.DirtySprite for more explanation
	"""
	def __init__(self, bonus):
		super(ComboElement, self).__init__()
		self.remove_existing()
		self.display = pygame.display.get_surface()
		self.font_manager = load_font(getComboFont(), getComboFontSize())
		self.image = self.font_manager.render(
			"COMBO! %d PT. BONUS" % bonus, True, (255, 255, 255))
		self.rect = pygame.Rect(
			(0 - self.image.get_width(), self.image.get_height()*2),
			 (self.image.get_width(), self.image.get_height()))
		self.pos_x = 0 - self.image.get_width()
		self.pos_y = self.image.get_height()*2
		self.delay = time.clock()
		self.has_shown = False
		self.dirty = 1


	def update(self):
		if self.pos_x < 0 - self.rect.width and self.has_shown:
			surface_manager.remove(self)

		if not self.has_shown and self.pos_x < 0:
			self.pos_x += getGamePixelMove()

		if self.pos_x >= 0 - self.rect.width and time.clock() > self.delay + 3:
			self.has_shown = True
			self.pos_x -= getGamePixelMove()

		self.rect.topleft = (self.pos_x, self.pos_y)
		self.dirty = 1

	def remove_existing(self):
		for surface in surface_manager.surface_list:
			if type(surface) is ComboElement:
				surface_manager.remove(surface)
				return

def show_combo(bonus):
	surface_manager.add(ComboElement(bonus))
