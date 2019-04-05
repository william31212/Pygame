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

'''pygame_surface_to_image(surface) -> Image

Convert the pygame surface to Image that holds OpenGL texture id
'''
def pygame_surface_to_image(surface):
	img = Image('')
	img.img = _pygame_surface_to_tex(surface)
	img.w = surface.get_width()
	img.h = surface.get_height()
	img.path = 'pygame_surface_to_image'
	return img

'''Image

image space: left-top: (0, 0); right-bottom (1, 1)
'''
class Image:
	def __init__(self, path: str, resize_size=(1., 1.), rotate_deg=0., cent_pos=(0., 0.)):
		self.path = path
		self.img = None
		self.x = 0
		self.y = 0
		self.w = -1
		self.h = -1

		# Load image if path
		if path != None and path != '':
			img = _load_image(path)
			self.img = img[0]
			self.w = img[1][0]
			self.h = img[1][1]

		self.cent_pos = cent_pos       # [0.0, 1.0]
		self.rotate_deg = rotate_deg
		self.resize_size = resize_size # (float, float)

	# BUG(roy4801): error
	def __del__(self):
		img = self.img
		if img != None:
			try:
				glDeleteTextures([img])
			except error.GLerror:
				err = glGetError()
				if ( err != GL_NO_ERROR ):
					print('GLERROR: ', gluErrorString( err ))
					sys.exit()

	def draw(self, x, y):
		self.x = x
		self.y = y
		# resize width and height
		t_w = self.w * self.resize_size[0]
		t_h = self.h * self.resize_size[1]
		t_x = x - t_w * self.cent_pos[0]
		t_y = y - t_h * self.cent_pos[1]
		# print('Draw {} {} {} {}'.format(t_x, t_y, t_w, t_h))
		_draw_image(self.img, t_x, t_y, t_w, t_h)

	def rotate(self, deg=0.):
		raise NotImplementedError

	def resize(self, resize_size=(0, 0)):
		raise NotImplementedError

	def copy(self):
		tmp = Image(self.path, self.resize_size, self.rotate_deg, self.cent_pos)
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
	# TODO(roy4801): make these return non-orig ver
	def get_width(self):
		return self.w * self.resize_size[0]
	def get_height(self):
		return self.h * self.resize_size[1]
	def get_size(self):
		return (self.w * self.resize_size[0], self.h * self.resize_size[1])

	def get_orig_width(self):
		return self.w
	def get_orig_height(self):
		return self.h
	def get_orig_size(self):
		return (self.w, self.h)

	def get_resize(self):
		return self.resize_size

	def get_left_upper(self):
		t_x = self.x - self.get_width() * self.cent_pos[0]
		t_y = self.y - self.get_height() * self.cent_pos[1]
		return (t_x, t_y)

	def get_cent(self):
		x, y = self.get_left_upper()
		x += self.get_width() * self.cent_pos[0]
		y += self.get_height() * self.cent_pos[1]
		return (x, y)
	# dbg
	def dbg_draw(self, x, y):
		import draw_premitive as dp
		t_w, t_h = self.get_size()
		cent_x, cent_y = self.get_cent()
		dp.rect((255, 0, 0, 204), (*self.get_left_upper(), t_w, t_h), 1)
		dp.circle((255, 0, 0, 204), (cent_x, cent_y), 3)
		

class Sprite:
	def __init__(self, sprite_type, name, fps=0, animate_type=ANI_NONE, cent_pos=(0, 0), start_frame=0, resize_size=(1., 1.), rotate_deg=0., copy=False):
		self.image_list = []             # image list
		self.sprite_type = sprite_type   # sprite type
		self.name = name                 # name
		# For SP_ANIMATE
		self.frame_num = 0               # total images of a animated sprite
		self.now_frame = start_frame     # current frame
		self.fps = fps                   # fps
		self.animate_type = animate_type # ANI_ONCE/ANI_LOOP
		self.timer = None                # timer
		self.start = False               # start flag
		# for ANI_ONCE
		self.had_draw_once = False
		self.draw_frame_cnt = 0

		if sprite_type == SP_STATIC:
			if not copy:
				img = Image(GET_PATH(IMG_SPRITE, name), resize_size, rotate_deg, cent_pos)
				self.image_list.append(img)
			self.frame_num = 1
		elif sprite_type == SP_ANIMATE:
			self.timer = Timer(1000/self.fps)
			if not copy:
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
					self.image_list.append(Image('{}{:03d}.png'.format(path + name, i), resize_size, rotate_deg, cent_pos))

	def copy(self):
		# TODO(roy4801): this should be refactor
		cent_pos = self.image_list[0].cent_pos
		resize_size = self.image_list[0].resize_size
		rotate_deg = self.image_list[0].rotate_deg
		new_sp = Sprite(SP_ANIMATE, self.name, self.fps, self.animate_type, cent_pos, 0, resize_size, rotate_deg, True)
		new_sp.image_list = self.image_list
		new_sp.frame_num = len(self.image_list)
		return new_sp

	def draw(self, x, y):
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

	def is_draw_once(self):
		return self.animate_type == ANI_ONCE and self.had_draw_once

	def reset_draw_once(self):
		if self.had_draw_once:
			self.had_draw_once = False
			self.draw_frame_cnt = 0

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