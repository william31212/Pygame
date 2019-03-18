import pygame
import os

from utils import GET_PATH
from clock import Timer

# For SP_ANIMATE
Clock_list = {}

# Sprite types
SP_STATIC  = 0
SP_ANIMATE = 1

# for SP_ANIMATE
ANI_NONE = 0
ANI_ONCE = 1
ANI_LOOP = 2

# resize
resize_x = 200
resize_y = 200
'''
Image
'''
class Image:
	def __init__(self,filename=None,resize=0):
		# asset image
		self.img = None
		self.resize = resize
		if filename != None:
			self.loadImage(filename,resize)
	def loadImage(self, filename,resize=0):
		self.resize = resize
		if resize == 0:
			self.img = pygame.image.load(GET_PATH('image', filename))
		if resize == 1:
			self.img = pygame.transform.scale(pygame.image.load(str(GET_PATH('image', filename))), (resize_x, resize_y))
# TODO(roy4801): Add re matching file names

'''
Sprite
	Positionable 2D image supporting static and animated sprite
'''
class Sprite:
	def __init__(self,t, name, fps=0, ani=ANI_NONE, startFrame=0, resize=0):
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
		# self.clk = None
		self.timer = None
		self.start = False

		# for ANI_ONCE
		self.draw_once = False
		self.drawFrameCnt = 0

		# for resize
		self.resize = resize

		# static sprite
		if self.t == SP_STATIC:
			img = Image()
			img.loadImage(name,resize)
			self.imageList.append(img)
			self.frameNum = 1
		# animated sprite
		elif self.t == SP_ANIMATE:
			self.timer = Timer(1000/self.fps)
			dir_list = os.listdir(GET_PATH('image', ''))
			print(dir_list)
			cnt = 0
			for item in dir_list:
				if item.startswith(name):
					cnt += 1
			self.frameNum = cnt
			# load {name}{000}.png ~ {name}{cnt}.png
			for i in range(cnt):
				self.imageList.append(Image('{}{:03d}.png'.format(name, i),resize))
	'''
	draw(x, y)
		draw the sprite on the screen
	return: if ani == ANI_ONCE && draw_once == true then return true meaning it draw one complete cycle (frameNum)
	, otherwise return false
	'''

	def draw(self, x, y):
		# Get gameDisplay
		gameDisplay = pygame.display.get_surface()
		# Actual draw
		if self.t == SP_ANIMATE and not (self.ani == ANI_ONCE and self.draw_once):
			if not self.start:
				# start the timer
				self.timer.reset()
				self.start = True
			else:
				# if timeout
				if self.timer.timeout():
					self.nowFrame += 1
					self.drawFrameCnt += 1
					# self.nowFrame %= self.frameNum
					if self.nowFrame >= self.frameNum:
						self.nowFrame = 0
						# if is `ANI_ONCE` and draw `frameNum` frames
						if self.ani == ANI_ONCE and self.drawFrameCnt >= self.frameNum:
							self.draw_once = True
					# reset clock
					self.timer.reset()
		# draw the image on the screen
		gameDisplay.blit(self.imageList[self.nowFrame].img, (x, y))

		if self.ani == ANI_ONCE and self.draw_once:
			self.draw_once = False
			self.drawFrameCnt = 0
			return True
		else:
			return False

	'''
	copy()
		Return a copy of self
	'''
	def copy(self):
		newSprite = Sprite(self.t, self.name, self.fps, self.ani, 0)
		return newSprite

	'''
	For print()
	'''
	def __repr__(self):
		return object.__repr__(self)
	def __str__(self):
		info = '{}:  {}\n\t'.format(self.name, self.__repr__())
		info += 'type = {}\n\t'.format('SP_STATIC' if self.t == 0 else 'SP_ANIMATE')

		if self.t == SP_ANIMATE:
			info += 'animate type = {}\n\t'.format('ANI_NONE' if self.ani == 0 else 'ANI_ONCE' if self.ani == 1 else 'ANI_LOOP' if self.ani == 2 else 'ANI_ERROR')
			info += 'frameNum = {}\n\t'.format(self.frameNum)
			info += 'nowFrame = {}\n\t'.format(self.nowFrame)
			info += 'fps = {}\n\t'.format(self.fps)
		return info