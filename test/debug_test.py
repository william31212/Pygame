import sys, math
sys.path.append("../RHframework")

from window import *
from asset import *
from utils import *
from input import *

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

		imgui.show_test_window()
		pass

	def render(self):
		pass

	def ask_quit(self):
		pass
		self.quit()

def main():
	app = App('image_test_1', (800, 600), W_OPENGL)
	app.run()


if __name__ == '__main__':
	main()