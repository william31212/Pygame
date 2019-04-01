import pygame
import pyscroll
import pygame.locals
import sys
import pytmx
import time

import draw_premitive


import pprint # test
pp = pprint.PrettyPrinter(indent=4)



# TODO: make them non-global
lists = []
sys.path.append("./RHframework")
from utils import *
from shape import *
from asset import *

def draw_layer(layer, tex_map, tile_size):
	for x, y, gid in layer:
		# print(x, y, gid)
		if gid in tex_map:
			tex_map[gid].draw(x*tile_size[0], y*tile_size[1])
# TODO: load custom attributes

class TiledMap:
	def __init__(self, filename):
		tm = pytmx.load_pygame(filename, pixelalpha=True)
		self.width = tm.width * tm.tilewidth
		self.height = tm.height * tm.tileheight
		self.tmxdata = tm
		self.tex_map = {}     # texture map (gid -> Image)

	def pick_layer(self):
		tmxdata = self.tmxdata
		tex_map = self.tex_map
		#
		for layer in tmxdata.visible_layers:
			if isinstance(layer, pytmx.TiledTileLayer):
				lists.append(layer)
		# Make the tex_map
		for layer in lists:
			for _, _, gid in layer:
				if gid != 0 and not gid in tex_map: # not zero
					tex_map[gid] = pygame_surface_to_image(tmxdata.get_tile_image_by_gid(gid))
					# print(tex_map[gid])

	def draw(self, func_draw_char):
		for i in lists:
			if i.name == 'character':
				for func in func_draw_char:
					func()
			else:
				draw_layer(i, self.tex_map, (self.get_tile_width(), self.get_tile_height()))
	# TODO: Refactor for performance
	def tile_object(self, obs_box, state, func_change, blood_change, num=0):
		for layer in self.tmxdata.layers:
			if isinstance(layer, pytmx.TiledObjectGroup) == True:
				if layer.properties['kill'] == 1:
					for object_iter in layer:
						obs_rec = Rect(object_iter.x, object_iter.y, object_iter.width, object_iter.height)
						# print(obs_box.x, obs_box.y)
						if obs_rec.check_rect(obs_box) == True and (state == 1):
							blood_change(num,-1)
						if obs_rec.check_rect(obs_box) == True and (state == 2):
							blood_change(num,-1)
						if obs_rec.check_rect(obs_box) == True and (state == 3):
							blood_change(num,-1)
						if obs_rec.check_rect(obs_box) == True and (state == 4):
							blood_change(num,-1)
						if obs_rec.check_rect(obs_box) == True and (state == 5):
							blood_change(num,-1)
						if obs_rec.check_rect(obs_box) == True and (state == 6):
							blood_change(num,-1)

				if layer.properties['collision'] == 1:
					for object_iter in layer:
						obs_rec = Rect(object_iter.x, object_iter.y, object_iter.width, object_iter.height)
						# print(obs_box.x, obs_box.y)
						if obs_rec.check_rect(obs_box) == True and (state == 1):
							func_change(num)
						if obs_rec.check_rect(obs_box) == True and (state == 2):
							func_change(num)
						if obs_rec.check_rect(obs_box) == True and (state == 3):
							func_change(num)
						if obs_rec.check_rect(obs_box) == True and (state == 4):
							func_change(num)
						if obs_rec.check_rect(obs_box) == True and (state == 5):
							func_change(num)
						if obs_rec.check_rect(obs_box) == True and (state == 6):
							func_change(num)

	# BUG(roy4801): draw_premitive fucked up here
	def dbg_draw_tile_object(self):
		for layer in self.tmxdata.layers:
			if isinstance(layer, pytmx.TiledObjectGroup) and layer.properties['collision'] == 1:
				for obj_iter in layer:
					# print((obj_iter.x, obj_iter.y, obj_iter.width, obj_iter.height))
					draw_premitive.rect((255, 0, 0), (obj_iter.x, obj_iter.y, obj_iter.width, obj_iter.height), 1)

	def get_map_width(self):
		return self.width
	def get_map_height(self):
		return self.height

	def get_tile_width(self):
		return self.tmxdata.tilewidth
	def get_tile_height(self):
		return self.tmxdata.tileheight

