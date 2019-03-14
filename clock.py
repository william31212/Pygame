import pygame

# helper func
def get_now():
	return pygame.time.get_ticks()

class Clock:
	def __init__(self):
		self.origin = 0
	# Start/Retst the Clock
	def reset(self):
		self.origin = get_now()
	# Get passed ms
	def getPassed(self):
		return get_now() - self.origin
	# Get passed sec
	def getPassedSec(self):
		return self.getPassed() / 1000

# TODO(roy4801): Add timer and refactor asset.py:90
class Timer:
	def __init__(self, lim=0):
		self.clk = Clock()
		self.limit = lim
	# Start/Reset the timer
	def reset(self):
		self.clk.reset()
	# If the timer ends, it returns true.
	def timeout(self):
		if self.clk.getPassed() >= self.limit:
			return True
		else:
			return False