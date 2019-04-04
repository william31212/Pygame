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

display_width = 800
display_height = 640

GAME_LEAVE = -1
GAME_MENU = 0
GAME_PLAY = 1
GAME_CLICK = 2

class App(Window):
	def __init__(self, title, size, win_flag=W_NONE):
		super().__init__(title, size, win_flag)
		self.keyboard = KeyHandler()
		self.add_event_handle(self.keyboard.handle_event)
		self.mouse = MouseHandler()
		self.add_event_handle(self.mouse.handle_event)
		self.player = None
		self.maps = None
		self.game_state = GAME_MENU


	def setup(self):
		self.player = Player(250, 300, 100, 100, 2, 'Player1')
		self.player2 = Player(500, 300, 100, 100, 2, 'Player2')
		self.bullet = Bullet(0, 0, 2, 20)
		self.bullet2 = Bullet(0, 0, 2, 20)
		self.message1 = Label('Player1: ' + str(self.player.get_player1_point()), (160, 82, 45), [32,30,200,50], 30)
		self.message2 = Label('Player2: ' + str(self.player.get_player2_point()), (85, 107, 47), [604,30,200,50], 30)
		self.home_button = Button(750, 50, 50, 50, Image('./assets/img/' + 'home' + '.png', (0.2, 0.2)), Image('./assets/img/' + 'home_hover' + '.png', (0.2, 0.2)), Image('./assets/img/' + 'home_click' + '.png', (0.2, 0.2)))
		self.maps = TiledMap("./level2.tmx")
		self.maps.pick_layer()
		self.menu = Menu()

	def update(self):

		keyboard = self.keyboard
		maps = self.maps
		player = self.player
		player2 = self.player2
		bullet	= self.bullet
		bullet2	= self.bullet2
		mouse = self.mouse
		self.message1 = Label('Player1: ' + str(self.player.get_player1_point()), (160, 82, 45), [32,30,200,50], 30)
		self.message2 = Label('Player2: ' + str(self.player.get_player2_point()), (85, 107, 47), [604,30,200,50], 30)

		if self.game_state == GAME_MENU:
			self.menu.update(mouse)
			# btn_click
			# TODO(roy4801): ugly
			if self.menu.button_play.is_clicked():
				self.game_state = GAME_PLAY
			elif self.menu.button_quit.is_clicked():
				self.ask_quit()

		elif self.game_state == GAME_PLAY:
			player.store_state(0)
			player2.store_state(1)

			# click home
			self.home_button.update((mouse.x, mouse.y), mouse.btn[MOUSE_L])
			if self.home_button.is_clicked():
				self.game_state = GAME_MENU

			# reset the game
			if player.blood_state <= 0 or player2.blood_state <= 0:
				player.reset_state(250,300)
				player2.reset_state(500,300)

			#Player 1
			if keyboard.key_state[KEY_w]:
				player.update_state(player.x, player.y, 1, False)
			if keyboard.key_state[KEY_s]:
				player.update_state(player.x, player.y, 2, False)
			if keyboard.key_state[KEY_a]:
				player.update_state(player.x, player.y, 3, False)
			if keyboard.key_state[KEY_d]:
				player.update_state(player.x, player.y, 4, False)
			if keyboard.key_state[KEY_v]:
				bullet.setting(player.x, player.y, player.state)
				player.update_state(player.x, player.y, player.state, True)
			# elif keyboard.key_state[KEY_b]:
			# 	bullet.setting(player.x, player.y, 1)
			# 	player.update_state(player.x, player.y, 6)

			#Player 2
			if keyboard.key_state[KEY_UP]:
				player2.update_state(player2.x, player2.y, 1, False)
			if keyboard.key_state[KEY_DOWN]:
				player2.update_state(player2.x, player2.y, 2, False)
			if keyboard.key_state[KEY_LEFT]:
				player2.update_state(player2.x, player2.y, 3, False)
			if keyboard.key_state[KEY_RIGHT]:
				player2.update_state(player2.x, player2.y, 4, False)
			if keyboard.key_state[KEY_PERIOD]:
				bullet2.setting(player2.x, player2.y, player2.state)
				player2.update_state(player2.x, player2.y, player2.state, True)
			# elif keyboard.key_state[KEY_SLASH]:
			# 	bullet2.setting(player2.x, player2.y, 1)
			# 	player2.update_state(player2.x, player2.y, 6)

			if keyboard.key_state[KEY_ESC]:
				pygame.quit()
				sys.exit()


			maps.tile_object(player.obs_box, player.state, player.release_state, player.blood_update, bullet.bullet_list, bullet.hit_thing, 0)
			maps.tile_object(player2.obs_box, player2.state, player2.release_state, player2.blood_update, bullet2.bullet_list, bullet2.hit_thing, 1)

			if player.x <= 0:
				player.x = 0
			elif player.y <= 0:
				player.y = 0
			elif player.x >= 800:
				player.x = 800
			elif player.y >= 600:
				player.y = 600

			if player2.x <= 0:
				player2.x = 0
			elif player2.y <= 0:
				player2.y = 0
			elif player2.x >= 800:
				player2.x = 800
			elif player2.y >= 800:
				player2.y = 800

			bullet.hit_people(player2.atk_box, player2.blood_update, player2.blood_state)
			bullet2.hit_people(player.atk_box, player.blood_update, player.blood_state)
			bullet.out_of_bound(display_width, display_height)
			bullet2.out_of_bound(display_width, display_height)
			player.store_clear()

			print(player.blood_state, player2.blood_state)
			player.check_who_win(player.blood_state, player2.blood_state)


	def render(self):
		maps = self.maps
		player = self.player
		player2 = self.player2
		bullet = self.bullet
		bullet2 = self.bullet2
		home_button = self.home_button


		if self.game_state == GAME_PLAY:
			maps.draw([player.draw_character,player2.draw_character])
			bullet.draw()
			bullet2.draw()
			self.message1.draw()
			self.message2.draw()
			home_button.draw()
			# player.game_over(player.blood_state, 1)
			# player2.game_over(player2.blood_state, 2)

		elif self.game_state == GAME_MENU:
			self.menu.draw()


		######debug#######
		# player.draw_character()
		# print()
		# draw_premitive.rect((0, 255, 0), (self.player.obs_box.x, self.player.obs_box.y, self.player.obs_box.wid, self.player.obs_box.hei), 2)
		# maps.dbg_draw_tile_object()

	def ask_quit(self):
		print('On quit')
		self.quit()

def main():
	app = App('rifleman', (display_width, display_height), W_OPENGL)
	app.run()


if __name__ == '__main__':
	main()
