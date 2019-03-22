import pygame, sys, random

sys.path.append("../")
from utils import *
from sound import *

SET_ROOT('..')

gameDisplay = None
clock = None

def main():
	while True:
		for e in pygame.event.get():
			if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
				pygame.quit()
				sys.exit()

		gameDisplay.fill((128, 128, 128))

		if s1.is_playing():
			print('[INFO] {} is playing'.format(s1.get_name()))

		pygame.display.update()
		clock.tick(60)

if __name__ == '__main__':
	pygame.init()
	pygame.mixer.init()
	gameDisplay = pygame.display.set_mode((800, 600))
	pygame.display.set_caption('music_test_2')
	clock = pygame.time.Clock()

	s1 = Music('the_embodiment_of_scarlet_devil.ogg', S_MUSIC_INF)
	s1.play()
	print(s1)
	main()