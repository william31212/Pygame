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
	def __init__(self):
		self.background = Image('./assets/img/' + 'start2' + '.png', (5.95, 7.85))
		self.button_play = Button(50, 450, 300, 70, Image('./assets/img/' + 'play' + '.png', (1.0, 1.0)), Image('./assets/img/' + 'play_hover' + '.png', (1.0, 1.0)), Image('./assets/img/' + 'play_click' + '.png', (1.0, 1.0)))
		self.button_quit = Button(450, 450, 300, 70, Image('./assets/img/' + 'quit' + '.png', (1.0, 1.0)), Image('./assets/img/' + 'quit_hover' + '.png', (1.0, 1.0)), Image('./assets/img/' + 'quit_click' + '.png', (1.0, 1.0)))

	def click(self, x, y, btn):
		if btn == True:
			if self.button_play.update([x, y], btn) == 0:
					return 1
			elif self.button_quit.update([x, y], btn) == 0:
					return -1

	def draw_background(self):
		self.background.draw(0,0)

	def draw_button(self, x, y, click):
			#hover
			if self.button_play.update([x, y], click) == 1:
				self.button_play.hover_draw(self.button_play.x, self.button_play.y)
				self.button_quit.normal_draw(self.button_quit.x, self.button_quit.y)

			elif self.button_quit.update([x, y], click) == 1:
				self.button_play.normal_draw(self.button_play.x, self.button_play.y)
				self.button_quit.hover_draw(self.button_quit.x, self.button_quit.y)

			elif self.button_play.update([x, y], click) == 0:
				self.button_play.click_draw(self.button_play.x, self.button_play.y)
				self.button_quit.normal_draw(self.button_quit.x, self.button_quit.y)

			elif self.button_quit.update([x, y], click) == 0:
				self.button_play.normal_draw(self.button_play.x, self.button_play.y)
				self.button_quit.click_draw(self.button_quit.x, self.button_quit.y)

			else:
				self.button_play.normal_draw(self.button_play.x, self.button_play.y)
				self.button_quit.normal_draw(self.button_quit.x, self.button_quit.y)

