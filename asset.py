import pygame
import os, re

from clock import Timer
from utils import *
from window import *

from OpenGL.GL import *
from OpenGL.GLU import *

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

def _load_image(path):
	image = pygame.image.load(path)
	w, h = image.get_width(), image.get_height()

	tex_id = _pygame_surface_to_tex(image)
	return (tex_id, (w, h))

def _draw_image(img, x, y, w, h):
	glMatrixMode(GL_MODELVIEW)
	glPushMatrix()
	glLoadIdentity()
	glTranslatef(x, y, 0.0) # shift to (x, y)
	glBindTexture(GL_TEXTURE_2D, img)

	# Actual draw
	glBegin(GL_QUADS)
	glTexCoord2f(0.0, 1.0); glVertex3f(0.0, 0.0,  0.0) # Left top
	glTexCoord2f(1.0, 1.0); glVertex3f(w,  0.0,  0.0)  # Right top
	glTexCoord2f(1.0, 0.0); glVertex3f(w, h,  0.0)     # Right bottom
	glTexCoord2f(0.0, 0.0); glVertex3f(0.0, h,  0.0)   # Left bottom
	glEnd()
	glBindTexture(GL_TEXTURE_2D, 0) # unbind
	glPopMatrix()

def _pygame_surface_to_tex(surface):
	tex_id = glGenTextures(1)
	glBindTexture(GL_TEXTURE_2D, tex_id)
	glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, surface.get_width(), surface.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, pygame.image.tostring(surface, 'RGBA', True))
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
	glPixelStorei(GL_PACK_ALIGNMENT, 1)
	return tex_id

'''pygame_surface_to_image(surface) -> Image_2

Convert the pygame surface to Image that holds OpenGL texture id
'''
def pygame_surface_to_image(surface):
	img = Image_2('')
	img.img = _pygame_surface_to_tex(surface)
	img.w = surface.get_width()
	img.h = surface.get_height()
	return img

'''Image

image space: left-top: (0, 0); right-bottom (1, 1)
'''
class Image_2:
	def __init__(self, path: str, resize_size=(1., 1.), rotate_deg=0., cent_pos=(0., 0.)):
		self.path = path
		self.img = None
		self.w = -1
		self.h = -1

		# Load image if path
		if path != None and path != '':
			img = _load_image(path)
			self.img = img[0]
			self.w = img[1][0]
			self.h = img[1][1]

		self.cent_pos = cent_pos      # [0.0, 1.0]
		self.rotate_deg = rotate_deg
		self.resize_size = resize_size # (float, float)

	# BUG(roy4801): error
	def __del__(self):
		pass
		# img = self.img
		# try:
		# 	glDeleteTextures([img])
		# except error.GLerror:
		# 	err = glGetError()
		# 	if ( err != GL_NO_ERROR ):
		# 		print('GLERROR: ', gluErrorString( err ))
		# 		sys.exit()

	def draw(self, x, y):
		t_w = int(self.w * self.resize_size[0])
		t_h = int(self.h * self.resize_size[1])
		t_x = x - int(self.w * self.cent_pos[0])
		t_y = y - int(self.h * self.cent_pos[1])
		# print('Draw {} {} {} {}'.format(t_x, t_y, t_w, t_h))
		_draw_image(self.img, t_x, t_y, t_w, t_h)

	def rotate(self, deg=0.):
		raise NotImplementedError

	def resize(self, resize_size=(0, 0)):
		raise NotImplementedError

	def copy(self):
		tmp = Image_2(self.path, self.resize_size, self.rotate_deg, self.cent_pos)
		return tmp

	def __repr__(self):
		return object.__repr__(self)
	def __str__(self):
		info = self.__repr__() + '\n  '
		info += 'Path = {}'.format(self.path) + '\n  '
		info += 'Img = {}'.format(self.img) + '\n  '
		info += 'w = {}, h = {}'.format(self.w, self.h) + '\n  '
		info += 'cent_pos = {}'.format(self.cent_pos) + '\n  '
		info += 'rotate_deg = {}'.format(self.rotate_deg) + '\n  '
		info += 'resize_size = {}'.format(self.resize_size) + '\n'
		return info

	# Getter/Setter
	def get_width(self):
		return self.w
	def get_height(self):
		return self.h
	def get_size(self):
		return (self.w, self.h)

