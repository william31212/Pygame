import sys, pygame


sys.path.append("./RHframework")
from clock import Clock
from input import *
from asset import *
from utils import *
from tile import *
from shape import *
from player import *
from window import *
from window import *
from Bullet import *


class Button:
	def __init__(self, x, y, width, height, normal, hover, click):
		self.normal = normal
		self.hover = hover
		self.click = click
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def normal_draw(self, x, y):
		self.normal.draw(x, y)

	def hover_draw(self, x, y):
		self.hover.draw(x, y)

	def click_draw(self, x, y):
		self.click.draw(x, y)


