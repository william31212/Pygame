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
        if state == 1:
            self.x = x + 13
        else:
            self.x = x - 2
        self.y = y + 14
        self.state = state

        if len(self.bullet_list) == 0:
            self.new_bullet([self.x, self.y, self.state, self.speed])
        if self.clock.getPassedSec() >= 0.2 and len(self.bullet_list) > 0:
            self.new_bullet([self.x, self.y, self.state, self.speed])
            self.clock.reset()

    def hit_people(self, atk_box, update_blood, blood_state):
        # move the bullet
        for i in self.bullet_list:
            if i[2] == 1:
                i[0] = i[0] + i[3]
            else:
                i[0] = i[0] - i[3]
        # kill to each other
        for i in self.bullet_list:
            bullet_rect = Rect(i[0], i[1], 30, 30)
            if atk_box.check_rect(bullet_rect) == True:
                update_blood(blood_state, -20)
                self.bullet_list.remove(i)

    def hit_thing(self, bullet_thing):
        self.bullet_list.remove(bullet_thing)

    def shoot(self):
        for i in self.bullet_list:
            if i[2] == 1:
                self.bullet_right.draw(i[0], i[1])
            else:
                self.bullet_left.draw(i[0], i[1])

    def new_bullet(self, new_bul):
        self.bullet_list.append(new_bul)