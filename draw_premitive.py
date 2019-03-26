from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from asset import pygame_surface_to_image

# TODO(roy4801): Replace these with OpenGL premitives

def _get_surface(size):
	s = pygame.Surface(size)
	s.set_colorkey((0, 0, 0))
	s = s.convert_alpha()
	return s

def _draw_and_del(sur, x, y):
	img = pygame_surface_to_image(sur)
	img.draw(x, y)
	glDeleteTextures([img.img])

def rect(color, Rect, width=0):
	sur = _get_surface((Rect[2], Rect[3]))
	pygame.draw.rect(sur, color, Rect, width)
	_draw_and_del(sur, Rect[0], Rect[1])

def circle(color, pos, radius, width=0):
	w = 2*radius
	sur = _get_surface((w, w))
	pygame.draw.circle(sur, color, (radius, radius), radius, width)
	_draw_and_del(sur, pos[0]-radius, pos[1]-radius)

# TODO(roy4801): width
def line(color, start_pos, end_pos, width=1):
	glPushAttrib(GL_CURRENT_BIT) # preserve now color
	glBegin(GL_LINES)
	glColor3i(*color)
	glVertex3i(*start_pos, 0)
	glVertex3i(*end_pos, 0)
	glEnd()
	glPopAttrib()

# TODO(roy4801): width
def lines(color, closed, pointlist, width=1):
	for i in range(len(pointlist)-1):
		line(color, pointlist[i], pointlist[i+1], width)
	if closed:
		line(color, pointlist[0], pointlist[len(pointlist)-1])