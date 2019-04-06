import sys, pygame, os, math, random
sys.path.append("../RHframework/")
sys.path.append("../")
from input import *
from utils import *
from window import *
from shape import *
from asset import *
import draw_premitive as dp

SET_ROOT('..')

display_width = 800
display_height = 600

class Ball:
    img = None
    moveUnit = 5

    def __init__(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta
        self.coll = Circle(7, 7, 8)
        self.speed = 1.0

    def update(self):
        theta = self.theta
        self.x += self.speed * self.moveUnit * math.cos(math.radians(theta))
        self.y += self.speed * self.moveUnit * math.sin(math.radians(theta))

    def is_hit(self, line):
        obs_cir = self.coll.to_screen_space((self.x, self.y), Ball.img)
        return obs_cir.check_line(line)

    def draw(self):
        self.image.draw(self.x, self.y)
        # self.coll.to_screen_space(self.image).dbg_draw()
        Ball.img.draw(self.x, self.y)
        # self.coll.to_screen_space((self.x, self.y), Ball.img)


class App(Window):
    def __init__(self, title, size, win_flag=W_NONE):
        super().__init__(title, size, win_flag)
        self.keyboard = KeyHandler()
        self.add_event_handle(self.keyboard.handle_event)
        self.mouse = MouseHandler()
        self.add_event_handle(self.mouse.handle_event)

    def setup(self):
        Ball.img = Image('ball.png', (1., 1.), 0., (0.5, 0.5))
        self.border = Rect(100, 100, 400, 400).to_line_list()
        # dbg
        for i in self.border:
            print(i)
        ###
        self.ball_list = []

    def update(self):
        mouse = self.mouse

        if mouse.btn[MOUSE_L]:
            self.ball_list.append(Ball(mouse.x, mouse.y, random.uniform(0, 360)))

        for b in self.ball_list:
            b.update()

        # bug
        for b in self.ball_list:
            for l in self.border:
                if b.is_hit(l):
                    b.speed = 0

    def render(self):
        for l in self.border:
            dp.line((255, 0, 0, 200), l.pt[0], l.pt[1], 1)

        for i in self.ball_list:
            i.draw()

    def ask_quit(self):
        print('On quit')
        self.quit()

def main():
    app = App('ball_colli', (display_width, display_height), W_OPENGL)
    app.run()

if __name__ == '__main__':
    main()