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
Player1_win = 0
Player2_win = 0

class Player:
    def __init__(self, x, y, width, height, state, Player):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.state = state
        self.blood_state = 240
        self.obs_box = Rect(self.x+20 , self.y+25 , 30, 20)
        self.atk_box = Rect(self.x, self.y, 80, 80)
        self.rifleman_down = Sprite(SP_ANIMATE, Player+'_down', 3, ANI_LOOP, (0.5, 0.5), 0, (2.17, 2))
        self.rifleman_right = Sprite(SP_ANIMATE, Player+'_right', 3, ANI_LOOP, (0.5, 0.5), 0, (2.17, 2))
        self.rifleman_left = Sprite(SP_ANIMATE, Player+'_left', 3, ANI_LOOP, (0.5, 0.5), 0, (2.17, 2))
        self.rifleman_up = Sprite(SP_ANIMATE, Player+'_up', 3, ANI_LOOP, (0.5, 0.5), 0, (2.17, 2))
        self.shoot_left = Sprite(SP_ANIMATE, Player+'_shoot_left', 1, ANI_LOOP, (0.5, 0.5), 0, (2.17, 2))
        self.shoot_right = Sprite(SP_ANIMATE, Player+'_shoot_right', 1, ANI_LOOP, (0.5, 0.5), 0, (2.17, 2))
        self.blood_img_100 = Image('./assets/sprite/' + 'blood_100original' + '.png', (1, 1))
        self.blood_img_80 = Image('./assets/sprite/' + 'blood_80original' + '.png', (1, 1))
        self.blood_img_60 = Image('./assets/sprite/' + 'blood_60original' + '.png', (1, 1))
        self.blood_img_40 = Image('./assets/sprite/' + 'blood_40original' + '.png', (1, 1))
        self.blood_img_20 = Image('./assets/sprite/' + 'blood_20original' + '.png', (1, 1))
        self.blood_img_10 = Image('./assets/sprite/' + 'blood_10original' + '.png', (1, 1))
        self.blood_img_0 = Image('./assets/sprite/' + 'blood_0original' + '.png', (1, 1))


    def reset_state(self, x, y):
        self.x = x
        self.y = y
        self.blood_img_0.draw(self.x-25, self.y-40)
        time.sleep(1)
        self.blood_state = 240

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
        self.atk_box = Rect(self.x, self.y, 80, 80)

    def store_state(self, num=0):
        store_arr.append([self.x, self.y, self.state])
        blood_arr.append([self.blood_state])

    def release_state(self, num):
        self.x = store_arr[num][0]
        self.y = store_arr[num][1]
        self.state = store_arr[num][2]
        self.obs_box = Rect(self.x+20 , self.y+25 , 30, 20)
        self.atk_box = Rect(self.x, self.y, 80, 80)

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
