import sys, pygame
sys.path.append("./RHframework")

from clock import Clock
from input import *
from asset import *
from utils import *
from tile import *
from shape import *
from window import *
import draw_premitive
#
from player import *
from bullet import *
from ui import *
from menu import *
from game import *

display_width = 800
display_height = 640

GAME_LEAVE = -1
GAME_MENU = 0
GAME_PLAY = 1
GAME_CLICK = 2

class App(Window):
	def __init__(self, title, size, win_flag=W_NONE):
		super().__init__(title, size, win_flag)
		self.keyboard = KeyHandler.get_keyboard()
		self.add_event_handle(self.keyboard.handle_event)
		self.mouse = MouseHandler.get_mouse()
		self.add_event_handle(self.mouse.handle_event)
		self.game_state = GAME_MENU

	def setup(self):
		self.game = Game()
		self.menu = Menu()

	def update(self):
		keyboard = self.keyboard
		mouse = self.mouse

		if self.game_state == GAME_MENU:
			self.menu.update(mouse)
			# btn_click
			# TODO(roy4801): ugly
			if self.menu.button_play.is_clicked():
				self.game_state = GAME_PLAY
			elif self.menu.button_quit.is_clicked():
				self.ask_quit()

		elif self.game_state == GAME_PLAY:
			self.game.update()

	def render(self):
		if self.game_state == GAME_PLAY:
			self.game.draw()
		elif self.game_state == GAME_MENU:
			self.menu.draw()

		######debug#######
		if self.game_state == GAME_PLAY:
			self.game.dbg_draw()

	def ask_quit(self):
		print('On quit')
		self.quit()

def main():
	app = App('rifleman', (display_width, display_height), W_OPENGL)
	app.run()

if __name__ == '__main__':
	main()
