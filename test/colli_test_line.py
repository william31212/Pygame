import sys, pygame, os
sys.path.append("../RHframework/")
sys.path.append("../")
from input import *
from utils import *
from shape import *
from window import *
import draw_premitive as dp

SET_ROOT('..')

display_width = 800
display_height = 600

class App(Window):
    def __init__(self, title, size, win_flag=W_NONE):
        super().__init__(title, size, win_flag)
        self.keyboard = KeyHandler()
        self.add_event_handle(self.keyboard.handle_event)
        self.mouse = MouseHandler()
        self.add_event_handle(self.mouse.handle_event)

    def setup(self):
        # self.line = Line((400, 0), (400, 600))
        self.line = Line((0, 300), (800, 300))
        # self.line = Line((0, 0), (800, 600))
        
        # TODO(roy4801): test circle hit line

    def update(self):
        mouse = self.mouse

        d = self.line.check_point((mouse.x, mouse.y))
        print(self.line.get_dis_point((mouse.x, mouse.y)))
        if d == LINE_RIGHT:
            print('right')
        elif d == LINE_ON:
            print('on')
        elif d == LINE_LEFT:
            print('left')


    def render(self):
        dp.line((255, 0, 0, 200), self.line.pt[0], self.line.pt[1])

    def ask_quit(self):
        print('On quit')
        self.quit()

def main():
    app = App('colli_test_line', (display_width, display_height), W_OPENGL)
    app.run()

if __name__ == '__main__':
    main()