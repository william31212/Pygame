import pygame, re

'''
Constants for SoundFile
'''
# Sound type
S_NONE  = 0
S_MUSIC = 1 # for bgm
S_SOUND = 2 # for se

# For music playing
S_MUSIC_ONCE = 0
S_MUSIC_INF  = 1

# Remember to call pygame.mixer.init()

'''
SoundFile

Interface of sound playing
'''
class SoundFile:
	def __init__(self, path):
		self.path = path

	def play(self):
		pass
	def stop(self):
		pass
	def pause(self):
		pass
	def resume(self):
		pass
	def set_volume(self, size):
		pass
	def get_volume(self):
		pass
	def is_playing(self):
		pass

	def get_name(self):
		return self.path.split('/')[-1]

	def __repr__(self):
		return object.__repr__(self)
	def __str__(self):
		info = '{}'.format(name) + ' '
		info += self.__repr__()
		return info

class Music(SoundFile):
	def __init__(self, path, play_type, volume=1.0):
		super().__init__(path)
		self.play_type = play_type
		pygame.mixer.music.load(self.path)
		self.set_volume(volume)

	def play(self):
		if self.is_playing():
			print('[Warning] The music is playing, stop it before call this fuc')
			return

		if self.play_type == S_MUSIC_INF:
			pygame.mixer.music.play(-1)
		elif self.play_type == S_MUSIC_ONCE:
			pygame.mixer.music.play()

	def stop(self):
		pygame.mixer.music.stop()

	def pause(self):
		pygame.mixer.music.pause()

	def resume(self):
		pygame.mixer.music.unpause()

	def fade_out(self, ms):
		pygame.mixer.music.fadeout(ms)

	def set_volume(self, size):
		pygame.mixer.music.set_volume(size)

	def get_volume(self):
		return pygame.mixer.music.get_volume()

	def is_playing(self):
		return pygame.mixer.music.get_busy()

	def __repr__(self):
		return object.__repr__(self)
	def __str__(self):
		info = self.__repr__() + '\n + '
		info += 'Name: {}'.format(self.path.split('/')[-1]) + '\n + '
		info += 'Path: {}'.format(self.path) + '\n + '
		info += 'Status: {}'.format('Playing' if self.is_playing() else 'Stopped') + '\n'
		return info