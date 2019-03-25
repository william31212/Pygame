import sys
sys.path.append("../")
from window import *
from asset import *
from utils import *

import random

SET_ROOT('..')

image = []
pos = []
num = 1000

class App(Window):
	def __init__(self, title, size, win_flag=W_NONE):
		super().__init__(title, size, win_flag)

	def setup(self):
		print('On setup')
		for i in range(num):
			image.append(Image_2(GET_PATH(IMG_SPRITE, 'attackA000.png'), (1, 1), cent_pos=(0.5, 0.5)))
			pos.append((random.randint(0, self.size[0]), random.randint(0, self.size[1])))

	def update(self):
		# print('On update')
		pass

	def render(self):
		for i in range(num):
			image[i].draw(pos[i][0], pos[i][1])

	def ask_quit(self):
		print('On quit')
		self.quit()

def main():
	app = App('image_test_1', (800, 600), W_OPENGL)
	app.run()

if __name__ == '__main__':
	main()