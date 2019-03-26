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
display_height = 600

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
		# self.maps = TiledMap("./level2.tmx", gameDisplay)
		# self.maps.pick_layer()

	def update(self):
		keyboard = self.keyboard
		maps = self.maps
		player = self.player
		#
		player.store_state()

		if keyboard.key_state[KEY_UP]:
			player.update_state(player.x, player.y, 1)
		if keyboard.key_state[KEY_DOWN]:
			player.update_state(player.x, player.y, 2)
		if keyboard.key_state[KEY_LEFT]:
			player.update_state(player.x, player.y, 3)
		if keyboard.key_state[KEY_RIGHT]:
			player.update_state(player.x, player.y, 4)
		if keyboard.key_state[KEY_ESC]:
			pygame.quit()
			sys.exit()

		# maps.tile_object(player.obs_box, player.state, player.release_state)
		if player.x <= -30:
			player.x = 760
		elif player.y <= -30:
			player.y = 640
		elif player.x >= 760:
			player.x = -30
		elif player.y >= 640:
			player.y = -30
		pass

	def render(self):
		maps = self.maps
		# maps.draw(player.draw_character)
		self.player.draw_character()

		# draw_premitive.rect((255, 0, 0), (0, 0, 100, 100), 1)
		# draw_premitive.circle((0, 255, 0), [0, 0], 100)
		# draw_premitive.line((255, 0, 0), (0, 0), (800, 600))
		draw_premitive.lines((255, 0, 0), False, [(0, 0), (30, 70), (100, 100), (250, 300), (800, 600)])
		pass

	def ask_quit(self):
		print('On quit')
		self.quit()


def main():
	app = App('rifleman', (display_width, display_height), W_OPENGL)
	app.run()

if __name__ == '__main__':
	main()