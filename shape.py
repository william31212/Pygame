import sys,pygame
import math

from utils import GET_PATH


class Rect:
	"""docstring for """
	def __init__(self, Left_x, Left_y, Right_x, Right_y):
		self.Left_x = Left_x
		self.Left_y = Left_y
		self.Right_x = Right_x
		self.Right_y = Right_y

	def check_point(self, point_x=0, point_y=0):
		if self.Left_x <= point_x and point_x <= self.Right_x:
			if self.Left_y <= point_y and point_y <= self.Right_y:
				return True
			else:
				return False
		else:
			return False
	# TODO(william31212): Refactor for performance
	def check_rect(self, other):
		for i in range(int(other.Left_x),int(other.Right_x)):
			if self.Left_x <= i and i <= self.Right_x:
				for j in range(int(other.Left_y),int(other.Right_y)):
					if self.Left_y <= j and j <= self.Right_y:
						return True
					else:
						continue
			else:
				continue
		return False


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