import sys, pygame
sys.path.append("../")
from Input import *



def main():
	keyboard = KeyHandler()

	pygame.key.set_repeat(10, 50)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				repeat = False
				if keyboard.get_key_state(event.key):
					repeat = True
				keyboard.set_key_state(event.key, True, repeat)
			elif event.type == pygame.KEYUP:
				keyboard.set_key_state(event.key, False, False)



if __name__ == '__main__':
	pygame.init()
	gameDisplay = pygame.display.set_mode((200, 200))
	pygame.display.set_caption('Input_test')
	main()