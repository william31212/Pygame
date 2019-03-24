import sys
sys.path.append("../")
from window import *

class App(Window):
	def __init__(self, title, size, win_flag=W_NONE):
		super().__init__(title, size, win_flag)

	def setup(self):
		print('On setup')

	def update(self):
		print('On update')

	def render(self):
		print('On render')

	def ask_quit(self):
		print('On quit')
		self.quit()


def main():
	app = App('window_test_1', (800, 600))
	app.run()

if __name__ == '__main__':
	main()