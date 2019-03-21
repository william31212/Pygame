import pygame
import pygame.locals
import sys
import pytmx
import time

sys.path.append("../")
from utils import *
from tile import *

def main():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    maps = TiledMap("./level2.tmx")

    maps_img = maps.make_map()
    gameDisplay.blit(maps_img, (0,0))


    for tile_object in maps.tmxdata.objects:
        if tile_object.name == 'Pillar':
            rect = pygame.Rect( tile_object.x,  tile_object.y, tile_object.width, tile_object.height)
            # pygame.draw.rect(gameDisplay,(233,33,55),rect)
        if tile_object.name == 'lava':
            rect = pygame.Rect( tile_object.x,  tile_object.y, tile_object.width, tile_object.height)
            # pygame.draw.rect(gameDisplay,(233,33,55),rect)
        if tile_object.name == 'grass':
            rect = pygame.Rect( tile_object.x,  tile_object.y, tile_object.width, tile_object.height)
            # pygame.draw.rect(gameDisplay,(233,33,55),rect)

    pygame.display.update()



if __name__ == '__main__':
    gameDisplay = pygame.display.set_mode((800,640))

    while True:
        main()
