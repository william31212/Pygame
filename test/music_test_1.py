import pygame, sys, random

sys.path.append("../")
import utils

utils.SET_ROOT('..')
def load_se(name, num):
	ll = []
	for i in range(num):
		new_load = pygame.mixer.Sound(name + '{:02d}'.format(i) + '.wav')
		new_load.set_volume(0.5)
		if new_load:
			ll.append(new_load)
			print('Succeeded to load se {}'.format(name + '{:02d}'.format(i) + '.wav'))
		else:
			print('Failed to load se {}'.foramt(name + '{:02d}'.format(i) + '.wav'))
	return ll

se_timeout = None
se_enep = None

b_playing = False
cnt_timeout = 0
cnt_enep = 0
cur_channel = None
def main():
	while True:
		global b_playing
		# handle events
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			# se trigger
			elif e.type == pygame.KEYDOWN and e.key == pygame.K_z:
				b_playing = True

		# play sound effects
		global cur_channel, cnt_timeout, cnt_enep
		if b_playing:
			# Play se_timeout
			if cnt_timeout < 3:
				if cur_channel != None:
					# delay main thread until se finishs playing
					# In real game, this should definitely not be used
					# Except for creating a new thread for checking if sound completes to play
					while cur_channel.get_busy():
						# print('Waiting cnt_timeout...')
						pygame.time.delay(10)
					cur_channel = None
				else:
					cur_channel = random.choice(se_timeout).play()
					cnt_timeout += 1
			# Play se_enep
			elif cnt_enep < 1:
				if cur_channel != None:
					while cur_channel.get_busy():
						# print('Waiting cnt_enep...')
						pygame.time.delay(10)
					cur_channel = None
				else:
					cur_channel = random.choice(se_enep).play()
					cnt_enep += 1
			else:
				b_playing = False
				cnt_timeout = cnt_enep = 0
			print(cur_channel)

if __name__ == '__main__':
	pygame.init()
	pygame.mixer.init()
	print(pygame.mixer.get_init())
	# Load bgm
	pygame.mixer.music.load('the_embodiment_of_scarlet_devil.ogg')
	print('Success to load music {}'.format('the_embodiment_of_scarlet_devil.ogg'))
	# Load sound effects
	se_timeout = load_se('se_timeout', 2)
	se_enep = load_se('se_enep', 3)

	# 0 = once, -1 = inf
	pygame.mixer.music.play(-1)

	gameDisplay = pygame.display.set_mode((800, 600))
	pygame.display.set_caption('music_test_1')
	main()