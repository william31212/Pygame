import pygame, sys, os
sys.path.append("../")
from vector import *
from utils import *


img = pygame.image.load('../assets/sprite/attackA000.png')
gameDisplay = None
clock = None

def main():
	while True:
		for e in pygame.event.get():
			if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
				pygame.quit()
				sys.exit()

		gameDisplay.fill((255, 255, 255))

		# img, pos, tex_rect
		gameDisplay.blit(img, (10, 10), (50, 50, 50, 50))

		pygame.display.update()
		clock.tick(60)


if __name__ == '__main__':
	gameDisplay = pygame.display.set_mode((300, 300))
	clock = pygame.time.Clock()
	main()