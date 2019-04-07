import sys,pygame
import math
import draw_premitive

sys.path.append("../")
from clock import Clock
from input import *
from asset import *
from utils import *
from tile import *
from shape import *
from player import *
from window import *

from OpenGL.GL import *

class Font:
	def __init__(self, path, size=12):
		self.path = path
		self.size = size
		self.font_file = pygame.font.Font(self.path, self.size)
		self.surface = None

	def draw_str(self, pos, string, color):
		if self.surface == None:
			self._render(string, color)
		# To Image
		tmp = pygame_surface_to_image(self.surface)
		tmp.draw(pos[0], pos[1])
		self.surface = None

	def get_size(self, string, color):
		if self.surface == None:
			self._render(string, color)
		return self.surface.get_size()

	def _render(self, string, color):
		self.surface = self.font_file.render(string, True, color)