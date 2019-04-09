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
GAME_MENU  = 0
GAME_PLAY  = 1
# GAME_CLICK = 2
GAME_INTRO = 3
GAME_ABOUT = 4

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
		self.about = About()

		######debug#######
		self.set_dbg_flag(True)
		self.toggle_dbg_draw = True
		self.toggle_dbg_print = True

	def update(self):
		keyboard = self.keyboard
		mouse = self.mouse
		game = self.game
		intro = self.intro
		# Menu
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
			elif self.menu.button_about.is_clicked():
				self.game_state = GAME_ABOUT
		# Play
		if self.game_state == GAME_PLAY:
			game.update()

			# this should refactor
			if game.home_button.is_clicked() or keyboard.key_state[KEY_ESC]:
				self.game.reset()
				self.game_state = GAME_MENU
			# TODO(roy4801): this will reveal the internal state which is *BAD*
			if game.quit_button.is_clicked():
				self.game.reset()
				self.game_state = GAME_MENU
				self.game.player.clear_point()
				self.game.gi_state = GI_PLAYING

				game.quit_button.reset() # ugly
		# Intro
		if self.game_state == GAME_INTRO:
			self.intro.update(mouse)
			if self.intro.button_quit.is_clicked():
				self.game_state = GAME_MENU
		# About
		if self.game_state == GAME_ABOUT:
			self.about.update()

			if self.about.button_quit.is_clicked():
				self.game_state = GAME_MENU

	def render(self):
		if self.game_state == GAME_PLAY:
			self.game.draw()
		if self.game_state == GAME_MENU:
			self.menu.draw()
		if self.game_state == GAME_INTRO:
			self.intro.draw()
		if self.game_state == GAME_ABOUT:
			self.about.draw()

		######debug#######
		imgui.begin('Option')
		_, self.toggle_dbg_draw = imgui.checkbox('Debug draw', self.toggle_dbg_draw)
		_, self.toggle_dbg_print = imgui.checkbox('Debug logger', self.toggle_dbg_print)
		if imgui.button('Reset game'):
			self.game.reset()

		if imgui.button('Let player 1 loses'):
			for _ in range(3):
				self.game.player.check_who_win(0, 100)
			dbprint('player 1 lose')

		state_str = {0 : 'GAME_MENU', 1 : 'GAME_PLAY', 3 : 'GAME_INTRO', 4 : 'GAME_ABOUT'}
		imgui.text('Now state = {}'.format(state_str[self.game_state]))
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
