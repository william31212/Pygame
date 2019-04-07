import sys, math
sys.path.append("../RHframework")

from window import *
from asset import *
from utils import *
from input import *
import draw_premitive as dp

SET_ROOT('..')

class box:
	def __init__(self, rect, color):
		self.x , self.y, self.w, self.h = rect
		self.color = color

		print(self.color)

	def draw(self):
		dp.rect(self.color, (self.x, self.y, self.w, self.h))

class Add_box_window:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.r = 0
		self.g = 0
		self.b = 0
		self.a = 1.

		self.rt = None

		self.ok = False
		self.cancel = False

	def get_result(self):
		return self.rt

	def update(self):
		imgui.begin('Add a box')
		_, (self.r, self.g, self.b, self.a) = imgui.color_edit4('Color', self.r, self.g, self.b, self.a)

		imgui.begin_group()
		imgui.text("Pos")
		changed, self.x = imgui.drag_float("self.x", self.x,)
		changed, self.y = imgui.drag_float("self.y", self.y,)
		imgui.text("Changed: {}, x: {:.2f} y: {:.2f}".format(changed, self.x, self.y))
		imgui.end_group()

		self.ok = imgui.button('Ok')
		self.cancel = imgui.button('Cancel')
		imgui.end()

		if self.ok:
			self.rt = box((self.x, self.y, 100, 100), (self.r*255, self.g*255, self.b*255, self.a*255))

class App(Window):
	def __init__(self, title, size, win_flag=W_NONE):
		super().__init__(title, size, win_flag)
		self.keyboard = KeyHandler()
		self.add_event_handle(self.keyboard.handle_event)

		self.mouse = MouseHandler()
		self.add_event_handle(self.mouse.handle_event)

		self.add_box_window = None
		self.box_list = []

		self.test = Image('ball.png')

	def setup(self):
		pass

	def update(self):
		mouse = self.mouse
		keyboard = self.keyboard

		imgui.begin('Hello')
		if imgui.button("Add a box"):
			self.add_box_window = None
			self.add_box_window = Add_box_window()
		imgui.end()

		# add_box_window logic #
		if self.add_box_window:
			self.add_box_window.update()
			if self.add_box_window.ok:
				self.box_list.append(self.add_box_window.get_result())

			if self.add_box_window.ok or self.add_box_window.cancel:
				self.add_box_window = None
		########################

	def render(self):
		for box in self.box_list:
			box.draw()


	def ask_quit(self):
		pass
		self.quit()

def main():
	app = App('image_test_1', (800, 600), W_OPENGL)
	app.run()

if __name__ == '__main__':
	main()