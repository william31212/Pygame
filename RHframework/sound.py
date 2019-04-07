import pygame, re

'''
Constants for SoundFile
'''
# Sound type
S_NONE  = 0
S_MUSIC = 1 # for bgm
S_SOUND = 2 # for se

# For music playing
S_PLAY_ONCE = 0
S_PLAY_INF  = 1

# Remember to call pygame.mixer.init()

'''
SoundFile

Interface of sound playing
'''
class SoundFile:
	def __init__(self, path):
		self.path = path

	def play(self):
		raise NotImplementedError
	def stop(self):
		raise NotImplementedError
	def fade_out(self, ms):
		raise NotImplementedError
	def pause(self):
		raise NotImplementedError
	def resume(self):
		raise NotImplementedError
	def set_volume(self, size):
		raise NotImplementedError
	def get_volume(self):
		raise NotImplementedError
	def is_playing(self):
		raise NotImplementedError

	def get_name(self):
		return self.path.split('/')[-1]

	def __repr__(self):
		return object.__repr__(self)
	def __str__(self):
		info = '{}'.format(name) + ' '
		info += self.__repr__()
		return info

class Music(SoundFile):
	def __init__(self, path, play_type=S_PLAY_INF, volume=1.0):
		super().__init__(path)
		self.play_type = play_type
		pygame.mixer.music.load(self.path)
		self.set_volume(volume)

	def play(self):
		if self.is_playing():
			print('[Warning] The music is playing, stop it before call this fuc')
			return

		if self.play_type == S_PLAY_INF:
			pygame.mixer.music.play(-1)
		elif self.play_type == S_PLAY_ONCE:
			pygame.mixer.music.play()

	def stop(self):
		pygame.mixer.music.stop()

	def fade_out(self, ms):
		pygame.mixer.music.fadeout(ms)

	def pause(self):
		pygame.mixer.music.pause()

	def resume(self):
		pygame.mixer.music.unpause()

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

class Sound(SoundFile):
	def __init__(self, path, play_type=S_PLAY_ONCE, volume=1.0):
		super().__init__(path)
		self.sound_file = pygame.mixer.Sound(path)
		self.play_type = play_type
		self.set_volume(volume)
		self.channel = None

	def play(self):
		loop = 0
		if self.play_type == S_PLAY_INF:
			loop = -1
		if self.channel == None:
			self.channel = self.sound_file.play(loop)
		else:
			self.channel.play(self.sound_file, loop)
	
	def stop(self):
		if self.channel:
			self.channel.stop()
	
	def fade_out(self, ms):
		if self.channel:
			self.channel.fadeout(ms)
	
	def pause(self):
		if self.channel != None and self.channel.get_sound() == self.sound_file:
			self.channel.pause()
		else:
			print('[WARNING] {} is not playing'.format(self.get_name()))
	
	def resume(self):
		if self.channel != None and self.channel.get_sound() == self.sound_file:
			self.channel.unpause()
		else:
			print('[WARNING] {} is not pausing'.format(self.get_name()))
	
	def set_volume(self, size):
		self.sound_file.set_volume(size)
	
	def get_volume(self):
		return self.sound_file.get_volume()
	
	def is_playing(self):
		if self.channel != None and self.channel.get_sound() == self.sound_file:
			return self.channel.get_busy()
		else:
			return False

	def get_play_count(self):
		return self.sound_file.get_num_channels()