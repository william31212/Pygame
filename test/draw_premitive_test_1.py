import sys, math, random
sys.path.append("../RHframework")

from window import *
from asset import *
from utils import *
from input import *

import draw_premitive

shape_list = []

S_CIRCLE = 0
S_RECT   = 1

class shape:
	def __init__(self, shape_type):
		self.type = shape_type
	def __setattr__(self, name, value):
		self.__dict__[name] = value

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

		if keyboard.key_state[KEY_a]:
			for _ in range(5):
				cir = shape(S_CIRCLE)
				cir.pos = (random.randint(0, 800), random.randint(0, 600))
				cir.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
				cir.radius = random.randint(1, 16)
				shape_list.append(cir)

				rect = shape(S_RECT)
				rect.pos = (random.randint(0, 800), random.randint(0, 600))
				rect.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
				rect.size = (random.randint(1, 100), random.randint(1, 100))
				shape_list.append(rect)
				

	def render(self):
		draw_premitive.rect((255, 0, 0, 128), (0, 0, 100, 100))
		draw_premitive.rect((0, 255, 0, 128), (50, 0, 100, 100))

		draw_premitive.circle((255, 0, 0, 128), (300, 300), 128)
		draw_premitive.circle((0, 255, 0, 128), (245, 248), 16)
		draw_premitive.circle((0, 255, 0, 128), (352, 253), 16)

		draw_premitive.line((0x19, 0x19, 0x70, 128), (400, 300), (300, 400), 5)

		for i in shape_list:
			if i.type == S_CIRCLE:
				draw_premitive.circle(i.color, i.pos, i.radius)
			elif i.type == S_RECT:
				draw_premitive.rect(i.color, (*i.pos, *i.size))

	def ask_quit(self):
		self.quit()

def main():
	app = App('image_test_1', (800, 600), W_OPENGL)
	app.run()

if __name__ == '__main__':
	main()