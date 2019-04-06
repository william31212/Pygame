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

class Game:
	def __init__(self):
		self.mouse = MouseHandler.get_mouse()
		self.keyboard = KeyHandler.get_keyboard()
		self.home_button = Button(750, 50, 50, 50, Image('./assets/img/' + 'home' + '.png', (0.2, 0.2)), Image('./assets/img/' + 'home_hover' + '.png', (0.2, 0.2)), Image('./assets/img/' + 'home_click' + '.png', (0.2, 0.2)))
		self.player = Player(250, 300, 100, 100, DIR_RIGHT, 'Player1')
		self.player2 = Player(500, 300, 100, 100, DIR_LEFT, 'Player2')
		self.bullet = Bullet(0, 0, 2, 20)
		self.bullet2 = Bullet(0, 0, 2, 20)
		self.maps = TiledMap("./level2.tmx")
		self.message1 = Label('Player1: ' + str(self.player.get_player1_point()), (160, 82, 45), [32,30,200,50], 30)
		self.message2 = Label('Player2: ' + str(self.player.get_player2_point()), (85, 107, 47), [604,30,200,50], 30)
		self.setup()

	def setup(self):
		self.maps.pick_layer()

	def update(self):
		keyboard = self.keyboard
		mouse = self.mouse
		maps = self.maps
		player = self.player
		player2 = self.player2
		bullet	= self.bullet
		bullet2	= self.bullet2

		player.store_state(0)
		player2.store_state(1)
		tmp1L = player.obs_box.to_screen_space(player.rifleman_left)
		tmp1R = player.obs_box.to_screen_space(player.rifleman_right)
		tmp2L = player2.obs_box.to_screen_space(player2.rifleman_left)
		tmp2R = player2.obs_box.to_screen_space(player2.rifleman_right)


		# click home
		# self.home_button.update((mouse.x, mouse.y), mouse.btn[MOUSE_L])
		# if self.home_button.is_clicked():
		# 	self.game_state = GAME_MENU

		# reset the game
		if player.blood_state <= 0 or player2.blood_state <= 0:
			player.reset_state(250,300)
			player2.reset_state(500,300)

		#Player 1
		# update_state(self, x, y, state, vertical, shoot)
		if keyboard.key_state[KEY_w]:
			player.update_state(player.x, player.y, player.state, 1, False)
		elif keyboard.key_state[KEY_s]:
			player.update_state(player.x, player.y, player.state, 2, False)
		elif keyboard.key_state[KEY_a]:
			player.update_state(player.x, player.y, DIR_LEFT, -1, False)
		elif keyboard.key_state[KEY_d]:
			player.update_state(player.x, player.y, DIR_RIGHT, -1, False)
		elif keyboard.key_state[KEY_v]:
			bullet.setting(player.x, player.y, player.state)
			player.update_state(player.x, player.y, player.state, -1, True)

		#Player 2
		# update_state(self, x, y, state, vertical, shoot)
		if keyboard.key_state[KEY_UP]:
			player2.update_state(player2.x, player2.y, player2.state, 1, False)
		elif keyboard.key_state[KEY_DOWN]:
			player2.update_state(player2.x, player2.y, player2.state, 2, False)
		elif keyboard.key_state[KEY_LEFT]:
			player2.update_state(player2.x, player2.y, DIR_LEFT, -1, False)
		elif keyboard.key_state[KEY_RIGHT]:
			player2.update_state(player2.x, player2.y, DIR_RIGHT, -1, False)
		elif keyboard.key_state[KEY_SLASH]:
			bullet2.setting(player2.x, player2.y, player2.state)
			player2.update_state(player2.x, player2.y, player2.state, -1, True)

		if keyboard.key_state[KEY_ESC]:
			pygame.quit()
			sys.exit()

		if keyboard.key_state[KEY_w] or keyboard.key_state[KEY_s]:
			if player.state == DIR_LEFT:
				maps.tile_object(tmp1L, player.state, player.release_state, player.blood_update, bullet.bullet_list, bullet.hit_thing, 0)
			elif player.state == DIR_RIGHT:
				maps.tile_object(tmp1R, player.state, player.release_state, player.blood_update, bullet.bullet_list, bullet.hit_thing, 0)

			if player2.state == DIR_LEFT:
				maps.tile_object(tmp2L, player2.state, player2.release_state, player2.blood_update, bullet2.bullet_list, bullet2.hit_thing, 1)
			elif player2.state == DIR_RIGHT:
				maps.tile_object(tmp2R, player2.state, player2.release_state, player2.blood_update, bullet2.bullet_list, bullet2.hit_thing, 1)


			time.sleep(0.2)

		if player.x <= 50:
			player.x = 50
		if player.y <= 30:
			player.y = 30
		if player.x >= 750:
			player.x = 750
		if player.y >= 600:
			player.y = 600

		if player2.x <= 50:
			player2.x = 50
		if player2.y <= 30:
			player2.y = 30
		if player2.x >= 750:
			player2.x = 750
		if player2.y >= 600:
			player2.y = 600

		if player.state == DIR_LEFT:
			bullet.hit_people(player2.atk_box.to_screen_space(player2.rifleman_left), player2.blood_update, player2.blood_state)
		elif player.state == DIR_RIGHT:
			bullet.hit_people(player2.atk_box.to_screen_space(player2.rifleman_right), player2.blood_update, player2.blood_state)

		if player2.state == DIR_LEFT:
			bullet2.hit_people(player.atk_box.to_screen_space(player.rifleman_left), player.blood_update, player.blood_state)
		elif player2.state == DIR_RIGHT:
			bullet2.hit_people(player.atk_box.to_screen_space(player.rifleman_right), player.blood_update, player.blood_state)

		bullet.out_of_bound(Window.get_width(), Window.get_height())
		bullet2.out_of_bound(Window.get_width(), Window.get_height())

		# print(player.x, player.y)
		player.check_who_win(player.blood_state, player2.blood_state)

	def draw(self):
		maps = self.maps
		player = self.player
		player2 = self.player2
		bullet = self.bullet
		bullet2 = self.bullet2
		home_button = self.home_button

		maps.draw([player.draw_character,player2.draw_character])
		bullet.draw()
		bullet2.draw()
		self.message1.draw()
		self.message2.draw()
		home_button.draw()
		# player.game_over(player.blood_state, 1)
		# player2.game_over(player2.blood_state, 2)

		# lu = player.rifleman_right.get_left_upper()
		# print(player.state, player2.state,player.rifleman_left,player.rifleman_right)

	def dbg_draw(self):
		player = self.player
		player2 = self.player2
		self.maps.dbg_draw_tile_object()

		if player.state == DIR_LEFT:
			draw_premitive.rect((0, 0, 0xff, 200), player.obs_box.to_screen_space(player.rifleman_left).get_tuple(), 2)
			draw_premitive.rect((0xca, 0x0a, 0xff, 200), player.atk_box.to_screen_space(player.rifleman_left).get_tuple(), 2)
		if player.state == DIR_RIGHT:
			draw_premitive.rect((0, 0, 0xff, 200), player.obs_box.to_screen_space(player.rifleman_right).get_tuple(), 2)
			draw_premitive.rect((0xca, 0x0a, 0xff, 200), player.atk_box.to_screen_space(player.rifleman_right).get_tuple(), 2)

		if player2.state == DIR_LEFT:
			draw_premitive.rect((0, 0, 0xff, 200), player2.obs_box.to_screen_space(player2.rifleman_left).get_tuple(), 2)
			draw_premitive.rect((0xca, 0x0a, 0xff, 200), player2.atk_box.to_screen_space(player2.rifleman_left).get_tuple(), 2)
		if player2.state == DIR_RIGHT:
			draw_premitive.rect((0, 0, 0xff, 200), player2.obs_box.to_screen_space(player2.rifleman_right).get_tuple(), 2)
			draw_premitive.rect((0xca, 0x0a, 0xff, 200), player2.atk_box.to_screen_space(player2.rifleman_right).get_tuple(), 2)