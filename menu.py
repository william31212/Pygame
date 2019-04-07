import sys, pygame

from ui import *
sys.path.append("./RHframework")

from clock import Clock
from input import *
from asset import *
from utils import *
from tile import *
from shape import *
from player import *
from window import *

class Menu:
	# public
	def __init__(self):
		self.background = Image('./assets/img/' + 'start2' + '.png', (5.95, 7.85))
		self.button_play = Button(50, 450, 300, 70, Image('./assets/img/' + 'play' + '.png', (1.0, 1.0)), Image('./assets/img/' + 'play_hover' + '.png', (1.0, 1.0)), Image('./assets/img/' + 'play_click' + '.png', (1.0, 1.0)))
		self.button_intro = Button(450, 550, 300, 70, Image('./assets/img/' + 'intro' + '.png', (1.0, 1.0)), Image('./assets/img/' + 'intro_hover' + '.png', (1.0, 1.0)), Image('./assets/img/' + 'intro_click' + '.png', (1.0, 1.0)))
		self.button_quit = Button(450, 450, 300, 70, Image('./assets/img/' + 'quit' + '.png', (1.0, 1.0)), Image('./assets/img/' + 'quit_hover' + '.png', (1.0, 1.0)), Image('./assets/img/' + 'quit_click' + '.png', (1.0, 1.0)))

	def update(self, mouse):
		self.button_play.update((mouse.x, mouse.y), mouse.btn[MOUSE_L])
		self.button_quit.update((mouse.x, mouse.y), mouse.btn[MOUSE_L])
		self.button_intro.update((mouse.x, mouse.y), mouse.btn[MOUSE_L])

	def draw(self):
		self._draw_background()
		self.button_play.draw()
		self.button_quit.draw()
		self.button_intro.draw()

	# private
	def _draw_background(self):
		self.background.draw(0,0)

class Intro:

	def __init__(self):
		self.background = Image('./assets/img/' + 'intro_page' + '.png', (5.5, 6.1))
		self.button_quit = Button(10, 10, 300, 30, Image('./assets/img/' + 'quit' + '.png', (0.7, 0.7)), Image('./assets/img/' + 'quit_hover' + '.png', (0.7, 0.7)), Image('./assets/img/' + 'quit_click' + '.png', (0.7, 0.7)))

	def update(self, mouse):
		self.button_quit.update((mouse.x, mouse.y), mouse.btn[MOUSE_L])

	def draw(self):
		self._draw_background()
		self.button_quit.draw()


	def _draw_background(self):
		self.background.draw(0,0)




