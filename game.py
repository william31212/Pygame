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
from sound import *
from input import *


GI_PLAYING = 1
GI_Player1_win = 2
GI_Player2_win = 3

class Game:
	def __init__(self):
		self.mouse = MouseHandler.get_mouse()
		self.keyboard = KeyHandler.get_keyboard()
		self.home_button = Button(750, 50, 50, 50, Image('./assets/img/' + 'home' + '.png', (0.2, 0.2)), Image('./assets/img/' + 'home_hover' + '.png', (0.2, 0.2)), Image('./assets/img/' + 'home_click' + '.png', (0.2, 0.2)))
		self.gi_state = GI_PLAYING

		self.bgm = Sound(GET_PATH(MUSIC_MAIN, 'battle1.wav'), S_PLAY_INF, 0.7)

		# win_message
		self.is_player1_win = Label('Player1 WIN ', (160, 82, 45), [125,300,500,0], 100)
		self.is_player2_win = Label('Player2 WIN ', (160, 82, 45), [125,300,500,0], 100)
		self.quit_button = Button(300, 500, 150, 50, Image('./assets/img/' + 'quit' + '.png', (0.5, 0.5)), Image('./assets/img/' + 'quit_hover' + '.png', (0.5, 0.5)), Image('./assets/img/' + 'quit_click' + '.png', (0.5, 0.5)))
		self.renew_button = Button(500, 500, 150, 50, Image('./assets/img/' + 'renew' + '.png', (0.5, 0.5)), Image('./assets/img/' + 'renew_hover' + '.png', (0.5, 0.5)), Image('./assets/img/' + 'renew_click' + '.png', (0.5, 0.5)))

		# player
		self.player = Player(250, 300, 100, 100, DIR_RIGHT, 'Player1')
		self.player2 = Player(500, 300, 100, 100, DIR_LEFT, 'Player2')
		self.player.set_key_map([KEY_w, KEY_s, KEY_a, KEY_d, KEY_v])
		self.player2.set_key_map([KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT, KEY_SLASH])

		self.bullet = Bullet(0, 0, 2, 20)
		self.bullet2 = Bullet(0, 0, 2, 20)
		self.maps = TiledMap("./level2.tmx")
		self.message1 = None
		self.message2 = None
		self.setup()

	def setup(self):
		self.maps.pick_layer()

	def reset(self):
		self.player.reset_state(250,300)
		self.player2.reset_state(500,300)

	def update(self):
		keyboard = self.keyboard
		mouse = self.mouse
		maps = self.maps
		player = self.player
		player2 = self.player2
		bullet	= self.bullet
		bullet2	= self.bullet2
		self.message1 = Label('Player1: ' + str(self.player.get_player1_point()), (160, 82, 45), [32,30,200,50], 30)
		self.message2 = Label('Player2: ' + str(self.player.get_player2_point()), (85, 107, 47), [604,30,200,50], 30)

		if not self.bgm.is_playing():
			self.bgm.play()

		if self.gi_state == GI_PLAYING:
			player.store_state(0)
			player2.store_state(1)

			self.home_button.update((mouse.x, mouse.y), mouse.btn[MOUSE_L])

			player.update(bullet)
			player2.update(bullet2)

			# collision
			if player.state == DIR_LEFT:
				maps.tile_object(player.obs_box.to_screen_space(player.get_pos(), player.rifleman_left), player.state, player.release_state, player.blood_update, bullet.bullet_list, bullet.hit_thing, 0)
			elif player.state == DIR_RIGHT:
				maps.tile_object(player.obs_box.to_screen_space(player.get_pos(), player.rifleman_right), player.state, player.release_state, player.blood_update, bullet.bullet_list, bullet.hit_thing, 0)

			if player2.state == DIR_LEFT:
				maps.tile_object(player2.obs_box.to_screen_space(player2.get_pos(), player2.rifleman_left), player2.state, player2.release_state, player2.blood_update, bullet2.bullet_list, bullet2.hit_thing, 1)
			elif player2.state == DIR_RIGHT:
				maps.tile_object(player2.obs_box.to_screen_space(player2.get_pos(), player2.rifleman_right), player2.state, player2.release_state, player2.blood_update, bullet2.bullet_list, bullet2.hit_thing, 1)

			if player.state == DIR_LEFT:
				bullet.hit_people(player2.atk_box.to_screen_space(player2.get_pos(), player2.rifleman_left), player2.blood_update, player2.blood_state)
			elif player.state == DIR_RIGHT:
				bullet.hit_people(player2.atk_box.to_screen_space(player2.get_pos(), player2.rifleman_right), player2.blood_update, player2.blood_state)

			if player2.state == DIR_LEFT:
				bullet2.hit_people(player.atk_box.to_screen_space(player.get_pos(), player.rifleman_left), player.blood_update, player.blood_state)
			elif player2.state == DIR_RIGHT:
				bullet2.hit_people(player.atk_box.to_screen_space(player.get_pos(), player.rifleman_right), player.blood_update, player.blood_state)

			bullet.out_of_bound(Window.get_width(), Window.get_height())
			bullet2.out_of_bound(Window.get_width(), Window.get_height())
			player.store_clear()

			if player.check_who_win(player.blood_state, player2.blood_state) == True:
				self.reset()
			if player.is_game_over(3) == 1:
				self.gi_state = GI_Player1_win
				player.clear_point()
			elif player2.is_game_over(3) == 2:
				self.gi_state = GI_Player2_win
				player2.clear_point()

		elif self.gi_state == GI_Player1_win or self.gi_state == GI_Player2_win:
			if self.renew_button.is_clicked():
				self.reset()
				self.player.clear_point()
				self.gi_state = GI_PLAYING

			self.quit_button.update((mouse.x, mouse.y), mouse.btn[MOUSE_L])
			self.renew_button.update((mouse.x, mouse.y), mouse.btn[MOUSE_L])


	def draw(self):
		maps = self.maps
		player = self.player
		player2 = self.player2
		bullet = self.bullet
		bullet2 = self.bullet2
		home_button = self.home_button

		if self.gi_state == GI_Player1_win or self.gi_state == GI_Player2_win:
			maps.draw([player.draw_character,player2.draw_character])
			if self.gi_state == GI_Player1_win:
				self.is_player1_win.draw()
			elif self.gi_state == GI_Player2_win:
				self.is_player2_win.draw()
			self.quit_button.draw()
			self.renew_button.draw()

		elif self.gi_state == GI_PLAYING:
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

	def stop_bgm_if_needed(self):
		if self.bgm.is_playing():
			self.bgm.fade_out(100)

	def dbg_draw(self):
		player = self.player
		player2 = self.player2
		self.maps.dbg_draw_tile_object()

		if player.state == DIR_LEFT:
			player.obs_box.to_screen_space(player.get_pos(), player.rifleman_left).dbg_draw((0, 0, 0xff, 200))
			player.atk_box.to_screen_space(player.get_pos(), player.rifleman_left).dbg_draw((0xca, 0x0a, 0xff, 200))
		if player.state == DIR_RIGHT:
			player.obs_box.to_screen_space(player.get_pos(), player.rifleman_right).dbg_draw((0, 0, 0xff, 200))
			player.atk_box.to_screen_space(player.get_pos(), player.rifleman_right).dbg_draw((0xca, 0x0a, 0xff, 200))

		if player2.state == DIR_LEFT:
			player2.obs_box.to_screen_space(player2.get_pos(), player2.rifleman_left).dbg_draw((0, 0, 0xff, 200))
			player2.atk_box.to_screen_space(player2.get_pos(), player2.rifleman_left).dbg_draw((0xca, 0x0a, 0xff, 200))
		if player2.state == DIR_RIGHT:
			player2.obs_box.to_screen_space(player2.get_pos(), player2.rifleman_right).dbg_draw((0, 0, 0xff, 200))
			player2.atk_box.to_screen_space(player2.get_pos(), player2.rifleman_right).dbg_draw((0xca, 0x0a, 0xff, 200))