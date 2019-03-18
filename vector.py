import sys,pygame
import math

RAD_TO_DEG = 180 / math.pi
DEG_TO_RAD = math.pi / 180
class Vec2:
	"""docstring for Vec2"""
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		return Vec2(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Vec2(self.x - other.x, self.y - other.y)

	def __mul__(self, other):
		return (self.x * other.x) + (self.y * other.y)

	def __eq__(self, other):
		if self.x == other.x and self.y == other.y:
			return True
		else:
			return False

	def scale(self, mag=1):
		self.x *= mag
		self.y *= mag

	def vec_len(self):
		return math.sqrt((self.x * self.x) + (self.y * self.y))

	def normal(self):
		divider = math.sqrt((self.x * self.x) + (self.y * self.y))
		self.x /= divider
		self.y /= divider

	def angle(self, other):
		return math.acos((self * other) / (self.vec_len() * other.vec_len())) * RAD_TO_DEG

	def rotate(self, theta=0.0):
		# print(math.sin(math.radians(theta)) )
		sin_t = round(math.sin(math.radians(theta)), 15)
		cos_t = round(math.cos(math.radians(theta)), 15)
		x = cos_t * self.x - sin_t * self.y
		y = sin_t * self.x + cos_t * self.y
		self.x = x
		self.y = y
