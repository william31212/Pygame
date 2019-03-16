import pygame
import time

class KeyHandler:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def set_key(self, key, press, hold):

		key = pygame.key.get_pressed()
		# distance moved in 5 frame
		dist = 5
		print("x:{} y:{}".format(self.x,self.y))
		# go_down

		for event in pygame.event.get():

			# leave the game
			if event.type == pygame.QUIT or key[pygame.K_ESCAPE] or key[pygame.K_q]:
				pygame.quit()
				quit()

			elif key[pygame.K_DOWN]:
				self.y += dist
			# go_up
			elif key[pygame.K_UP]:
				self.y -= dist
			# go_right
			elif key[pygame.K_RIGHT]:
				self.x += dist
			# go_left
			elif key[pygame.K_LEFT]:
				self.x -= dist
			# game_stop
			elif key[pygame.K_SPACE]:
				print("stop")

MOUSE_L = 0
MOUSE_M = 1
MOUSE_R = 2
# TODO(roy4801): Implement this
class MouseHandler:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.rel_x = 0
		self.rel_y = 0
		self.btn = [False] * 3

	def set_motion(self, pos, rel, btns):
		self.x = pos[0]
		self.y = pos[1]
		self.rel_x = rel[0]
		self.rel_y = rel[1]
		for i in range(len(self.btn)):
			self.btn[i] = False if btns[i] == 0 else True

	def set_mbtn_down(self, pos, btn):
		self.x = pos[0]
		self.y = pos[1]
		self.btn[btn-1] = True

	def set_mbtn_up(self, pos, btn):
		self.x = pos[0]
		self.y = pos[1]
		self.btn[btn-1] = False

	def __repr__(self):
		return object.__repr__(self)
	def __str__(self):
		info = self.__repr__()
		info += '\n    '
		info += 'x = {}, y = {}'.format(self.x, self.y)
		info += '\n    '
		info += 'rel_x = {}, rel_y = {}'.format(self.rel_x, self.rel_y)
		info += '\n    '
		info += 'btn[{}] = {}'.format('MOUSE_L', self.btn[MOUSE_L])
		info += '\n    '
		info += 'btn[{}] = {}'.format('MOUSE_M', self.btn[MOUSE_M])
		info += '\n    '
		info += 'btn[{}] = {}'.format('MOUSE_R', self.btn[MOUSE_R])
		return info