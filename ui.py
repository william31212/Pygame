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
	def __init__(self, text, text_color, rect, bg_color=(0, 0, 0, 0), font_path=GET_PATH(FONT_MAIN, 'LucidaBrightDemiBold.ttf'), size=12):
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

BTN_CLICK = 0
BTN_HOVER = 1
BTN_NORMAL = 2
class Button:
	def __init__(self, x, y, width, height, normal, hover, click):
		self.normal = normal
		self.hover = hover
		self.click = click
		self.now_state = BTN_NORMAL
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	# TODO(roy4801): deprecated
	def normal_draw(self, x, y):
		self.normal.draw(x, y)

	def hover_draw(self, x, y):
		self.hover.draw(x, y)

	def click_draw(self, x, y):
		self.click.draw(x, y)
	############################

	def update(self, mouse_pos, click):
		mx, my = mouse_pos
		if click == False:
			if self.x <= mx <= self.x + self.width:
				if self.y <= my <= self.y + self.height:
					return BTN_HOVER
				else:
					return BTN_NORMAL
			else:
				return BTN_NORMAL

		elif click == True:
			if self.x <= mx <= self.x + self.width:
				if self.y <= my <= self.y + self.height:
					return BTN_CLICK
				else:
					return BTN_NORMAL
			else:
				return BTN_NORMAL



	def draw(self):
		pass
		# TODO(roy4801): implement this
