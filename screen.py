# !/usr/bin/env python
# -*- coding: utf-8 *-*

## we use regex to get the resolution of the screen
import re

## class to get information on the screen size
## in order to adapt the size of the game to the 
## screen player resolution
class Screen(object):

	def __init__(self,vidInfo):
		self.stringToParse=str(vidInfo)
		self.width = -1
		self.height = -1
		## TODO : à changer
		self.setWidth()
		self.setHeight()

	def setWidth(self):
		pattern = "current_w = [0-9]*"
		rawResult = re.search(pattern,self.stringToParse).group(0)
		self.width = int(rawResult.split('=')[1])
		assert(self.width > 0)

	def setHeight(self):
		pattern = "current_h = [0-9]*"
		rawResult = re.search(pattern,self.stringToParse).group(0)
		self.height = int(rawResult.split('=')[1])
		assert(self.height > 0)