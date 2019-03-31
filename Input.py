import pygame, time

'''
KeyHandler: Process and handle the keyboard event
'''

KEY_UP    = 0
KEY_DOWN  = 1
KEY_LEFT  = 2
KEY_RIGHT = 3
KEY_ESC   = 4
KEY_a     = 5
KEY_w     = 6
KEY_s     = 7
KEY_d     = 8
KEY_b     = 9
KEY_SPACE = 10
KEY_TOTAL = 11

def _keyboard_handle(keyboard, e):
	# Keydown
	if e.type == pygame.KEYDOWN:
		repeat = False
		if keyboard.get_key_state(e.key)[0]:
			repeat = True
		keyboard.set_key_state(e.key, True, repeat)
	# Keyup
	elif e.type == pygame.KEYUP:
		keyboard.set_key_state(e.key, False, False)

class KeyHandler:
	def __init__(self):
		self.keymap = {
			pygame.K_UP     : KEY_UP,
			pygame.K_DOWN   : KEY_DOWN,
			pygame.K_LEFT   : KEY_LEFT,
			pygame.K_RIGHT  : KEY_RIGHT,
			pygame.K_ESCAPE : KEY_ESC,
			pygame.K_w      : KEY_w,
			pygame.K_s      : KEY_s,
			pygame.K_d      : KEY_d,
			pygame.K_a      : KEY_a,
			pygame.K_b      : KEY_b,
			pygame.K_SPACE  : KEY_SPACE
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
	# get current key state (press, repeat)
	def get_key_state(self, key):
		if not key in self.keymap:
			return (False, False)
		else:
			idx = self.keymap[key]
			return (self.key_state[idx], self.key_repeat[idx])

	def handle_event(self, e):
		_keyboard_handle(self, e)
	# for print()
	def __repr__(self):
		return object.__repr__(self)
	def __str__(self):
		info = self.__repr__()

'''
MouseHandler: Process and handle the mouse event
'''
MOUSE_L      = 0
MOUSE_M      = 1
MOUSE_R      = 2
MOUSE_WHUP   = 3
MOUSE_WHDOWN = 4
MOUSE_TOTAL  = 5

def _mouse_handle(m, e):
	if e.type == pygame.MOUSEMOTION:
		m.set_motion(e.pos, e.rel, e.buttons)
	elif e.type == pygame.MOUSEBUTTONDOWN:
		m.set_mbtn_down(e.pos, e.button)
	elif e.type == pygame.MOUSEBUTTONUP:
		m.set_mbtn_up(e.pos, e.button)

class MouseHandler:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.rel_x = 0
		self.rel_y = 0
		self.btn = [False] * MOUSE_TOTAL

	def set_motion(self, pos, rel, btns):
		self.x = pos[0]
		self.y = pos[1]
		self.rel_x = rel[0]
		self.rel_y = rel[1]
		for i in range(len(btns)):
			self.btn[i] = False if btns[i] == 0 else True

	def set_mbtn_down(self, pos, btn):
		self.x = pos[0]
		self.y = pos[1]
		self.btn[btn-1] = True

	def set_mbtn_up(self, pos, btn):
		self.x = pos[0]
		self.y = pos[1]
		self.btn[btn-1] = False

	def handle_event(self, e):
		_mouse_handle(self, e)

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
		info += '\n    '
		info += 'btn[{}] = {}'.format('MOUSE_WHUP', self.btn[MOUSE_WHUP])
		info += '\n    '
		info += 'btn[{}] = {}'.format('MOUSE_WHDOWN', self.btn[MOUSE_WHDOWN])
		return info