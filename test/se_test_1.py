import sys, pygame, os
sys.path.append("../RHframework/")
sys.path.append("../")
from input import *
from utils import *
from sound import *
from window import *

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
        self.se = Sound(GET_PATH(SE_MAIN, 'ak47.wav'), S_PLAY_ONCE)
        self.se2 = Sound(GET_PATH(SE_MAIN, 'ak47reload.wav'), S_PLAY_ONCE)
        self.m = Sound(GET_PATH(SE_MAIN, 'test.wav'), S_PLAY_ONCE)

    def setup(self):
        self.m.play()

    def update(self):
        kb = self.keyboard

        if kb.key_state[KEY_v]:
            self.se.play()
        if kb.key_state[KEY_SLASH]:
            self.se2.play()

    def render(self):
        pass

    def ask_quit(self):
        print('On quit')
        self.quit()

def main():
    app = App('example', (display_width, display_height), W_OPENGL)
    app.run()

if __name__ == '__main__':
    main()