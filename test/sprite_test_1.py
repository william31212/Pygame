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
		self.sp = sp.copy()

	def update(self):
		pass

	def draw(self):
		self.sp.draw(self.x, self.y)

class App(Window):
	def __init__(self, title, size, win_flag=W_NONE):
		super().__init__(title, size, win_flag)
		self.keyboard = KeyHandler()
		self.add_event_handle(self.keyboard.handle_event)

		self.mouse = MouseHandler()
		self.add_event_handle(self.mouse.handle_event)

		self.ch_list = []

	def setup(self):
		global sp
		sp = Sprite_2(SP_ANIMATE, 'stand', 15, ANI_ONCE, (0.5, 0.5))
		print(sp)

	def update(self):
		mouse = self.mouse
		keyboard = self.keyboard
		#
		ch_list = self.ch_list

		if keyboard.key_state[KEY_a]:
			ch_list.append(Character(random.randint(0, 800), random.randint(0, 600)))

		for i in ch_list:
			i.update()

		print('Now: {}'.format(len(self.ch_list)))
		tmp = [True for i in self.ch_list if not i.sp.had_draw_once]
		print('Running: {}'.format(len(tmp)))

	def render(self):
		ch_list = self.ch_list
		for i in ch_list:
			i.draw()

	def ask_quit(self):
		self.quit()

def main():
	app = App('image_test_1', (800, 600), W_OPENGL)
	app.run()

if __name__ == '__main__':
	main()