# TODO(roy4801: deprecated
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

# TODO(roy4801): Implement this
class Sprite_2:
	def __init__(self, sprite_type, name, fps=0, animate_type=ANI_NONE, cent_pos=(0, 0), start_frame=0, resize_size=(1., 1.), rotate_deg=0.):
		self.image_list = []  # image list
		self.sprite_type = sprite_type # sprite type
		self.name = name  # name
		# For SP_ANIMATE
		self.frame_num = 0
		self.now_frame = start_frame
		self.fps = fps
		self.animate_type = animate_type
		self.timer = None
		self.start = False
		# for ANI_ONCE
		self.had_draw_once = False
		self.draw_frame_cnt = 0

		if sprite_type == SP_STATIC:
			img = Image_2(GET_PATH(IMG_SPRITE, name), resize_size, rotate_deg, cent_pos)
			self.image_list.append(img)
			self.frame_num = 1
		elif sprite_type == SP_ANIMATE:
			self.timer = Timer(1000/fps)
			# list dir
			path = GET_DIR(IMG_SPRITE)
			dir_list = os.listdir(path)
			# count frame_num
			cnt = 0
			for item in dir_list:
				if item.startswith(name):
					cnt += 1
			self.frame_num = cnt
			# load {name}{000}.png ~ {name}{cnt}.png
			for i in range(cnt):
				self.image_list.append(Image_2('{}{:03d}.png'.format(path + name, i), resize_size, rotate_deg, cent_pos))

	def copy(self):
		new_sp = Sprite_2(-1, self.name, self.fps, self.animate_type, self.cent_pos, 0, self.resize_size, self.rotate_deg)
		new_sp.sprite_type = self.sprite_type
		new_sp.image_list = self.image_list
		return new_sp

	def draw(self, x, y):
		if self.had_draw_once:
			self.had_draw_once = False
			self.draw_frame_cnt = 0

		# Actual draw
		if self.sprite_type == SP_ANIMATE and not (self.animate_type == ANI_ONCE and self.had_draw_once):
			if not self.start:
				# start the timer
				self.timer.reset()
				self.start = True
			else:
				# if timeout
				if self.timer.timeout():
					# next frame
					self.now_frame += 1
					self.draw_frame_cnt += 1
					# self.nowFrame %= self.frame_num
					if self.now_frame >= self.frame_num:
						self.now_frame = 0
						# if is `ANI_ONCE` and draw `frame_num` frames
						if self.animate_type == ANI_ONCE and self.draw_frame_cnt >= self.frame_num:
							self.had_draw_once = True
					# reset clock
					self.timer.reset()
		# draw the image on the screen
		self.image_list[self.now_frame].draw(x, y)

		if self.animate_type == ANI_ONCE and self.had_draw_once:
			return True
		else:
			return False

	def __repr__(self):
		return object.__repr__(self)
	def __str__(self):
		info = '{}:  {}\n\t'.format(self.name, self.__repr__())
		info += 'type = {}\n\t'.format('SP_STATIC' if self.sprite_type == SP_STATIC else 'SP_ANIMATE')

		if self.sprite_type == SP_ANIMATE:
			info += 'animate type = {}\n\t'.format('ANI_NONE' if self.animate_type == 0 else 'ANI_ONCE' if self.animate_type == 1 else 'ANI_LOOP' if self.animate_type == 2 else 'ANI_ERROR')
			info += 'frame_num = {}\n\t'.format(self.frame_num)
			info += 'now_frame = {}\n\t'.format(self.now_frame)
			info += 'fps = {}\n\t'.format(self.fps)
		return info

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
		self.timer = None
		self.start = False

		# for ANI_ONCE
		self.draw_once = False
		self.drawFrameCnt = 0

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