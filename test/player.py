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

hold_x = 0
hold_y = 0
hold_state = 0


class Player:
    def __init__(self, x, y, width, height, state):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.state = state
        self.obs_box = Rect(self.x+41 , self.y+66 , 19, 10)
        self.atk_box = Rect(self.x, self.y, 100, 100)
        self.rifleman_down = Sprite(SP_ANIMATE, 'winchester_down', 3, ANI_LOOP, (0.5, 0.5), 0, (2.17, 2))
        self.rifleman_right = Sprite(SP_ANIMATE, 'winchester_right', 3, ANI_LOOP, (0.5, 0.5), 0, (2.17, 2))
        self.rifleman_left = Sprite(SP_ANIMATE, 'winchester_left', 3, ANI_LOOP, (0.5, 0.5), 0, (2.17, 2))
        self.rifleman_up = Sprite(SP_ANIMATE, 'winchester_up', 3, ANI_LOOP, (0.5, 0.5), 0, (2.17, 2))

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
        self.obs_box = Rect(self.x+41 , self.y+66 , 19, 10)
        self.atk_box = Rect(self.x, self.y, 100, 100)

    def store_state(self):
        global hold_x,hold_y,hold_state
        hold_x = self.x
        hold_y = self.y
        hold_state = self.state

    def release_state(self):
        global hold_x,hold_y,hold_state
        self.x = hold_x
        self.y = hold_y
        self.state = hold_state
        self.obs_box = Rect(self.x+41 , self.y+66 , 19, 10)
        self.atk_box = Rect(self.x, self.y, 100, 100)

    def draw_character(self):
        if self.state == 1:
            self.rifleman_up.draw(self.x, self.y)
        elif self.state == 2:
            self.rifleman_down.draw(self.x, self.y)
        elif self.state == 3:
            self.rifleman_left.draw(self.x, self.y)
        elif self.state == 4:
            self.rifleman_right.draw(self.x, self.y)
