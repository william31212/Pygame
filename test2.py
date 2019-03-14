import pygame
import pprint

from clock import Clock
from asset import *


gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('test')
clock = pygame.time.Clock()

pygame.init()

# Load a sttic sprite
s1 = Sprite(SP_STATIC, 'attackA.png')

# Load a animate sprite
s2 = Sprite(SP_ANIMATE, 'stand', 20, ANI_LOOP)
s3 = s2.copy()
s3.nowFrame = 3

# TODO(roy4801): user this in the future
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(s1)

print(s1)
print(s2)
print(s3)

timer = Clock()
timer.reset()
while True:
	# print(timer.getPassedSec())

	# Handle event
	for e in pygame.event.get():
		if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
			pygame.quit()
			quit()

	# Update

	# Draw
	gameDisplay.fill((255, 255, 255))

	s1.draw(400, 300)
	s2.draw(500, 300)
	s3.draw(600, 300)

	# Render
	pygame.display.update()

	# clock.tick(60)