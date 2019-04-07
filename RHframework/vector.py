import sys,pygame
import math

class Vec2:
	""" math two dim vector"""
	def __init__(self, x=0., y=0.):
		self.x = x
		self.y = y

	def __add__(self, other):
		return Vec2(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Vec2(self.x - other.x, self.y - other.y)
    # dot
	def __mul__(self, other):
		return (self.x * other.x) + (self.y * other.y)

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __ne__(self, other):
		return self != other

	def dot(self, other):
		return self * other

	def scale(self, mag=1):
		self.x *= mag
		self.y *= mag
		return self

	def vec_len(self):
		return math.sqrt((self.x * self.x) + (self.y * self.y))

	def normal(self):
		nor = self.copy()
		divider = self.vec_len()
		nor.x /= divider
		nor.y /= divider
		return nor

	def angle(self, other):
		return math.degrees(math.acos((self * other) / (self.vec_len() * other.vec_len())))

	def rotate(self, theta=0.0):
		sin_t = round(math.sin(math.radians(theta)), 15)
		cos_t = round(math.cos(math.radians(theta)), 15)
		x = cos_t * self.x - sin_t * self.y
		y = sin_t * self.x + cos_t * self.y
		self.x = x
		self.y = y
		return self

	def copy(self):
		return Vec2(self.x, self.y)

	def __repr__(self):
		return object.__repr__(self)
	def __str__(self):
		info = 'x = {:.3f}, y = {:.3f}'.format(self.x, self.y)
		info += ' ' + self.__repr__()
		return info