import pygame, sys
from OpenGL.GL import *
from OpenGL.GLU import *

W_NONE       = 0
W_FULLSCREEN = 1<<0
W_OPENGL     = 1<<1
W_RESIZABLE  = 1<<2 # not impl
W_NOFRAME    = 1<<3 # not impl

# TODO(roy4801): Have own event queue
'''
Window

Manage the window
'''
class Window:
	def __init__(self, title, size, win_flag=W_NONE):
		self.title = title
		self.size = size
		self.win_flag = win_flag

		flag = pygame.DOUBLEBUF
		flag |= pygame.FULLSCREEN if win_flag & W_FULLSCREEN else 0
		flag |= pygame.OPENGL if win_flag & W_OPENGL else 0
		flag |= pygame.RESIZABLE if win_flag & W_RESIZABLE else 0
		flag |= pygame.NOFRAME if win_flag & W_NOFRAME else 0

		self.surface = pygame.display.set_mode(size, flag, 32)
		self.set_caption(title)

		if win_flag & W_OPENGL:
			# TODO(roy4801): OpenGL init things

	def main_loop(self):
		self.process_event()
		self.update()
		self.draw()
		self._flip()

	def process_event(self, handle_list):
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			# TODO(roy4801): process events

	def update(self):
		pass

	def draw(self):
		pass

	def set_icon(self, icon):
		raise NotImplementedError
	def get_icon(self):
		raise NotImplementedError

	def set_caption(self, s):
		pygame.display.set_caption(s)
	def get_caption(self):
		raise NotImplementedError

	def is_focus(self):
		return pygame.display.get_active()

	def iconify(self):
		return pygame.display.iconify()

	def _clear_screen(sefl):
		if self.win_flag & W_OPENGL:

	def _flip(self):
		pygame.display.flip()