import pygame, sys, random

sys.path.append("../")
from utils import *
from sound import *

gameDisplay = None
clock = None
keyboard = None

def load_se(name, num):
	ll = []
	for i in range(num):
		new_load = Sound(name + '{:02d}'.format(i) + '.wav')
		new_load.set_volume(0.5)
		if new_load:
			ll.append(new_load)
			print('Succeeded to load se {}'.format(name + '{:02d}'.format(i) + '.wav'))
		else:
			print('Failed to load se {}'.foramt(name + '{:02d}'.format(i) + '.wav'))
	return ll

se_timeout = None
se_enep = None
def main():
	z_f = False
	playing = False
	timeout_cnt = 0
	enep_cnt = 0
	cur = None
	# main loop
	while True:
		for e in pygame.event.get():
			if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
				pygame.quit()
				sys.exit()
			elif e.type == pygame.KEYDOWN and e.key == pygame.K_z:
				z_f = True

		gameDisplay.fill((128, 128, 128))

		if s1.is_playing():
			print('[INFO] {} is playing'.format(s1.get_name()))

		if z_f:
			if cur != None and cur.is_playing():
				playing = True
			else:
				playing = False

		if z_f and not playing:
			if timeout_cnt != 3:
				cur = random.choice(se_timeout)
				cur.play()
				timeout_cnt += 1
				playing = True
			elif enep_cnt != 1:
				cur = random.choice(se_enep)
				cur.play()
				enep_cnt += 1
				playing = True
			else:
				timeout_cnt = enep_cnt = 0
				z_f = False

		pygame.display.update()
		clock.tick(60)

if __name__ == '__main__':
	pygame.init()
	pygame.mixer.init()
	gameDisplay = pygame.display.set_mode((800, 600))
	pygame.display.set_caption('music_test_2')
	clock = pygame.time.Clock()

	s1 = Music('the_embodiment_of_scarlet_devil.ogg', S_PLAY_INF)
	s1.play()
	print(s1)

	se_timeout = load_se('se_timeout', 2)
	se_enep = load_se('se_enep', 3)

	main()