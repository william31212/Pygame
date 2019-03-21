import pygame
import os, re

from clock import Timer
from utils import *

# For SP_ANIMATE
Clock_list = {}

# Sprite types
SP_STATIC  = 0
SP_ANIMATE = 1

# for SP_ANIMATE
ANI_NONE = 0
ANI_ONCE = 1
ANI_LOOP = 2

DBG_SHOW_IMAGE_CENT   = True
DBG_SHOW_IMAGE_BORDER = True

'''
Image
'''
# TODO(roy4801): Support for dynamic rescale
F_NONE   = 0
F_ROTATE = 1
F_ALL    = 2
# num of flags
F_TOTAL  = 3

class Image:
	'''
	__init__(name, resize_size, rotate_deg, cent_pos) -> None
	'''
	def __init__(self, name=None, resize_size=(0, 0), rotate_deg=0., cent_pos=None):
		# image
		self.img = None

		# Load image
		if name != None:
			self.img = pygame.image.load(name)
		# Resize
		if resize_size != (0, 0):
			self.img = pygame.transform.scale(self.img, resize_size)
		# Cent point
		if cent_pos != None:
			self.cent_x = cent_pos[0]
			self.cent_y = cent_pos[1]
		else:
			self.cent_x = self.get_width() // 2
			self.cent_y = self.get_height() // 2
		
		self.flags = F_NONE        # flags for operations

		# Rotation
		self.rot_deg = rotate_deg  # rotation degrees
		self.rot_upper_left = None # lambda for getting rotated upper left

		self.rot_img = None        # changed img

	'''
	rotate(deg) -> Image
		rotate image by deg degrees (counter-clockwise)
	'''
	def rotate(self, deg=0.):
		if deg == 0.:
			return self

		self.rot_img = pygame.transform.rotate(self.img, deg)
		self.rot_deg = deg
		self.flags |= F_ROTATE

		w, h = self.img.get_size()
		originPos = (self.cent_x, self.cent_y)
		
		# TODO(roy4801): Figure this out
		box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
		box_rotate = [p.rotate(deg) for p in box]
		min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
		max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

		pivot        = pygame.math.Vector2(originPos[0], -originPos[1])
		pivot_rotate = pivot.rotate(deg)
		pivot_move   = pivot_rotate - pivot

		self.rot_upper_left = lambda x, y: (x - originPos[0] + min_box[0] - pivot_move[0], y - originPos[1] - max_box[1] + pivot_move[1])
		return self

	def draw(self, x, y):
		gameDisplay = pygame.display.get_surface()
		img = None
		upper_left = None
		# if rotated
		if self.flags & F_ROTATE:
			img = self.rot_img
			upper_left = self.rot_upper_left(x, y)
		# not changed
		else:
			img = self.img
			upper_left = (x-self.cent_x, y-self.cent_y)
		
		gameDisplay.blit(img, upper_left)

		if DBG_SHOW_IMAGE_CENT:
			pygame.draw.circle(gameDisplay, (0, 255, 0), (x, y), 3)
			pygame.draw.circle(gameDisplay, (255, 0, 0), (int(upper_left[0]), int(upper_left[1])), 3)
		if DBG_SHOW_IMAGE_BORDER:
			pygame.draw.rect(gameDisplay, (255, 0, 0), (*upper_left, *img.get_size()), 1)

	def copy(self):
		new = Image(None, (0, 0), 0, (self.cent_x, self.cent_y))
		new.img = self.img
		return new

	'''
	these get_xxx() returns the original img size
	'''
	def get_width(self):
		return self.img.get_width()
	def get_height(self):
		return self.img.get_height()
	def get_size(self):
		return self.img.get_size()

# 1. TODO(roy4801): Add re matching file names
# 2. TODO(roy4801): Refactor resize and rotate
'''
Sprite
	Positionable 2D image supporting static and animated sprite
'''
class Sprite:
	def __init__(self,t, name, fps=0, ani=ANI_NONE, startFrame=0, resize=(0, 0), rotate=0., cent_pos=None):
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
			img = Image(name, resize, rotate, cent_pos)
			self.imageList.append(img)
			self.frameNum = 1
		# animated sprite
		elif self.t == SP_ANIMATE:
			self.timer = Timer(1000/self.fps)
			name = re.search(r"\w+$", self.name).group(0)
			# split file
			path = GET_DIR(IMG_SPRITE)
			dir_list = os.listdir(path)
			# Count frameNum
			cnt = 0
			for item in dir_list:
				if item.startswith(name):
					cnt += 1
			self.frameNum = cnt
			# load {name}{000}.png ~ {name}{cnt}.png
			for i in range(cnt):
				self.imageList.append(Image('{}{:03d}.png'.format(path+name, i), resize, rotate, cent_pos))
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