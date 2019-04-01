import pygame
import pyscroll
import pygame.locals
import sys
import pytmx
import time

from player import *

sys.path.append("../")
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
        self.bullet_right = Sprite(SP_ANIMATE, 'bullet_right', 3, ANI_LOOP, (0.5, 0.5), 0, (3, 3))
        self.bullet_left = Sprite(SP_ANIMATE, 'bullet_left', 3, ANI_LOOP, (0.5, 0.5), 0, (3, 3))

    def setting(self, x, y, state, who):
        if state == 1:
            self.x = x + 13
        else:
            self.x = x - 2
        self.y = y + 14
        self.state = state

        if who == 1:
            if len(store) == 0:
                self.new_bullet([self.x, self.y, self.state, self.speed],1)
            elif self.clock.getPassedSec() >= 0.5 and len(store) != 0:
                self.new_bullet([self.x, self.y, self.state, self.speed],1)
                self.clock.reset()
        elif who == 2:
            if len(store2) == 0:
                self.new_bullet([self.x, self.y, self.state, self.speed],2)
            elif self.clock.getPassedSec() >= 0.5 and len(store2) != 0:
                self.new_bullet([self.x, self.y, self.state, self.speed],2)
                self.clock.reset()


    def update_bullet(self):
        for i in store:
            if i[2] == 1:
                i[0] = i[0] + i[3]
            else:
                i[0] = i[0] - i[3]
        for i in store:
            if i[0] <= 0 or i[0] >= 800:
                store.remove(i)
                continue
            if i[1] <= 0 or i[1] >= 600:
                store.remove(i)
                continue

        for i in store2:
            if i[2] == 1:
                i[0] = i[0] + i[3]
            else:
                i[0] = i[0] - i[3 ]
        for i in store2:
            if i[0] <= 0 or i[0] >= 800:
                store2.remove(i)
                continue
            if i[1] <= 0 or i[1] >= 600:
                store2.remove(i)
                continue


    def shoot(self):
        for i in store:
            if i[2] == 1:
                self.bullet_right.draw(i[0], i[1])
            else:
                self.bullet_left.draw(i[0], i[1])

        for i in store2:
            if i[2] == 1:
                self.bullet_right.draw(i[0], i[1])
            else:
                self.bullet_left.draw(i[0], i[1])



    def new_bullet(self, new_bul, who):
        if who == 1:
            store.append(new_bul)
        if who == 2:
            store2.append(new_bul)






