import sys
sys.path.append("../")
from window import *
from asset import *
from utils import *

SET_ROOT('..')

image_1 = None

class App(Window):
	def __init__(self, title, size, win_flag=W_NONE):
		super().__init__(title, size, win_flag)

	def setup(self):
		print('On setup')
		global image_1
		image_1 = Image_2(GET_PATH(IMG_SPRITE, 'attackA000.png'))

	def update(self):
		# print('On update')
		pass

	def render(self):
		image_1.draw(0, 0)

	def ask_quit(self):
		print('On quit')
		self.quit()

def main():
	app = App('image_test_1', (800, 600), W_OPENGL)
	app.run()

if __name__ == '__main__':
	main()