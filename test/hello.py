from __future__ import absolute_import

import sys

import pygame
import OpenGL.GL as gl

from imgui.integrations.pygame import PygameRenderer
import imgui

w_closable = True
cb_another = False

def main():
    pygame.init()

    size = 800, 600

    pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.OPENGL)

    io = imgui.get_io()
    io.fonts.add_font_default()
    io.display_size = size

    renderer = PygameRenderer()

    clock = pygame.time.Clock()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()

            renderer.process_event(event)

        # Start frame
        imgui.new_frame()

        if imgui.begin_main_menu_bar():
            if imgui.begin_menu("File", True):

                clicked_quit, selected_quit = imgui.menu_item(
                    "Quit", 'Cmd+Q', False, True
                )

                if clicked_quit:
                    exit(1)

                imgui.end_menu()
            imgui.end_main_menu_bar()

        global cb_another, w_closable

        if imgui.begin("Main window"):
            imgui.begin_child("aaa", 100, -10, border=False)
            imgui.begin_group()
            
            imgui.text("Toggle")

            _, cb_another = imgui.checkbox("Another Window", cb_another)
            imgui.text("Another Window state = {}".format(cb_another))

            w_closable = cb_another

            imgui.end_group()
            imgui.end_child()
            imgui.end()

        # Disable perm
        if w_closable:
            _, w_closable = imgui.begin("Another window", False) # return (collapse, state)
            imgui.text("Bar")
            imgui.text_colored("Eggs", 0.2, 1., 0.)
            imgui.text("AAAA")
            imgui.end()

        # note: cannot use screen.fill((1, 1, 1)) because pygame's screen
        #       does not support fill() on OpenGL sufraces
        gl.glClearColor(0.5, 0.5, 0.5, 1)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        imgui.render()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()