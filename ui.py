import sys
sys.path.append("./RHframework")

from font import *
from utils import *
import draw_premitive as dp
# notify_font = Font("Georgia", (0,255,255), 50)

LABEL_ALIGN_LEFT  = 0
LABEL_ALIGN_MID   = 1
LABEL_ALIGN_RIGHT = 2
class Label:
	def __init__(self, text, text_color, rect, size=12, bg_color=(0, 0, 0, 0), font_path=GET_PATH(FONT_MAIN, 'WhiteRabbit.otf')):
		# font
		self.font = Font(font_path, size)
		self.font_size = size
		# text
		self.text = text
		self.text_color = text_color
		self.pos = (rect[0], rect[1])
		self.size = (rect[2], rect[3]) # (0, 0) for auto
		self.bg_color = bg_color

	def draw(self):
		size = self.size
		font = self.font
		#
		if size == (0, 0):
			size = font.get_size(self.text, self.text_color)
		dp.rect(self.bg_color, (*self.pos, *size))
		font.draw_str(self.pos, self.text, self.text_color)

BTN_PRESS   = 0
BTN_RELEASE = 1
BTN_CLICK   = 2
BTN_HOVER   = 3
BTN_NORMAL  = 4
class Button:
	def __init__(self, x, y, width, height, normal, hover, press):
		# image
		self.normal = normal
		self.hover = hover
		self.press = press
		# info
		self.now_state = BTN_NORMAL
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def _normal_draw(self, x, y):
		self.normal.draw(x, y)

	def _hover_draw(self, x, y):
		self.hover.draw(x, y)

	def _press_draw(self, x, y):
		self.press.draw(x, y)

	def update(self, mouse_pos, press):
		mx, my = mouse_pos
		# print('mx={} my={} {}'.format(mx, my, press))
		if self.x <= mx and mx <= self.x + self.width and self.y <= my and my <= self.y + self.height:
			if press:
				self.now_state = BTN_PRESS
			else: # not press
				if self.now_state == BTN_PRESS:
					self.now_state = BTN_CLICK
				else:
					self.now_state = BTN_HOVER
		else:
			self.now_state = BTN_NORMAL

	def draw(self):
		state = self.now_state
		x = self.x
		y = self.y

		if state == BTN_NORMAL:
			self._normal_draw(x, y)
		elif state == BTN_HOVER:
			self._hover_draw(x, y)
		elif state == BTN_PRESS:
			self._press_draw(x, y)

	def is_pressed(self):
		return True if self.now_state == BTN_PRESS else False

	def is_clicked(self):
		return True if self.now_state == BTN_CLICK else False

	def reset(self):
		self.now_state = BTN_NORMAL