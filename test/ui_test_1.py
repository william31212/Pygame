import sys, pygame, os
sys.path.append("../RHframework/")
sys.path.append("../")
from input import MouseHandler, KeyHandler
from utils import *
SET_ROOT('..')

from ui import *


display_width = 800
display_height = 600

class App(Window):
	def __init__(self, title, size, win_flag=W_NONE):
		super().__init__(title, size, win_flag)
		self.keyboard = KeyHandler()
		self.add_event_handle(self.keyboard.handle_event)
		self.mouse = MouseHandler()
		self.add_event_handle(self.mouse.handle_event)

	def setup(self):
		self.label = Label("Hello", (255, 0, 0), (0, 0, 0, 0), (255, 255, 255, 255))

	def update(self):
		pass

	def render(self):
		self.label.draw()

	def ask_quit(self):
		print('On quit')
		self.quit()

def main():
	app = App('example', (display_width, display_height), W_OPENGL)
	app.run()

if __name__ == '__main__':
	main()