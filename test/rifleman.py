import sys, pygame

sys.path.append("../")
from clock import Clock
from Input import *
from asset import *
from utils import *
from tile import *
from shape import *

SET_ROOT('..')

display_width = 800
display_height = 600

rifleman_down = Sprite(SP_ANIMATE, GET_PATH(IMG_SPRITE, 'winchester_down'), 3, ANI_LOOP,0, (100, 100))
rifleman_right = Sprite(SP_ANIMATE, GET_PATH(IMG_SPRITE, 'winchester_right'), 3, ANI_LOOP, 0, (100, 100))
rifleman_left = Sprite(SP_ANIMATE, GET_PATH(IMG_SPRITE, 'winchester_left'), 3, ANI_LOOP, 0, (100, 100))
rifleman_up = Sprite(SP_ANIMATE, GET_PATH(IMG_SPRITE, 'winchester_up'), 3, ANI_LOOP, 0, (100, 100))

pos = [10, 10]
pos_tmp = [0, 0]
state = 2

clock = pygame.time.Clock()

def change():
	pos[0] = pos_tmp[0]
	pos[1] = pos_tmp[1]

# temp helper func
def to_pygame_rect(x):
	return (x.Left_x, x.Left_y, x.Right_x - x.Left_x, x.Right_y - x.Left_y)

def main():

	global state
	keyboard = KeyHandler()
	handle_keys = [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]
	handle_key_name = {KEY_UP:'KEY_UP', KEY_DOWN:'KEY_DOWN', KEY_LEFT:'KEY_LEFT', KEY_RIGHT:'KEY_RIGHT'}
	gameDisplay = pygame.display.set_mode((800,640))
	maps = TiledMap("./level2.tmx")
	maps_img = maps.make_map()

	while True:
		# Process event
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			# Keydown
			elif event.type == pygame.KEYDOWN:
				repeat = False
				if keyboard.get_key_state(event.key)[0]:
					repeat = True
				keyboard.set_key_state(event.key, True, repeat)
			# Keyup
			elif event.type == pygame.KEYUP:
				keyboard.set_key_state(event.key, False, False)

		# Update
		pos_tmp[0] = pos[0]
		pos_tmp[1] = pos[1]
		if keyboard.key_state[KEY_UP]:
			pos[1] -= 10
			state = 1
		if keyboard.key_state[KEY_DOWN]:
			pos[1] += 10
			state = 2
		if keyboard.key_state[KEY_LEFT]:
			pos[0] -= 10
			state = 3
		if keyboard.key_state[KEY_RIGHT]:
			pos[0] += 10
			state = 4

		rifleman_obs_box = None
		obs_list = []

		##obstacle
		for tile_object in maps.tmxdata.objects:
			rifleman_obs_box = Rect(pos[0]+41, pos[1]+66, pos[0]+60, pos[1]+76)
			# print("rifleman_obs_box : Lx:{} Ly:{} Rx:{} Ry:{}".format(pos[0]+30, pos[1]+30, pos[0]+70, pos[1]+70))
			if tile_object.name == 'Pillar':
				pilliar_obs_box = Rect(tile_object.x, tile_object.y, tile_object.x + tile_object.width, tile_object.y + tile_object.height)
				obs_list.append(pilliar_obs_box)
				# print("Lx:{} Ly:{} Rx:{} Ry:{}".format(tile_object.x,tile_object.y,tile_object.x + tile_object.width,tile_object.y+tile_object.height))
				if pilliar_obs_box.check_rect(rifleman_obs_box) == True and (state == 1):
					change()
				if pilliar_obs_box.check_rect(rifleman_obs_box) == True and (state == 2):
					change()
				if pilliar_obs_box.check_rect(rifleman_obs_box) == True and (state == 3):
					change()
				if pilliar_obs_box.check_rect(rifleman_obs_box) == True and (state == 4):
					change()
			if tile_object.name == 'grass':
				grass_obs_box = Rect(tile_object.x, tile_object.y, tile_object.x + tile_object.width, tile_object.y + tile_object.height)
				obs_list.append(grass_obs_box)
				# print("Lx:{} Ly:{} Rx:{} Ry:{}".format(tile_object.x,tile_object.y,tile_object.x + tile_object.width,tile_object.y+tile_object.height))
				if grass_obs_box.check_rect(rifleman_obs_box) == True and (state == 1):
					change()
				if grass_obs_box.check_rect(rifleman_obs_box) == True and (state == 2):
					change()
				if grass_obs_box.check_rect(rifleman_obs_box) == True and (state == 3):
					change()
				if grass_obs_box.check_rect(rifleman_obs_box) == True and (state == 4):
					change()
			if tile_object.name == 'lava':
				lava_obs_box = Rect(tile_object.x, tile_object.y, tile_object.x + tile_object.width, tile_object.y + tile_object.height)
				obs_list.append(lava_obs_box)
				# print("Lx:{} Ly:{} Rx:{} Ry:{}".format(tile_object.x,tile_object.y,tile_object.x + tile_object.width,tile_object.y+tile_object.height))
				if lava_obs_box.check_rect(rifleman_obs_box) == True and (state == 1):
					print("you died")
				if lava_obs_box.check_rect(rifleman_obs_box) == True and (state == 2):
					print("you died")
				if lava_obs_box.check_rect(rifleman_obs_box) == True and (state == 3):
					print("you died")
				if lava_obs_box.check_rect(rifleman_obs_box) == True and (state == 4):
					print("you died")
			if tile_object.name == 'edge':
				edge_obs_box = Rect(tile_object.x, tile_object.y, tile_object.x + tile_object.width, tile_object.y + tile_object.height)
				obs_list.append(edge_obs_box)
				# print("fucker : Lx:{} Ly:{} Rx:{} Ry:{}".format(tile_object.x, tile_object.y, (tile_object.x + tile_object.width), (tile_object.y+tile_object.height)))
				# print(edge_obs_box.check_rect(rifleman_obs_box))
				if edge_obs_box.check_rect(rifleman_obs_box) == True and (state == 1):
					change()
				if edge_obs_box.check_rect(rifleman_obs_box) == True and (state == 2):
					change()
				if edge_obs_box.check_rect(rifleman_obs_box) == True and (state == 3):
					change()
				if edge_obs_box.check_rect(rifleman_obs_box) == True and (state == 4):
					change()

		##edge
		if pos[0] <= -30:
			pos[0] = 760
		elif pos[1] <= -30:
			pos[1] = 640
		elif pos[0] >= 760:
			pos[0] = -30
		elif pos[1] >= 640:
			pos[1] = -30

		##draw
		gameDisplay.blit(maps_img, (0,0))
		if state == 1:
			rifleman_up.draw(pos[0],pos[1])
		elif state == 2:
			rifleman_down.draw(pos[0],pos[1])
		elif state == 3:
			rifleman_left.draw(pos[0],pos[1])
		elif state == 4:
			rifleman_right.draw(pos[0],pos[1])

		## dbg view ##
		pygame.draw.circle(gameDisplay, (0xe5, 0, 0xff), (pos[0], pos[1]), 2)
		for i in obs_list:
			pygame.draw.rect(gameDisplay,(255, 0, 0), to_pygame_rect(i), 2)
		pygame.draw.rect(gameDisplay,(0, 0, 255), to_pygame_rect(rifleman_obs_box))
		## dbg view ##

		pygame.display.update()
		clock.tick(60)

if __name__ == '__main__':
	pygame.init()
	main()