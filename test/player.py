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


store_arr = []


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
        # self.blood = Sprite(SP_ANIMATE, 'winchester_up', 1, ANI_LOOP, (0.5, 0.5), 0, (2.17, 2))

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
        self.obs_box = Rect(self.x+20 , self.y+25 , 30, 20)
        self.atk_box = Rect(self.x, self.y, 100, 100)

    def store_state(self, num=0):

        store_arr.append([self.x, self.y, self.state])
        # hold_x = self.x
        # hold_y = self.y
        # hold_state = self.state

    def release_state(self, num):
        # global hold_x,hold_y,hold_state
        self.x = store_arr[num][0]
        self.y = store_arr[num][1]
        self.state = store_arr[num][2]
        self.obs_box = Rect(self.x+20 , self.y+25 , 30, 20)
        self.atk_box = Rect(self.x, self.y, 100, 100)

    def store_clear(self):
        store_arr.clear()

    def draw_character(self):
        if self.state == 1:
            self.rifleman_up.draw(self.x, self.y)
        elif self.state == 2:
            self.rifleman_down.draw(self.x, self.y)
        elif self.state == 3:
            self.rifleman_left.draw(self.x, self.y)
        elif self.state == 4:
            self.rifleman_right.draw(self.x, self.y)
