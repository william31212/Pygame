import sys, math, random
sys.path.append("../")

from window import *
from asset import *
from utils import *
from input import *

import draw_premitive

pos_rect = []

SET_ROOT('..')

class App(Window):
	def __init__(self, title, size, win_flag=W_NONE):
		super().__init__(title, size, win_flag)
		self.keyboard = KeyHandler()
		self.add_event_handle(self.keyboard.handle_event)

		self.mouse = MouseHandler()
		self.add_event_handle(self.mouse.handle_event)

	def setup(self):
		pass

	def update(self):
		mouse = self.mouse
		keyboard = self.keyboard

		if mouse.btn[MOUSE_L]:
			pos_rect.append([(mouse.x, mouse.y), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))])

	def render(self):
		draw_premitive.rect((255, 0, 0), (0, 0, 100, 100))
		draw_premitive.rect((0, 255, 0), (100, 0, 100, 100))

		draw_premitive.circle((255, 0, 0), (300, 300), 128)
		draw_premitive.circle((0, 255, 0), (245, 248), 16)
		draw_premitive.circle((0, 255, 0), (352, 253), 16)

		draw_premitive.line((0x19, 0x19, 0x70), (400, 300), (300, 400), 5)

		for i in pos_rect:
			draw_premitive.circle(i[1], i[0], 8)

	def ask_quit(self):
		self.quit()

def main():
	app = App('image_test_1', (800, 600), W_OPENGL)
	app.run()

if __name__ == '__main__':
	main()