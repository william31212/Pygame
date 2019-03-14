import pygame
import os

from utils import GET_PATH
from clock import Clock

gameDisplay = None

# For SP_ANIMATE
Clock_list = {}

# Sprite types
SP_STATIC  = 0
SP_ANIMATE = 1

# for SP_ANIMATE
ANI_NONE = 0
ANI_ONCE = 1
ANI_LOOP = 2

'''
Image
'''
class Image:
	def __init__(self, filename=None):
		# asset image
		self.img = None
		if filename != None:
			self.loadImage(filename)
	def loadImage(self, filename):
		self.img = pygame.image.load(GET_PATH('image', filename))

'''
Sprite
'''
class Sprite:
	def __init__(self, t, name, fps=0, ani=ANI_NONE, startFrame=0):
		self.imageList = []
		# sprite type
		self.t = t
		# image
		self.name = name

		# for SP_ANIMATE
		self.frameNum = 0
		self.nowFrame = startFrame
		self.fps = fps
		self.ani = ani
		self.clk = None
		self.start = False

		# static sprite
		if self.t == SP_STATIC:
			img = Image()
			img.loadImage(name)
			self.imageList.append(img)
			self.frameNum = 1
		# animated sprite
		elif self.t == SP_ANIMATE:
			self.clk = Clock()
			dir_list = os.listdir(GET_PATH('image', ''))
			print(dir_list)
			cnt = 0
			for item in dir_list:
				if item.startswith(name):
					cnt += 1
			self.frameNum = cnt
			# load {name}{000}.png ~ {name}{cnt}.png
			for i in range(cnt):
				self.imageList.append(Image('{}{:03d}.png'.format(name, i)))

	# draw the sprite on the screen
	def draw(self, x, y):
		# Get gameDisplay
		global gameDisplay
		if gameDisplay == None:
			gameDisplay = pygame.display.get_surface()
		# Actual draw
		if self.t == SP_ANIMATE:
			if not self.start:
				self.clk.reset()
				self.start = True
			else:
				# print('{} = {}'.format(self.name, self.clk.getPassed()))
				# if timeout
				if self.clk.getPassed() > 1000 / self.fps:
					self.nowFrame += 1
					if self.nowFrame >= self.frameNum: # %= frameNum
						self.nowFrame = 0
					# reset clock
					self.clk.reset()
		gameDisplay.blit(self.imageList[self.nowFrame].img, (x, y))

	def copy(self):
		newSprite = Sprite(self.t, self.name, self.fps, self.ani, 0)
		return newSprite

	def __repr__(self):
		return object.__repr__(self)
	'''
	For print()
	'''
	def __str__(self):
		info = '{}:  {}\n\t'.format(self.name, self.__repr__())
		info += 'type = {}\n\t'.format('SP_STATIC' if self.t == 0 else 'SP_ANIMATE')

		if self.t == SP_ANIMATE:
			info += 'animate type = {}\n\t'.format('ANI_NONE' if self.ani == 0 else 'ANI_ONCE' if self.ani == 1 else 'ANI_LOOP' if self.ani == 2 else 'ANI_ERROR')
			info += 'frameNum = {}\n\t'.format(self.frameNum)
			info += 'nowFrame = {}\n\t'.format(self.nowFrame)
			info += 'fps = {}\n\t'.format(self.fps)
		return info