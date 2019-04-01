import pygame
import pyscroll
import pygame.locals
import sys
import pytmx
import time

sys.path.append("../")
from utils import *
from shape import *
from asset import *
from font import *


store_arr = []
blood_arr = []


class Player:
    def __init__(self, x, y, width, height, state):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.state = state
        self.obs_box = Rect(self.x+20 , self.y+25 , 30, 20)
        self.atk_box = Rect(self.x, self.y, 100, 100)
        self.rifleman_down = Sprite(SP_ANIMATE, 'winchester_down', 3, ANI_LOOP, (0.5, 0.5), 0, (2.17, 2))
        self.rifleman_right = Sprite(SP_ANIMATE, 'winchester_right', 3, ANI_LOOP, (0.5, 0.5), 0, (2.17, 2))
        self.rifleman_left = Sprite(SP_ANIMATE, 'winchester_left', 3, ANI_LOOP, (0.5, 0.5), 0, (2.17, 2))
        self.rifleman_up = Sprite(SP_ANIMATE, 'winchester_up', 3, ANI_LOOP, (0.5, 0.5), 0, (2.17, 2))
        self.shoot_left = Sprite(SP_ANIMATE, 'shoot_left', 1, ANI_LOOP, (0.5, 0.5), 0, (2.17, 2))
        self.shoot_right = Sprite(SP_ANIMATE, 'shoot_right', 1, ANI_LOOP, (0.5, 0.5), 0, (2.17, 2))
        self.blood_state = 240
        self.blood_img_100 = Sprite(SP_ANIMATE, 'blood_100original', 1, ANI_LOOP, (0.5, 0.5), 0, (1, 1))
        self.blood_img_80 = Sprite(SP_ANIMATE, 'blood_80original', 1, ANI_LOOP, (0.5, 0.5), 0, (1, 1))
        self.blood_img_60 = Sprite(SP_ANIMATE, 'blood_60original', 1, ANI_LOOP, (0.5, 0.5), 0, (1, 1))
        self.blood_img_40 = Sprite(SP_ANIMATE, 'blood_40original', 1, ANI_LOOP, (0.5, 0.5), 0, (1, 1))
        self.blood_img_20 = Sprite(SP_ANIMATE, 'blood_20original', 1, ANI_LOOP, (0.5, 0.5), 0, (1, 1))
        self.blood_img_10 = Sprite(SP_ANIMATE, 'blood_10original', 1, ANI_LOOP, (0.5, 0.5), 0, (1, 1))
        self.blood_img_0 = Sprite(SP_ANIMATE, 'blood_0original', 1, ANI_LOOP, (0.5, 0.5), 0, (1, 1))


    def update_state(self, x, y, state):

        if state == 1:
            self.y = y - 10
            self.state = 1
        elif state == 2:
            self.y = y + 10
            self.state = 2
        elif state == 3:
            self.x = x - 10
            self.state = 3
        elif state == 4:
            self.x = x + 10
            self.state = 4
        elif state == 5:
            self.state = 5
        elif state == 6:
            self.state = 6
        self.obs_box = Rect(self.x+20 , self.y+25 , 30, 20)
        self.atk_box = Rect(self.x, self.y, 100, 100)

    def store_state(self, num=0):

        store_arr.append([self.x, self.y, self.state])
        blood_arr.append([self.blood_state])

    def release_state(self, num):
        self.x = store_arr[num][0]
        self.y = store_arr[num][1]
        self.state = store_arr[num][2]
        self.obs_box = Rect(self.x+20 , self.y+25 , 30, 20)
        self.atk_box = Rect(self.x, self.y, 100, 100)

    def store_clear(self):
        store_arr.clear()
        blood_arr.clear()

    def draw_character(self):

        self.draw_blood(self.blood_state)

        if self.state == 1:
            self.rifleman_up.draw(self.x, self.y)
        elif self.state == 2:
            self.rifleman_down.draw(self.x, self.y)
        elif self.state == 3:
            self.rifleman_left.draw(self.x, self.y)
        elif self.state == 4:
            self.rifleman_right.draw(self.x, self.y)
        elif self.state == 5:
            self.shoot_left.draw(self.x, self.y)
            self.state = 3
        elif self.state == 6:
            self.shoot_right.draw(self.x, self.y)
            self.state = 4


    def draw_blood(self, blood_state):
        if blood_state <= 0:
            self.blood_img_0.draw(self.x+20, self.y-20)
        if blood_state >= 0:
            self.blood_img_10.draw(self.x+20, self.y-20)
        if blood_state >= 40:
            self.blood_img_20.draw(self.x+20, self.y-20)
        if blood_state >= 80:
            self.blood_img_40.draw(self.x+20, self.y-20)
        if blood_state >= 120:
            self.blood_img_60.draw(self.x+20, self.y-20)
        if blood_state >= 160:
            self.blood_img_80.draw(self.x+20, self.y-20)
        if blood_state >= 200:
            self.blood_img_100.draw(self.x+20, self.y-20)

    def blood_update(self, blood):
        self.blood_state = self.blood_state - 1

    def game_over(self, blood_state, who, quit):
        self.p1_lose = Font("Player1 game over", "Georgia", (0,255,255), 50)
        self.p2_lose = Font("Player2 game over", "Georgia", (0,255,255), 50)

        if who == 1 and self.blood_state <= 0:
            self.p1_lose.draw_str(200, 200)

        if who == 2 and self.blood_state <= 0:
            self.p2_lose.draw_str(200, 200)