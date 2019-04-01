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

store = []
store2 = []


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
        if self.clock.getPassedSec() >= 0.5 and len(self.bullet_list) > 0:
            self.new_bullet([self.x, self.y, self.state, self.speed])
            self.clock.reset()



    def update_bullet(self):

        for i in self.bullet_list:
            if i[2] == 1:
                i[0] = i[0] + i[3]
            else:
                i[0] = i[0] - i[3]


    def shoot(self):
        for i in self.bullet_list:
            if i[2] == 1:
                self.bullet_right.draw(i[0], i[1])
            else:
                self.bullet_left.draw(i[0], i[1])



    def new_bullet(self, new_bul):
        self.bullet_list.append(new_bul)





