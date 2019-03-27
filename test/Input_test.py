import sys, pygame, logging
sys.path.append("../")
from input import *

logger = logging.getLogger('input_test')
logger.setLevel(logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(levelname)-s] %(name)-12s\n    %(message)s')
console.setFormatter(formatter)
logger.addHandler(console)

def main():
	keyboard = KeyHandler()

	pygame.key.set_repeat(10, 50)

	handle_keys = [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]
	handle_key_name = {KEY_UP:'KEY_UP', KEY_DOWN:'KEY_DOWN', KEY_LEFT:'KEY_LEFT', KEY_RIGHT:'KEY_RIGHT'}

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			# Keydown
			elif event.type == pygame.KEYDOWN:
				repeat = False
				if keyboard.get_key_state(event.key)[0]:
					repeat = True
				keyboard.set_key_state(event.key, True, repeat)
			# Keyup
			elif event.type == pygame.KEYUP:
				keyboard.set_key_state(event.key, False, False)

		for i in handle_keys:
			any_pressed = False
			key_name = ''
			if keyboard.key_state[i]:
				key_name = handle_key_name[i]
				any_pressed = True
			key_name += ' key '

			if keyboard.key_repeat[i]:
				key_name += '(repeat)'
			if any_pressed:
				logger.info('Pressed {}'.format(key_name))


if __name__ == '__main__':
	pygame.init()
	gameDisplay = pygame.display.set_mode((200, 200))
	pygame.display.set_caption('Input_test')
	main()