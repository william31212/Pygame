import sys, pygame

sys.path.append("../")
from clock import Clock
from input import *
from asset import *
from utils import *
from tile import *
from shape import *
from player import *
from window import *
import draw_premitive

SET_ROOT('..')

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
		self.player = Player(0, 0, 100, 100, 2)
		self.player2 = Player(300, 500, 100, 100, 2)
		self.maps = TiledMap("./level2.tmx")
		self.maps.pick_layer()

	def update(self):
		keyboard = self.keyboard
		maps = self.maps
		player = self.player
		player2 = self.player2

		player.store_state(0)
		player2.store_state(1)


		if keyboard.key_state[KEY_UP]:
			player.update_state(player.x, player.y, 1)
		if keyboard.key_state[KEY_DOWN]:
			player.update_state(player.x, player.y, 2)
		if keyboard.key_state[KEY_LEFT]:
			player.update_state(player.x, player.y, 3)
		if keyboard.key_state[KEY_RIGHT]:
			player.update_state(player.x, player.y, 4)
		if keyboard.key_state[KEY_SPACE]:
			player.update_state(player.x, player.y, 5)
		if keyboard.key_state[KEY_b]:
			player.update_state(player.x, player.y, 6)

		if keyboard.key_state[KEY_w]:
			player2.update_state(player2.x, player2.y, 1)
		if keyboard.key_state[KEY_s]:
			player2.update_state(player2.x, player2.y, 2)
		if keyboard.key_state[KEY_a]:
			player2.update_state(player2.x, player2.y, 3)
		if keyboard.key_state[KEY_d]:
			player2.update_state(player2.x, player2.y, 4)

		if keyboard.key_state[KEY_ESC]:
			pygame.quit()
			sys.exit()


		maps.tile_object(player.obs_box, player.state, player.release_state,0)
		maps.tile_object(player2.obs_box, player2.state, player2.release_state,1)

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


	def render(self):
		maps = self.maps
		player = self.player
		player2 = self.player2


		maps.draw([player.draw_character,player2.draw_character])

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