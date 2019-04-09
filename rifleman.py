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
GAME_INTRO = 3

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
		self.intro = Intro()

		######debug#######
		self.set_dbg_flag(True)
		self.toggle_dbg_draw = True
		self.toggle_dbg_print = True

		self.cnt = 0

	def update(self):
		keyboard = self.keyboard
		mouse = self.mouse
		game = self.game
		intro = self.intro

		dbprint('hello {}'.format(self.cnt))
		self.cnt += 1

		if self.game_state == GAME_MENU:
			self.menu.update(mouse)
			# btn_click
			# TODO(roy4801): ugly
			if self.menu.button_play.is_clicked():
				self.game_state = GAME_PLAY
			elif self.menu.button_quit.is_clicked():
				self.ask_quit()
			elif self.menu.button_intro.is_clicked():
				self.game_state = GAME_INTRO

		if self.game_state == GAME_PLAY:
			game.update()

			if game.home_button.is_clicked():
				self.game.reset()
				self.game_state = GAME_MENU

		if self.game_state == GAME_INTRO:
			self.intro.update(mouse)
			if self.intro.button_quit.is_clicked():
				self.game_state = GAME_MENU

	def render(self):
		if self.game_state == GAME_PLAY:
			self.game.draw()
		if self.game_state == GAME_MENU:
			self.menu.draw()
		if self.game_state == GAME_INTRO:
			self.intro.draw()

		######debug#######
		imgui.begin('Option')
		_, self.toggle_dbg_draw = imgui.checkbox('Debug draw', self.toggle_dbg_draw)
		_, self.toggle_dbg_print = imgui.checkbox('Debug logger', self.toggle_dbg_print)
		if imgui.button('Reset game'):
			self.game.reset()
		imgui.end()

		if self.toggle_dbg_draw:
			if self.game_state == GAME_PLAY:
				self.game.dbg_draw()

		if self.toggle_dbg_print:
			dbg_print.get_dbg_print().draw()

	def ask_quit(self):
		print('On quit')
		self.quit()

def main():
	app = App('rifleman', (display_width, display_height), W_OPENGL)
	app.run()

if __name__ == '__main__':
	main()
