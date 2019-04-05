import sys,pygame
import math

from utils import GET_PATH
import draw_premitive as dp

# Todo change x, y, w, h
class Rect:
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

	def to_line_list(self):
		l = []
		x, y, w, h = self.x, self.y, self.wid, self.hei
		l.append(Line((x, y), (x+w, y)))
		l.append(Line((x+w, y), (x+w, y+h)))
		l.append(Line((x+w, y+h), (x, y+h)))
		l.append(Line((x, y+h), (x, y)))
		return l

	# pos must be the screen space coordinate of origin in image space
	def to_screen_space(self, pos):
		return Rect(pos[0]+self.x, pos[1]+self.y, self.wid, self.hei)

	def get_tuple(self):
		return (self.x, self.y, self.wid, self.hei)
	def get_list(self):
		return [self.x, self.y, self.wid, self.hei]

LINE_RIGHT = 1
LINE_ON    = 2
LINE_LEFT  = 3
class Line:
	def __init__(self, a, b):
		self.pt = [a, b]
		x_0, y_0 = self.pt[0][0], -self.pt[0][1]
		x_1, y_1 = self.pt[1][0], -self.pt[1][1]

		if x_1 - x_0 != 0:
			self.m = (y_1 - y_0) / (x_1 - x_0)
		else:
			self.m = None

	def get_dis_point(self, p):
		m = self.m
		x, y = p[0], -p[1]
		x_0, y_0 = self.pt[0][0], -self.pt[0][1]

		if m == None: # x = ?
			return math.fabs(x_0 - x)
		elif m == 0:
			return math.fabs(y_0 - y)
		#
		a = -m
		b = 1
		c = m*x_0 - y_0
		#
		up = math.fabs(a*x + b*y + c)
		down = math.sqrt(a*a + b*b)
		return round(up / down, 15)

	def check_point(self, p):
		m = self.m
		# convert to math coordinate
		x_0, y_0 = self.pt[0][0], -self.pt[0][1]
		x_1, y_1 = self.pt[1][0], -self.pt[1][1]
		x, y = p[0], -p[1]

		if m == None: # x = ?
			if x > x_0:
				return LINE_RIGHT
			elif x < x_0:
				return LINE_LEFT
			elif x == x_0:
				return LINE_ON
		else:
			leq = round(m*x - y, 15)
			req = round(m*x_0 - y_0, 15)

			if leq == req:
				return LINE_ON

			if m > 0:
				if leq < req:
					return LINE_LEFT
				elif leq > req:
					return LINE_RIGHT
			elif m < 0:
				if leq < req:
					return LINE_RIGHT
				elif leq > req:
					return LINE_LEFT
			else: # y = ?
				if y > y_0:
					return LINE_LEFT
				elif y < y_0:
					return LINE_RIGHT
				else:
					return LINE_ON
	# for print()
	def __repr__(self):
		return object.__repr__(self)
	def __str__(self):
		info = self.__repr__() + '\n    '
		info += 'pt={}'.format(self.pt) + '\n    '
		info += 'm={}'.format(self.m)
		return info
		

class Circle:
	def __init__(self, cent_x, cent_y, radius):
		self.cent_x = cent_x
		self.cent_y = cent_y
		self.radius = radius

	def check_circle(self,other):
		x = (other.cent_x - self.cent_x) * (other.cent_x - self.cent_x)
		y = (other.cent_y - self.cent_y) * (other.cent_y - self.cent_y)
		if math.sqrt(x + y) <= self.radius + other.radius:
			return True
		else:
			return False

	def check_rect(self, rect):
		# TODO(roy4801): implement this
		pass
	# circle撞到line
	def check_line(self, line):
		if line.get_dis_point((self.cent_x, self.cent_y)) <= self.radius:
			return True
		else:
			return False

	# pos must be the screen space coordinate of origin in image space
	def to_screen_space(self, pos):
		return Circle(pos[0]+self.cent_x, pos[1]+self.cent_y, self.radius)

	def get_pos(self):
		return (self.cent_x, self.cent_y)