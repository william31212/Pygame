import sys,pygame
import math

from utils import GET_PATH
import draw_premitive as dp

def to_rect(tup):
	l = len(tup)
	if l == 2:
		return Rect(tup[0], tup[1], 0, 0)
	elif l == 4:
		return Rect(tup[0], tup[1], tup[2], tup[3])
	else:
		print('[Error] to_rect(tup): the len(tup) should be 2 or 4')
		return None

# Todo change x, y, w, h
class Rect:
	def __init__(self, x, y, wid, hei):
		self.x = x
		self.y = y
		self.wid = wid
		self.hei = hei

	def __add__(self, other):
		return Rect(self.x+other.x, self.y+other.y, self.wid+other.wid, self.hei+other.hei)

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
	def to_screen_space(self, cent_pos, img):
		resize = img.get_resize()
		pos = img.get_left_upper(cent_pos)
		return to_rect(pos) + Rect(self.x*resize[0], self.y*resize[1], self.wid*resize[0], self.hei*resize[1])

	def get_tuple(self):
		return (self.x, self.y, self.wid, self.hei)
	def get_list(self):
		return [self.x, self.y, self.wid, self.hei]
	# for debugging
	def dbg_draw(self, color):
		dp.rect(color, self.get_tuple(), 2)
	def __repr__(self):
		return object.__repr__(self)
	def __str__(self):
		info = '  '
		info += 'x = {}'.format(self.x) + '\n  '
		info += 'y = {}'.format(self.y) + '\n  '
		info += 'w = {}'.format(self.wid) + '\n  '
		info += 'h = {}'.format(self.hei) + '\n'
		return info

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

	# 點到線的距離
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

	# 判斷點與線
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
		
def to_circle(tup):
	if len(tup) == 3:
		return Circle(tup[0], tup[1], tup[2])
	elif len(tup) == 2:
		return Circle(tup[0], tup[1], 0)
	else:
		print('[Error] to_circle(tup): the len(tup) should be 2 or 3')
		return None


class Circle:
	def __init__(self, cent_x, cent_y, radius):
		self.cent_x = cent_x
		self.cent_y = cent_y
		self.radius = radius

	def __add__(self, other):
		return Circle(self.cent_x+other.cent_x, self.cent_y+other.cent_y, max(self.radius, other.radius))

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
	def to_screen_space(self, cent_pos, img):
		resize = img.get_resize()
		pos = img.get_left_upper(cent_pos)
		return to_circle(pos) + Circle(self.cent_x*resize[0], self.cent_y*resize[1], self.radius*max(resize))

	def get_pos(self):
		return (self.cent_x, self.cent_y)