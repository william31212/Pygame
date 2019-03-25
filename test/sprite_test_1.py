import sys, math, random
sys.path.append("../")

from window import *
from asset import *
from utils import *
from input import *

SET_ROOT('..')

sp = None

class Character:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def update(self):
		pass

	def draw(self):
		pass

class App(Window):
	def __init__(self, title, size, win_flag=W_NONE):
		super().__init__(title, size, win_flag)
		self.keyboard = KeyHandler()
		self.add_event_handle(self.keyboard.handle_event)

		self.mouse = MouseHandler()
		self.add_event_handle(self.mouse.handle_event)

	def setup(self):
		global sp
		sp = Sprite_2(SP_ANIMATE, 'stand', 15, ANI_LOOP, (0.5, 0.5))

	def update(self):
		mouse = self.mouse
		keyboard = self.keyboard

		pass

	def render(self):
		sp.draw(400, 300)
		pass

	def ask_quit(self):
		self.quit()

def main():
	app = App('image_test_1', (800, 600), W_OPENGL)
	app.run()

if __name__ == '__main__':
	main()