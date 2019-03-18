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

'''
Image
'''
IMAGE_POS_LT   = 0
IMAGE_POS_CENT = 1 # TODO(roy4801): Implement this

class Image:
	def __init__(self, filename=None, resize=(0, 0), rotate=0.):
		# asset image
		self.img = None
		self.resize = resize
		self.rot_deg = rotate
		self.rot_img = None
		if filename != None:
			self.loadImage(filename, resize, rotate)
	'''
	loadImage(filename, resize, rotate) -> None
	'''
	def loadImage(self, filename ,resize=(0, 0), rotate=0.):
		self.resize = resize
		self.rot_deg = rotate
		# TODO(roy4801): move the GET_PATH to outside
		self.img = pygame.image.load(GET_PATH('image', filename))
		if resize != (0, 0):
			self.img = pygame.transform.scale(self.img, resize)
		if rotate != 0.:
			self.rot_img = pygame.transform.rotate(self.img, rotate)
	'''
	rotate(deg) -> Image
		rotate image by deg degrees (counter-clockwise)
	'''
	def rotate(self, deg=0., rotate_type=IMAGE_ROT_PT):
		self.rot_deg += deg
		if deg != 0.:
			self.rot_img = pygame.transform.rotate(self.img, deg)
		return self
	'''
	resize(resize=(0, 0)) -> Image
	'''
	def resize(self, resize=(0, 0)):
		self.resize = resize
		if resize != (0, 0):
			self.img = pygame.transform.scale(self.img, resize)
		return self
	# TODO(roy4801): Implement this
	def draw(self, x, y):
		gameDisplay = pygame.display.get_surface()
		img = None
		if self.rot_deg != 0.:
			img = self.rot_img
		else:
			img = self.img
		gameDisplay.blit(img, (x, y))

	def get_width(self):
		return self.img.get_width()
	def get_height(self):
		return self.img.get_height()
	def get_rect(self):
		return (self.get_width(), self.get_height())
# TODO(roy4801): Add re matching file names
'''
Sprite
	Positionable 2D image supporting static and animated sprite
'''
class Sprite:
	def __init__(self,t, name, fps=0, ani=ANI_NONE, startFrame=0, resize=(0, 0), rotate=0.):
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

		# transform
		self.resize = resize
		self.rotate = rotate

		# static sprite
		if self.t == SP_STATIC:
			img = Image()
			img.loadImage(name, resize, rotate)
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
				self.imageList.append(Image('{}{:03d}.png'.format(name, i), resize, rotate))
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