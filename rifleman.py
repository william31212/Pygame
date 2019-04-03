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
from Bullet import *
from ui import *

display_width = 800
display_height = 640

class App(Window):
	def __init__(self, title, size, win_flag=W_NONE):
		super().__init__(title, size, win_flag)
		self.keyboard = KeyHandler()
		self.add_event_handle(self.keyboard.handle_event)
		self.mouse = MouseHandler()
		self.add_event_handle(self.mouse.handle_event)
		self.player = None
		self.maps = None

	def setup(self):
		self.player = Player(600, 600, 100, 100, 2, 'Player1')
		self.player2 = Player(0, 0, 100, 100, 2, 'Player2')
		self.bullet = Bullet(0, 0, 2, 20)
		self.bullet2 = Bullet(0, 0, 2, 20)
		self.maps = TiledMap("./level2.tmx")
		self.maps.pick_layer()

	def update(self):
		keyboard = self.keyboard
		maps = self.maps
		player = self.player
		player2 = self.player2
		bullet	= self.bullet
		bullet2	= self.bullet2

		player.store_state(0)
		player2.store_state(1)

		#Player 1
		if keyboard.key_state[KEY_UP]:
			player.update_state(player.x, player.y, 1)
		if keyboard.key_state[KEY_DOWN]:
			player.update_state(player.x, player.y, 2)
		if keyboard.key_state[KEY_LEFT]:
			player.update_state(player.x, player.y, 3)
		if keyboard.key_state[KEY_RIGHT]:
			player.update_state(player.x, player.y, 4)
		if keyboard.key_state[KEY_PERIOD]:
			bullet.setting(player.x, player.y, 0)
			player.update_state(player.x, player.y, 5)
		if keyboard.key_state[KEY_SLASH]:
			bullet.setting(player.x, player.y, 1)
			player.update_state(player.x, player.y, 6)

		#Player 2
		if keyboard.key_state[KEY_w]:
			player2.update_state(player2.x, player2.y, 1)
		if keyboard.key_state[KEY_s]:
			player2.update_state(player2.x, player2.y, 2)
		if keyboard.key_state[KEY_a]:
			player2.update_state(player2.x, player2.y, 3)
		if keyboard.key_state[KEY_d]:
			player2.update_state(player2.x, player2.y, 4)
		if keyboard.key_state[KEY_v]:
			bullet2.setting(player2.x, player2.y, 0)
			player2.update_state(player2.x, player2.y, 5)
		if keyboard.key_state[KEY_b]:
			bullet2.setting(player2.x, player2.y, 1)
			player2.update_state(player2.x, player2.y, 6)

		if keyboard.key_state[KEY_ESC]:
			pygame.quit()
			sys.exit()

		maps.tile_object(player.obs_box, player.state, player.release_state, player.blood_update, bullet.bullet_list, bullet.hit_thing, 0)
		maps.tile_object(player2.obs_box, player2.state, player2.release_state, player2.blood_update, bullet2.bullet_list, bullet2.hit_thing, 1)

		if player.x <= -30:
			player.x = 760
		elif player.y <= -30:
			player.y = 640
		elif player.x >= 760:
			player.x = -30
		elif player.y >= 640:
			player.y = -30

		if player2.x <= -30:
			player2.x = 760
		elif player2.y <= -30:
			player2.y = 640
		elif player2.x >= 760:
			player2.x = -30
		elif player2.y >= 640:
			player2.y = -30

		player.store_clear()
		bullet.hit_people(player2.atk_box, player2.blood_update, player2.blood_state)
		bullet2.hit_people(player.atk_box, player.blood_update, player.blood_state)

	def render(self):
		maps = self.maps
		player = self.player
		player2 = self.player2
		bullet = self.bullet
		bullet2 = self.bullet2

		maps.draw([player.draw_character,player2.draw_character])
		bullet.shoot()
		bullet2.shoot()
		# player.game_over(player.blood_state, 1)
		# player2.game_over(player2.blood_state, 2)

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