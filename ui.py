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