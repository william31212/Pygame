import sys, math
sys.path.append("../")

from window import *
from asset import *
from utils import *
from input import *

import random

SET_ROOT('..')

ball_list = []
ball_image = None
move_unit = 10

class Ball:
	def __init__(self, pos):
		self.x = pos[0]
		self.y = pos[1]
		self.theta = random.uniform(0, 360)
	def update(self):
		rad = math.radians(self.theta)
		self.x += int(move_unit * math.cos(rad))
		self.y += int(move_unit * math.sin(rad))
	def draw(self):
		ball_image.draw(self.x, self.y)

class App(Window):
	def __init__(self, title, size, win_flag=W_NONE):
		super().__init__(title, size, win_flag)
		self.keyboard = KeyHandler()
		self.add_event_handle(self.keyboard.handle_event)

		self.mouse = MouseHandler()
		self.add_event_handle(self.mouse.handle_event)

	def setup(self):
		global ball_image
		ball_image = Image('ball.png', (1, 1), 0, (0.5, 0.5))

	def update(self):
		mouse = self.mouse
		keyboard = self.keyboard

		for _ in range(10):
			ball_list.append(Ball((random.randint(0, 800), random.randint(0, 600))))

		for b in ball_list:
			b.update()

			if b.x < 0 or b.x > 800 or b.y < 0 or b.y > 600:
				ball_list.remove(b)

	def render(self):
		for b in ball_list:
			b.draw()

	def ask_quit(self):
		print('On quit')
		glDeleteTextures([ball_image.img])
		self.quit()

def main():
	app = App('image_test_1', (800, 600), W_OPENGL)
	app.run()


if __name__ == '__main__':
	main()