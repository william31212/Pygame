import pygame

from Input import *
from asset import *


def main():


	Man = KeyHandler()
	while True:
		Man.set_key()


if __name__ == '__main__':
	pygame.init()
	gameDisplay = pygame.display.set_mode((800, 600))
	pygame.display.set_caption('test')
	main()