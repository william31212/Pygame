import pygame, os, sys
sys.path.append("../")

from asset import Image
from utils import *
img = None
clock = pygame.time.Clock()
gameDisplay = None
SET_ROOT('..')

def main():
	deg = 0.
	while True:
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		gameDisplay.fill((128, 128, 128))

		img.draw(0, 0)

		img.rotate(deg)
		deg += 10.

		print(img.get_rect())
		pygame.display.update()
		clock.tick(60)

if __name__ == "__main__":
	pygame.init()

	gameDisplay = pygame.display.set_mode((800, 600))

	img = Image('attackA000.png', (0, 0), 0.)

	main()