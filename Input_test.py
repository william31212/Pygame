import pygame

from Input import *



def main():
	Man = KeyHandler()

	pygame.key.set_repeat(10, 50)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				Man.set_key(event.key)
			elif event.type == pygame.KEYUP:
				Man.set_key(event.key)



if __name__ == '__main__':
	pygame.init()
	gameDisplay = pygame.display.set_mode((200, 200))
	pygame.display.set_caption('Input_test')
	main()