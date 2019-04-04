import pygame
import pyscroll
import pygame.locals
import sys
import pytmx
import time

from player import *

sys.path.append("./RHframework")
from clock import Clock
from utils import *
from shape import *
from asset import *
from vector import *

class Bullet:
    def __init__(self, x, y, state, speed):
        self.x = x
        self.y = y
        self.state = state
        self.speed = speed
        self.clock = Clock()
        self.bullet_list = []
        self.bullet_right = Sprite(SP_ANIMATE, 'bullet_right', 3, ANI_LOOP, (0.5, 0.5), 0, (3, 3))
        self.bullet_left = Sprite(SP_ANIMATE, 'bullet_left', 3, ANI_LOOP, (0.5, 0.5), 0, (3, 3))

    def setting(self, x, y, state):
        if state == 1 or state == 4:
            self.x = x + 13
        if state == 2 or state == 3:
            self.x = x - 2
        self.y = y + 14
        self.state = state

        if self.clock.getPassedSec() >= 0.5 and len(self.bullet_list) > 0:
            self._new_bullet([self.x, self.y, self.state, self.speed])
            self.clock.reset()
        if len(self.bullet_list) == 0:
            self._new_bullet([self.x, self.y, self.state, self.speed])
            self.clock.reset()

    def hit_people(self, atk_box, update_blood, blood_state):
        # move the bullet
        for i in self.bullet_list:
            if i[2] == 4:
                i[0] = i[0] + i[3]
            if i[2] == 3:
                i[0] = i[0] - i[3]
        # kill to each other
        for i in self.bullet_list:
            bullet_rect = Rect(i[0], i[1], 30, 30)
            if atk_box.check_rect(bullet_rect) == True:
                update_blood(blood_state, -20)
                self.bullet_list.remove(i)

    def hit_thing(self, bullet_thing):
        self.bullet_list.remove(bullet_thing)

    def out_of_bound(self, display_x, display_y):
        for i in self.bullet_list:
            bullet_rect = Rect(i[0], i[1], 30, 30)
            if display_x <= i[0] or 0 >= i[0] or display_y <= i[1] or 0 >= i[1]:
                self.bullet_list.remove(i)

    def draw(self):
        for i in self.bullet_list:
            if i[2] == 4:
                self.bullet_right.draw(i[0], i[1])
            if i[2] == 3:
                self.bullet_left.draw(i[0], i[1])

    def _new_bullet(self, new_bul):
        self.bullet_list.append(new_bul)