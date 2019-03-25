import pygame
import pyscroll
import pygame.locals
import sys
import pytmx
import time

import pprint # test

pp = pprint.PrettyPrinter(indent=4)

sys.path.append("../")

# TODO: make them non-global
lists = []

from utils import *
from shape import *

def draw_layer(surface, layer, tmxdata):
    for x, y, gid in layer:
        # print('{} {} {}'.format(x, y, gid))
        tile = tmxdata.get_tile_image_by_gid(gid)
        if tile:
            surface.blit(tile, (x * tmxdata.tilewidth,
                                y * tmxdata.tileheight))

# TODO: load custom attributes

class TiledMap:
    def __init__(self, filename, surface):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm
        self.surface = surface

    def pick_layer(self):
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                lists.append(layer)

    def draw(self, func_draw_char):
        for i in lists:
            if i.name == 'character':
                func_draw_char()
            else:
                draw_layer(self.surface, i, self.tmxdata)

    def tile_object(self, obs_box, state, func_change):

        for layer in self.tmxdata.layers:
            if isinstance(layer, pytmx.TiledObjectGroup) == True:
                if layer.properties['collision'] == 1:
                    for object_iter in layer:
                        obs_rec = Rect(object_iter.x, object_iter.y, object_iter.width, object_iter.height )

                        print(obs_box.x, obs_box.y)
                        if obs_rec.check_rect(obs_box) == True and (state == 1):
                            func_change()
                        if obs_rec.check_rect(obs_box) == True and (state == 2):
                            func_change()
                        if obs_rec.check_rect(obs_box) == True and (state == 3):
                            func_change()
                        if obs_rec.check_rect(obs_box) == True and (state == 4):
                            func_change()
                else:
                    continue

