import pygame, os, sys
sys.path.append("../")

from clock import Clock
from asset import *
from utils import *

SET_ROOT('..')

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('test')
clock = pygame.time.Clock()

pygame.init()

# Load a sttic sprite
s1 = Sprite(SP_STATIC, GET_PATH(IMG_SPRITE, 'attackA000.png'))

# Load a animate sprite
s2 = Sprite(SP_ANIMATE, GET_PATH(IMG_SPRITE, 'stand'), 20, ANI_LOOP)
s3 = s2.copy()
s3.nowFrame = 3

s_right = Sprite(SP_ANIMATE, GET_PATH(IMG_SPRITE, 'walkFront'), 15, ANI_LOOP)
s_left = Sprite(SP_ANIMATE, GET_PATH(IMG_SPRITE, 'walkBack'), 15, ANI_LOOP)
attack_a = Sprite(SP_ANIMATE, GET_PATH(IMG_SPRITE, 'attackA'), 15, ANI_ONCE)

# TODO(roy4801): user this in the future
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(s1)

DIR_NONE  = 0
DIR_LEFT  = 1
DIR_RIGHT = 2

pos = [10, 10]
nowDir = DIR_NONE
go = False
f_attack = False
def processKey(k, flag):
	global go, nowDir, f_attack
	if k == pygame.K_LEFT:
		if flag:
			print('Pressed left')
			nowDir = DIR_LEFT
			go = True
		else:
			print('Released left')
			nowDir = DIR_NONE
			go = False
	elif k == pygame.K_RIGHT:
		if flag:
			print('Pressed right')
			nowDir = DIR_RIGHT
			go = True
		else:
			print('Released right')
			nowDir = DIR_NONE
			go = False
	elif k == pygame.K_c:
		if flag:
			print('Pressed C')
			f_attack = True
		else:
			print('Released C')

print(s_left)

timer = Clock()
timer.reset()
while True:
	# print(timer.getPassedSec())

	# Handle event
	for e in pygame.event.get():
		if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
			pygame.quit()
			quit()
		if e.type == pygame.KEYDOWN:
			processKey(e.key, True)
		if e.type == pygame.KEYUP:
			processKey(e.key, False)

	# Update
	offset = 5
	if f_attack:
		offset = 2
	if go:
		if nowDir == DIR_LEFT:
			pos[0] -= offset
		elif nowDir == DIR_RIGHT:
			pos[0] += offset

	# Draw
	gameDisplay.fill((255, 255, 255))

	s1.draw(400, 300)
	s2.draw(500, 300)
	s3.draw(600, 300)

	if f_attack:
		if attack_a.draw(pos[0], pos[1]):
			f_attack = False
	else:
		if nowDir == DIR_LEFT:
			s_left.draw(pos[0], pos[1])
		elif nowDir == DIR_RIGHT:
			s_right.draw(pos[0], pos[1])
		else:
			s2.draw(pos[0], pos[1])
	# Render
	pygame.display.update()

	clock.tick(60)