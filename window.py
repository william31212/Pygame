import pygame, sys
from OpenGL.GL import *
from OpenGL.GLU import *

# TODO(roy4801): Impl D_SOFTWARE
D_SOFTWARE = 0
D_HARDWARE = 1
DRAW_METHOD = D_HARDWARE

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
	def __init__(self, title, size, win_flag=W_NONE, fps=60):
		self.title = title
		self.size = size
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

		global DRAW_METHOD
		if win_flag & W_OPENGL:
			DRAW_METHOD = D_HARDWARE
			glEnable(GL_TEXTURE_2D)
			glEnable(GL_BLEND)
			glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

			glClearColor(0.5, 0.5, 0.5, 0.0)
			#
			glMatrixMode(GL_PROJECTION)
			glLoadIdentity()
			gluOrtho2D(0.0, size[0], size[1], 0.0) # Important
			#
			glMatrixMode(GL_MODELVIEW)
		else:
			DRAW_METHOD = D_SOFTWARE

	# Do not overwrite ##########
	def run(self):
		self.setup()

		while self.running:
			self.process_event()
			self.update()
			self._clear_screen()
			self.render()
			self._flip()
			self.fps_timer.tick(self.target_fps)

	def process_event(self):
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				self.ask_quit()
			# TODO(roy4801): process events
			for handle in self.handle_list:
				handle(e)

	def add_event_handle(self, handle):
		self.handle_list.append(handle)

	#############################
	# need to be implement
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