import pygame
import pyscroll
import pygame.locals
import sys
import pytmx
import time

sys.path.append("../")
from utils import *

class TiledMap:
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        # print(ti)
        for layer in self.tmxdata.visible_layers:
            # print(pytmx.TiledTileLayer)
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    print(x,y,gid)
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth,
                                            y * self.tmxdata.tileheight))

    def make_map(self):
        temp_surface = pygame.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface




