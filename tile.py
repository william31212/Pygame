import pygame
import pyscroll
import pygame.locals
import sys
import pytmx
import time

sys.path.append("../")

lists = []
obs = []
from utils import *

class TiledMap:
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm
        self.surface = pygame.Surface((self.width, self.height))

    def render(self):
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                lists.append(layer)
            if isinstance(layer, pytmx.TiledObjectGroup):
                obs.append(layer)


    def make_background(self):
        for iter_lists in lists:
            if iter_lists == self.tmxdata.get_layer_by_name('background'):
                for x, y, gid, in iter_lists:
                    tile = self.tmxdata.get_tile_image_by_gid(gid)
                    if tile:
                        self.surface.blit(tile, (x * self.tmxdata.tilewidth,
                                                 y * self.tmxdata.tileheight))
    def make_character(self):
        for iter_lists in lists:
            if iter_lists == self.tmxdata.get_layer_by_name('bridge'):
                for x, y, gid, in iter_lists:
                    tile = self.tmxdata.get_tile_image_by_gid(gid)
                    if tile:
                        self.surface.blit(tile, (x * self.tmxdata.tilewidth,
                                                 y * self.tmxdata.tileheight))
    def make_object(self):
        for iter_lists in lists:
            if iter_lists != self.tmxdata.get_layer_by_name('background'):
                for x, y, gid, in iter_lists:
                    tile = self.tmxdata.get_tile_image_by_gid(gid)
                    if tile:
                        self.surface.blit(tile, (x * self.tmxdata.tilewidth,
                                                 y * self.tmxdata.tileheight))
            if iter_lists != self.tmxdata.get_layer_by_name('character'):
                for x, y, gid, in iter_lists:
                    tile = self.tmxdata.get_tile_image_by_gid(gid)
                    if tile:
                        self.surface.blit(tile, (x * self.tmxdata.tilewidth,
                                                 y * self.tmxdata.tileheight))
    def make_obstacle(self):
        for x, y, gid, in obs:
            tile = tmxdata.get_tile_image_by_gid(gid)
            if tile:
                surface.blit(tile, (x * self.tmxdata.tilewidth,
                                    y * self.tmxdata.tileheight))
    # def make_background(self):


    # def make_character(self):


    # def make_obstacle(self):








