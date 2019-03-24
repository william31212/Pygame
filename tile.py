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
obs = []
from utils import *

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
            if isinstance(layer, pytmx.TiledObjectGroup):
                obs.append(layer)
        pp.pprint(lists)

    def draw(self, func_draw_char):
        for i in lists:
            if i.name == 'character':
                func_draw_char()
            else:
                draw_layer(self.surface, i, self.tmxdata)