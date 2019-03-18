import sys, pygame

sys.path.append("../")
from clock import Clock
from Input import *
from asset import *
from utils import *

SET_ROOT('..')

display_width = 800
display_height = 600

rifleman_down = Sprite(SP_ANIMATE, "winchester_down", 3, ANI_LOOP,0,1)
rifleman_right = Sprite(SP_ANIMATE, "winchester_right", 3, ANI_LOOP,0,1)
rifleman_left = Sprite(SP_ANIMATE, "winchester_left", 3, ANI_LOOP,0,1)
rifleman_up = Sprite(SP_ANIMATE, "winchester_up", 3, ANI_LOOP,0,1)


pos = [10, 10]
state = 2

def main():

	global state
	keyboard = KeyHandler()
	handle_keys = [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]
	handle_key_name = {KEY_UP:'KEY_UP', KEY_DOWN:'KEY_DOWN', KEY_LEFT:'KEY_LEFT', KEY_RIGHT:'KEY_RIGHT'}
	gameDisplay = pygame.display.set_mode((display_width,display_height))
	keyboard = KeyHandler()

	while True:

		gameDisplay.fill((163, 148, 128))
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

		for i in handle_keys:
			any_pressed = False
			if keyboard.key_state[i]:
				if handle_key_name[i] == 'KEY_UP':
					pos[1] -= 10
					state = 1
					rifleman_up.draw(pos[0],pos[1])
				elif handle_key_name[i] == 'KEY_DOWN':
					pos[1] += 10
					state = 2
					rifleman_down.draw(pos[0],pos[1])
				elif handle_key_name[i] == 'KEY_LEFT':
					pos[0] -= 10
					state = 3
					rifleman_left.draw(pos[0],pos[1])
				elif handle_key_name[i] == 'KEY_RIGHT':
					pos[0] += 10
					state = 4
					rifleman_right.draw(pos[0],pos[1])

		if state == 1:
			rifleman_up.draw(pos[0],pos[1])
		if state == 2:
			rifleman_down.draw(pos[0],pos[1])
		if state == 3:
			rifleman_left.draw(pos[0],pos[1])
		if state == 4:
			rifleman_right.draw(pos[0],pos[1])




		pygame.display.update()
		clock = pygame.time.Clock()
		clock.tick(60)




if __name__ == "__main__":
	pygame.init()

	main()