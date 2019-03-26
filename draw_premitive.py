from OpenGL.GL import *
from OpenGL.GLU import *
import pygame, math
from asset import pygame_surface_to_image

# TODO(roy4801): Replace these with OpenGL premitives

def _gl_prologue():
	glMatrixMode(GL_MODELVIEW)
	glPushMatrix()
	glLoadIdentity()
	glPushAttrib(GL_CURRENT_BIT)

def _gl_epilogue():
	glPopAttrib()
	glPopMatrix()

def rect(color, Rect, width=0):
	_gl_prologue()
	glTranslatef(Rect[0], Rect[1], 0.0)
	r, g, b = [x/0xff for x in color]
	w, h = Rect[2], Rect[3]

	if width != 0:
		glLineWidth(width)
		glBegin(GL_LINE_LOOP)
		glColor3f(r, g, b)
		glVertex3f(0., 0., 0.)
		glVertex3f(0., h, 0.)
		glVertex3f(w, h, 0.)
		glVertex3f(w, 0., 0.)
		glEnd()
		glLineWidth(1)
	else:
		glBegin(GL_TRIANGLE_FAN)
		glColor3f(r, g, b)
		glVertex3f(0., 0., 0.)
		glVertex3f(0., h, 0.)
		glVertex3f(w, h, 0.)
		glVertex3f(w, 0., 0.)
		glEnd()

	_gl_epilogue()

def circle(color, pos, radius, width=0, segment=32):
	_gl_prologue()
	glTranslatef(pos[0], pos[1], 0.0)

	r, g, b = [x/0xff for x in color]
	pt = []
	for i in range(segment+1):
		theta = 2 * math.pi * i / segment
		x = float(radius) * math.cos(theta)
		y = float(radius) * math.sin(theta)
		pt.append((x, y))

	if width != 0:
		glLineWidth(width)
		glBegin(GL_LINE_LOOP)
		glColor3f(r, g, b)

		for i in pt:
			glVertex3f(i[0], i[1], 0.0)

		glEnd()
		glLineWidth(1.0)
	else:
		glBegin(GL_TRIANGLE_FAN)
		glColor3f(r, g, b)

		glVertex3f(0, 0, 0)
		for i in pt:
			glVertex3f(i[0], i[1], 0.0)

		glEnd()

	_gl_epilogue()

# TODO(roy4801): width
def line(color, start_pos, end_pos, width=1):
	_gl_prologue()
	r, g, b = [x/0xff for x in color]
	
	glLineWidth(float(width))
	
	glBegin(GL_LINES)
	glColor3f(r, g, b)
	glVertex3i(*start_pos, 0)
	glVertex3i(*end_pos, 0)
	glEnd()
	glLineWidth(1.0)
	
	_gl_epilogue()

# TODO(roy4801): width
def lines(color, closed, pointlist, width=1):
	for i in range(len(pointlist)-1):
		line(color, pointlist[i], pointlist[i+1], width)
	if closed:
		line(color, pointlist[0], pointlist[len(pointlist)-1])