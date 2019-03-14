import pygame

# helper func
def get_now():
	return pygame.time.get_ticks()

class Clock:
	def __init__(self):
		self.origin = 0
	# Start the Clock
	def reset(self):
		self.origin = get_now()
	# Get passed ms
	def getPassed(self):
		return get_now() - self.origin
	# Get passed sec
	def getPassedSec(self):
		return self.getPassed() / 1000