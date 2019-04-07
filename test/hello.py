from __future__ import absolute_import

import pygame, sys
from OpenGL.GL import *
from OpenGL.GLU import *

sys.path.append('../RHframework')

from imgui_pygame_intergation import PygameRenderer
import imgui

# states for GUI
w_closable = True
cb_another = False
dg_val = 42.0

def main():
    pygame.init()

    size = 800, 600

    screen = pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.OPENGL)

    io = imgui.get_io()
    io.fonts.add_font_default()
    io.display_size = size

    renderer = PygameRenderer()

    clock = pygame.time.Clock()

    ## Test #######
    # Setup OpenGL for 2D rendering
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, size[0], size[1], 0.0) # Important
    glMatrixMode(GL_MODELVIEW)
    
    # new pygame.Surface
    test = pygame.Surface((300, 300))
    test_x = 100
    test_y = 100
    test.fill((255, 0, 0))
    tex_id = None

    # pygame surface to OpenGL tex
    ix, iy = test.get_width(), test.get_height()
    image = pygame.image.tostring(test, "RGBA", True)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    tex_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    ###############

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

        global cb_another, w_closable, dg_val

        if imgui.begin("Main window")[1]:
            imgui.begin_child("aaa", 300 , -10, border=False)
            imgui.begin_group()
            
            imgui.text("Toggle")

            _, cb_another = imgui.checkbox("Another Window", cb_another)
            imgui.text("Another Window state = {}".format(cb_another))

            w_closable = cb_another

            imgui.end_group()

            imgui.begin_group()
            imgui.text("Example: drag float")
            changed, test_x = imgui.drag_float(
                "test_x", test_x,
            )
            changed, test_y = imgui.drag_float(
                "test_y", test_y,
            )

            imgui.text("Changed: {}, x: {:.2f} y: {:.2f}".format(changed, test_x, test_y))
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

        # Clean screen
        glClearColor(0.5, 0.5, 0.5, 1)
        glClear(GL_COLOR_BUFFER_BIT)
        
        ## Draw ##########
        x = test_x
        y = test_y
        w = test.get_width()
        h = test.get_height()

        # Prepare the matrix
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(x, y, 0.0) # shift to (x, y)
        glBindTexture(GL_TEXTURE_2D, tex_id)

        # Actual draw
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 1.0); glVertex3f(0.0, 0.0,  0.0) # Left top
        glTexCoord2f(1.0, 1.0); glVertex3f(w,  0.0,  0.0)  # Right top
        glTexCoord2f(1.0, 0.0); glVertex3f(w, h,  0.0)     # Right bottom
        glTexCoord2f(0.0, 0.0); glVertex3f(0.0, h,  0.0)   # Left bottom
        glEnd()
        ##################

        imgui.render()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()