import pygame
import time

# TODO(roy4801): Implement this

class KeyHandler:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def set_key(self):

		key = pygame.key.get_pressed()
		# distance moved in 5 frame
		dist = 5
		print("x:{} y:{}".format(self.x,self.y))
		# go_down

		for event in pygame.event.get():

			# leave the game
			if event.type == pygame.QUIT or key[pygame.K_ESCAPE] or key[pygame.K_q]:
				pygame.quit()
				quit()

			elif key[pygame.K_DOWN]:
				self.y += dist
			# go_up
			elif key[pygame.K_UP]:
				self.y -= dist
			# go_right
			elif key[pygame.K_RIGHT]:
				self.x += dist
			# go_left
			elif key[pygame.K_LEFT]:
				self.x -= dist
			# game_stop
			elif key[pygame.K_SPACE]:
				print("stop")

