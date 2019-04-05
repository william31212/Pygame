import sys, pygame, os
sys.path.append("../RHframework/")
sys.path.append("../")
from input import *
from utils import *
from window import *
from asset import *
from shape import *
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
        self.keyboard.set_dbg_print(True)
        self.img = Image(GET_PATH(IMG_SPRITE, 'Player1_down000.png'), (2., 2.), 0., (0.52, 0.56))

    def update(self):
        kb = self.keyboard
        if kb.key_state[KEY_ESC]:
            self.ask_quit()

    def render(self):
        x = display_width/2
        y = display_height/2

        self.img.draw(x, y) # draw the image
        self.img.dbg_draw(x, y) # draw the image border

        obs_box = Rect(18, 33, 13, 7) # image space
        atk_box = Rect(17, 9, 15, 32) # image space

        # get left upper point of the img
        lu = self.img.get_left_upper()

        # draw obs_box
        dp.rect((0, 0, 0xff, 200), obs_box.to_screen_space(self.img).get_tuple(), 2)

        # draw atk_box
        dp.rect((0xca, 0x0a, 0xff, 200), atk_box.to_screen_space(self.img).get_tuple(), 2)

        # display green line
        dp.line((0, 255, 0, 128), (x, 0), (x, display_height))
        dp.line((0, 255, 0, 128), (0, y), (display_width, y))

    def ask_quit(self):
        print('On quit')
        self.quit()

def main():
    app = App('image_test_2', (display_width, display_height), W_OPENGL)
    app.run()

if __name__ == '__main__':
    main()
