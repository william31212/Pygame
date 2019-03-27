import sys,pygame
import math
import draw_premitive

sys.path.append("../")
from clock import Clock
from Input import *
from asset import *
from utils import *
from tile import *
from shape import *
from player import *
from window import *



class Font:

	def __init__(self, string, style, color, size=12):
		self.string = string
		self.style = style
		self.size = size
		self.color = color

	def draw_str(self, x, y):
		my_font = pygame.font.SysFont(self.style, self.size)
		textSurface = my_font.render(self.string, True, self.color)
		word_rect = textSurface.get_rect()
		tmp = pygame_surface_to_image(textSurface)
		tmp.draw(x , y)
