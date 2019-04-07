import pygame
import pyscroll
import pygame.locals
import sys
import pytmx
import time

sys.path.append("./RHframework")
from utils import *
from shape import *
from asset import *
from sound import *

from ui import *

store_arr = []
blood_arr = []

DIR_NONE = -1
DIR_UP = 1
DIR_DOWN = 2
DIR_LEFT = 3
DIR_RIGHT = 4

Player1_win = 0
Player2_win = 0

class Player:
	P_UP = 0
	P_DOWN = 1
	P_LEFT = 2
	P_RIGHT = 3
	P_SHOOT = 4

	def __init__(self, x, y, width, height, state, Player):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.state = state
		self.hori = 0
		self.blood_state = 240
		
		# shoot
		self.shoot = False
		self.recoil = 20

		self.obs_box = Rect(20, 30, 10, 10) # image space
		self.atk_box = Rect(10, 5, 30, 35) # image space
		self.key_map = None

		self.ak47_se = Sound(GET_PATH(SE_MAIN, 'ak47.wav'), S_PLAY_ONCE, 0.3)
		self.rifleman_right = Image(GET_PATH(IMG_SPRITE, Player+'_right001.png'), (2., 2.), 0., (0.52, 0.56))
		self.rifleman_left =  Image(GET_PATH(IMG_SPRITE, Player+'_left001.png'), (2., 2.), 0., (0.52, 0.56))
		self.shoot_left =     Image(GET_PATH(IMG_SPRITE, Player+'_shoot_left000.png'), (2., 2.), 0., (0.52, 0.56))
		self.shoot_right =    Image(GET_PATH(IMG_SPRITE, Player+'_shoot_right000.png'), (2., 2.), 0., (0.52, 0.56))
		self.blood_img_100 =  Image(GET_PATH(IMG_SPRITE, 'blood_100original.png'), (1, 1))
		self.blood_img_80 =   Image(GET_PATH(IMG_SPRITE, 'blood_80original.png'), (1, 1))
		self.blood_img_60 =   Image(GET_PATH(IMG_SPRITE, 'blood_60original.png'), (1, 1))
		self.blood_img_40 =   Image(GET_PATH(IMG_SPRITE, 'blood_40original.png'), (1, 1))
		self.blood_img_20 =   Image(GET_PATH(IMG_SPRITE, 'blood_20original.png'), (1, 1))
		self.blood_img_10 =   Image(GET_PATH(IMG_SPRITE, 'blood_10original.png'), (1, 1))
		self.blood_img_0 =    Image(GET_PATH(IMG_SPRITE, 'blood_0original.png'), (1, 1))

	def draw(self):
		pass

	def reset_state(self, x, y):
		self.x = x
		self.y = y
		self.blood_img_0.draw(self.x-25, self.y-40)
		self.obs_box = Rect(20, 30, 10, 10) # image space
		self.atk_box = Rect(10, 5, 30, 35)  # image space
		self.blood_state = 240

	def set_key_map(self, m):
		self.key_map = m

	def update(self, bullet):
		kb = KeyHandler.get_keyboard()
		km = self.key_map

		# DIR_UP/DIR_DOWN
		if kb.key_state[km[Player.P_UP]]:
			self.y -= 10
		elif kb.key_state[km[Player.P_DOWN]]:
			self.y += 10
		# DIR_LEFT/DIR_RIGHT
		if kb.key_state[km[Player.P_LEFT]]:
			self.x -= 10
			self.state = DIR_LEFT
		elif kb.key_state[km[Player.P_RIGHT]]:
			self.x += 10
			self.state = DIR_RIGHT
		# shoot
		if kb.key_state[km[Player.P_SHOOT]]:
			self.shoot = True
			bullet.setting(self.x, self.y, self.state)
			self.ak47_se.play()

			# recoil
			if self.state == DIR_LEFT:
				self.x += 20
			elif self.state == DIR_RIGHT:
				self.x -= 20
		# limit play area
		self.x = 0 if self.x < 0 else Window.get_width() if self.x > Window.get_width() else self.x
		self.y = 0 if self.y < 0 else Window.get_height() if self.y > Window.get_height() else self.y

	def store_state(self, num=0):
		store_arr.append([self.x, self.y, self.state])
		blood_arr.append([self.blood_state])

	def store_clear(self):
		store_arr.clear()
		blood_arr.clear()

	def release_state(self, num):
		print(store_arr)
		self.x = store_arr[num][0]
		self.y = store_arr[num][1]
		self.state = store_arr[num][2]

	def draw_character(self):
		self.draw_blood(self.blood_state)
		#sprite
		if self.shoot == True:
			self.shoot = False
			if self.state == DIR_LEFT:
				self.shoot_left.draw(self.x, self.y)
			elif self.state == DIR_RIGHT:
				self.shoot_right.draw(self.x, self.y)
		#normal
		else:
			if self.state == DIR_LEFT:
				self.rifleman_left.draw(self.x, self.y)
			elif self.state == DIR_RIGHT:
				self.rifleman_right.draw(self.x, self.y)

	def draw_blood(self, blood_state):
		if blood_state <= 0:
			self.blood_img_0.draw(self.x-25, self.y-40)
		if blood_state > 0:
			self.blood_img_10.draw(self.x-25, self.y-40)
		if blood_state >= 40:
			self.blood_img_20.draw(self.x-25, self.y-40)
		if blood_state >= 80:
			self.blood_img_40.draw(self.x-25, self.y-40)
		if blood_state >= 120:
			self.blood_img_60.draw(self.x-25, self.y-40)
		if blood_state >= 160:
			self.blood_img_80.draw(self.x-25, self.y-40)
		if blood_state >= 200:
			self.blood_img_100.draw(self.x-25, self.y-40)

	def blood_update(self, blood, num=1):
		self.blood_state = self.blood_state + num

	def check_who_win(self, player1_blood, player2_blood):
		global Player1_win ,Player2_win
		# print(Player1_win, Player2_win)
		if player1_blood <= 0:
			Player2_win += 1
		elif player2_blood <= 0:
			Player1_win += 1

	def game_over(self, point):
		global Player1_win,Player2_win
		if Player1_win >= point:
			Player1_win = 0
			Player2_win = 0
			return 1
		elif Player2_win >= point:
			Player1_win = 0
			Player2_win = 0
			return 2
		else:
			return 0

	def get_player1_point(self):
		return Player1_win

	def get_player2_point(self):
		return Player2_win

	def get_pos(self):
		return (self.x, self.y)