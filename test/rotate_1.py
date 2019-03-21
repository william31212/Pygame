import pygame, os, sys
sys.path.append("../")

from asset import *
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


		img.rotate(deg)
		deg += 10.

		img.draw(100, 100)
		img2.draw(200, 100)
		img3.draw(100, 300)
		pygame.display.update()
		clock.tick(60)

if __name__ == "__main__":
	pygame.init()

	gameDisplay = pygame.display.set_mode((800, 600))

	img = Image(GET_PATH(IMG_SPRITE, 'attackA000.png'), (0, 0), 0., (38, 65))
	img2 = img.copy()
	img3 = img.copy()
	main()