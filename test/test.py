import pygame, os
sys.path.append("../")

display_width  = 640
display_height = 480

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('test')
clock = pygame.time.Clock()
running = True

PATH = 'asset/'
ASSET = {}
ASSET_NUM = {}
ASSET_NOW_FRAME = {}
def loadAssets(name, file, num):
	print('Loading assets...')
	ASSET_NUM[name] = num
	ASSET_NOW_FRAME[name] = 0
	ll = []
	for i in range(num):
		ll.append(pygame.image.load(PATH + file + '{:03d}'.format(i) + '.png'))
	return ll

def nowTime():
	return pygame.time.get_ticks()
def blit(img, x, y):
	gameDisplay.blit(img, (x, y))

# 1 left
# 2 right
direction = 0
start_tick = 0

def draw(name, fps, i, j):
	global start_tick
	now_tick = nowTime()-start_tick
	print('now = {} pass = {}'.format(now_tick, nowTime()))
	if now_tick > 1000/fps:
		ASSET_NOW_FRAME[name] += 1
		ASSET_NOW_FRAME[name] %= ASSET_NUM[name]
		start_tick = nowTime()
	blit(ASSET[name][ASSET_NOW_FRAME[name]], i, j)

def gameLoop():
	global direction
	prevDir = 'walk_b'

	# start_tick = nowTime()
	i = display_width/2
	j = display_height/2

	while running:
		#################################
		# event loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					direction = 1
				elif event.key == pygame.K_RIGHT:
					direction = 2
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					direction = 0

		#################################
		# Update
		if direction == 1:
			i -= 1
		elif direction == 2:
			i += 1
		#################################
		# Draw
		gameDisplay.fill((255, 255, 255))

		dd = ['stand', 'walk_b', 'walk_f']
		draw(dd[direction], 10, i, j)
		
		pygame.display.update()
		clock.tick(60)

if __name__ == '__main__':
	pygame.init()

	ASSET['attack'] = loadAssets('attack', 'attackA', 6)
	ASSET['walk_f'] = loadAssets('walk_f', 'walkFront', 7)
	ASSET['walk_b'] = loadAssets('walk_b', 'walkBack', 7)
	ASSET['stand']  = loadAssets('stand', 'stand', 9)
	print(ASSET)
	gameLoop()