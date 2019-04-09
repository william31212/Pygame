import pygame, sys
from OpenGL.GL import *
from OpenGL.GLU import *

from debug_view import *

W_NONE       = 0
W_FULLSCREEN = 1<<0
W_OPENGL     = 1<<1
W_RESIZABLE  = 1<<2 # not impl
W_NOFRAME    = 1<<3 # not impl

def _init():
	pygame.init()
	pygame.mixer.init()

# TODO(roy4801): Have own event queue

'''Window

Manage the window
'''
class Window:
	WIDTH = None
	HEIGHT = None

	@staticmethod
	def get_width():
		return Window.WIDTH

	@staticmethod
	def get_height():
		return Window.HEIGHT

	@staticmethod
	def get_size():
		return (Window.WIDTH, Window.HEIGHT)

	def __init__(self, title, size, win_flag=W_NONE, fps=60):
		_init()
		self.title = title
		Window.WIDTH = size[0]
		Window.HEIGHT = size[1]
		self.win_flag = win_flag
		self.running = True

		self.handle_list = []

		flag = pygame.DOUBLEBUF
		flag |= pygame.FULLSCREEN if win_flag & W_FULLSCREEN else 0
		flag |= pygame.OPENGL if win_flag & W_OPENGL else 0
		flag |= pygame.RESIZABLE if win_flag & W_RESIZABLE else 0
		flag |= pygame.NOFRAME if win_flag & W_NOFRAME else 0

		self.surface = pygame.display.set_mode(size, flag)
		self.set_caption(title)
		self.fps_timer = pygame.time.Clock()
		self.target_fps = fps

		# DEBUG
		self.debug_flag = False
		self.debug_view = dbg_view(size)
		self.add_event_handle(self.debug_view.handle_event)

		if win_flag & W_OPENGL:
			glEnable(GL_TEXTURE_2D)
			glEnable(GL_BLEND)
			glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

			glClearColor(0.5, 0.5, 0.5, 1)
			#
			glMatrixMode(GL_PROJECTION)
			glLoadIdentity()
			gluOrtho2D(0.0, size[0], size[1], 0.0) # Important
			#
			glMatrixMode(GL_MODELVIEW)

	# Do not overwrite ##########
	def run(self):
		self.setup()

		while self.running:
			# process event
			self.process_event()
			# update
			self.debug_view.update()
			self.update()
			# Render
			self._clear_screen()
			self.render()
			if self.debug_flag:
				self.debug_view.render()
			self._flip()
			self.fps_timer.tick(self.target_fps)

	def process_event(self):
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				self.ask_quit()
			elif e.type == pygame.KEYDOWN and e.key == pygame.K_BACKQUOTE:
				self.debug_flag = not self.debug_flag
			# TODO(roy4801): process events
			for handle in self.handle_list:
				handle(e)

	def add_event_handle(self, handle):
		self.handle_list.append(handle)

	#############################
	# NEED to be implement
	def setup(self):
		raise NotImplementedError

	def update(self):
		raise NotImplementedError

	def render(self):
		raise NotImplementedError

	def ask_quit(self):
		raise NotImplementedError
		# self.quit()
	##############################
	def quit(self):
		self.running = False
		pygame.quit()
		sys.exit()

	def _clear_screen(self):
		if self.win_flag & W_OPENGL:
			glClear(GL_COLOR_BUFFER_BIT)
		else:
			pygame.display.get_surface().fill((128, 128, 128))

	def _flip(self):
		pygame.display.flip()

	# TODO(roy4801): impl
	def set_icon(self, icon):
		raise NotImplementedError
	def get_icon(self):
		raise NotImplementedError

	def set_caption(self, s):
		pygame.display.set_caption(s)
	# TODO(roy4801): impl
	def get_caption(self):
		raise NotImplementedError
	# BUG(roy4801): not return True after a full round of hidding and opening
	def is_focus(self):
		return pygame.display.get_active()

	def iconify(self):
		return pygame.display.iconify()

	def set_dbg_flag(self, flag):
		self.debug_flag = flag