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
import ui

store_arr = []
blood_arr = []
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

Player1_win = 0
Player2_win = 0

class Player:
    def __init__(self, x, y, width, height, state, Player):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.state = state
        self.hori = 0
        self.blood_state = 240
        self.shoot = False
        self.rifleman_right = Image(GET_PATH(IMG_SPRITE, Player+'_right001.png'), (2., 2.), 0., (0.52, 0.56))
        self.rifleman_left =  Image(GET_PATH(IMG_SPRITE, Player+'_left001.png'), (2., 2.), 0., (0.52, 0.56))
        self.shoot_left =     Image(GET_PATH(IMG_SPRITE, Player+'_shoot_left000.png'), (2., 2.), 0., (0.52, 0.56))
        self.shoot_right =    Image(GET_PATH(IMG_SPRITE, Player+'_shoot_right000.png'), (2., 2.), 0., (0.52, 0.56))
        self.obs_box = Rect(20, 30, 10, 10) # image space
        self.atk_box = Rect(10, 5, 30, 35) # image space
        self.blood_img_100 =  Image(GET_PATH(IMG_SPRITE, 'blood_100original.png'), (1, 1))
        self.blood_img_80 =   Image(GET_PATH(IMG_SPRITE, 'blood_80original.png'), (1, 1))
        self.blood_img_60 =   Image(GET_PATH(IMG_SPRITE, 'blood_60original.png'), (1, 1))
        self.blood_img_40 =   Image(GET_PATH(IMG_SPRITE, 'blood_40original.png'), (1, 1))
        self.blood_img_20 =   Image(GET_PATH(IMG_SPRITE, 'blood_20original.png'), (1, 1))
        self.blood_img_10 =   Image(GET_PATH(IMG_SPRITE, 'blood_10original.png'), (1, 1))
        self.blood_img_0 =    Image(GET_PATH(IMG_SPRITE, 'blood_0original.png'), (1, 1))


    def reset_state(self, x, y):
        self.x = x
        self.y = y
        self.blood_img_0.draw(self.x-25, self.y-40)
        self.obs_box = Rect(10, 30, 30, 10) # image space
        self.atk_box = Rect(10, 5, 30, 35) # image space
        # time.sleep(1)
        self.blood_state = 240


    def update_state(self, x, y, state, vertical, shoot):
        self.shoot = shoot
        if shoot == False:
            if (state == LEFT or state == RIGHT) and vertical == UP:
                self.y = y - 10
            elif (state == LEFT or state == RIGHT) and vertical == DOWN:
                self.y = y + 10
            elif state == LEFT:
                self.x = x - 10
                self.state = 3
            elif state == RIGHT:
                self.x = x + 10
                self.state = 4
        else:
            if state == LEFT:
                self.x = x + 20
                self.state = 3
            elif state == RIGHT:
                self.x = x - 20
                self.state = 4


    def store_state(self, num=0):
        store_arr.append([self.x, self.y, self.state])
        blood_arr.append([self.blood_state])


    def store_clear(self):
        store_arr.clear()
        blood_arr.clear()

    def release_state(self, num):
        self.x = store_arr[num][0]
        self.y = store_arr[num][1]
        self.state = store_arr[num][2]

    def draw_character(self):
        self.draw_blood(self.blood_state)
        #sprite
        if self.shoot == True:
            self.shoot = False
            if self.state == LEFT:
                self.shoot_left.draw(self.x, self.y)
            elif self.state == RIGHT:
                self.shoot_right.draw(self.x, self.y)

        #normal
        else:
            if self.state == LEFT:
                self.rifleman_left.draw(self.x, self.y)
            elif self.state == RIGHT:
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

    def game_over(self, blood_state, who, quit):
        notify_font = ui.notify_font # this should be refactored in the future
        if who == 1 and self.blood_state <= 0:
            notify_font.draw_str("Player1 game over", 200, 200)
        if who == 2 and self.blood_state <= 0:
            notify_font.draw_str("Player1 game over", 200, 200)

    def get_player1_point(self):
        return Player1_win

    def get_player2_point(self):
        return Player2_win
