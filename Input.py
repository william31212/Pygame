import pygame, time

KEY_UP    = 0
KEY_DOWN  = 1
KEY_LEFT  = 2
KEY_RIGHT = 3
KEY_TOTAL = 4


class KeyHandler:
	def __init__(self):
		self.keymap = {
			pygame.K_UP  : KEY_UP,
			pygame.K_DOWN  : KEY_DOWN,
			pygame.K_LEFT  : KEY_LEFT,
			pygame.K_RIGHT : KEY_RIGHT
		}
		self.key_state  = [False] * KEY_TOTAL
		self.key_repeat = [False] * KEY_TOTAL
	
	def set_key_state(self, key, press, repeat):
		if not key in self.keymap:
			# TODO(roy4801): Replace with the logger
			print('[Warning] The key ({}) isn\'t in the keymap'.format(pygame.key.name(key)))
		else:
			idx = self.keymap[key]
			self.key_state[idx] = press
			self.key_repeat[idx] = repeat
	# TODO(roy4801): Change the return type to tuple (press, repeat)
	def get_key_state(self, key):
		if not key in self.keymap:
			return False
		else:
			return self.key_state[self.keymap[key]]

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