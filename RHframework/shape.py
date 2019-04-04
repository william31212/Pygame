import sys,pygame
import math

from utils import GET_PATH
import draw_premitive as dp

# Todo change x, y, w, h
class Rect:
	"""docstring for """
	def __init__(self, x, y, wid, hei):
		self.x = x
		self.y = y
		self.wid = wid
		self.hei = hei

	def check_point(self, point_x=0, point_y=0):
		if self.x <= point_x and point_x <= (self.x + self.wid):
			if self.y <= point_y and point_y <= (self.y + self.hei):
				return True
			else:
				return False
		else:
			return False
	# TODO(william31212): Refactor for performance
	def check_rect(self, other):
		for i in range(int(other.x),int(other.x + other.wid)):
			if self.x <= i and i <= (self.x + self.wid):
				for j in range(int(other.y),int(other.y + other.hei)):
					if self.y <= j and j <= (self.y + self.hei):
						return True
					else:
						continue
			else:
				continue
		return False

	def get_tuple(self):
		return (self.x, self.y, self.wid, self.hei)
	def get_list(self):
		return [self.x, self.y, self.wid, self.hei]

class Circle:
	"""docstring for Circle"""
	def __init__(self, center_x, center_y, radius):
		self.center_x = center_x
		self.center_y = center_y
		self.radius = radius

	def check_circle(self,other):
		x = (other.center_x - self.center_x) * (other.center_x - self.center_x)
		y = (other.center_y - self.center_y) * (other.center_y - self.center_y)
		if math.sqrt(x + y) <= self.radius + other.radius:
			return True
		else:
			return False