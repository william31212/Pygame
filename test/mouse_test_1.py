import sys, pygame, os
sys.path.append("../")

from Input import MouseHandler

m = MouseHandler()
def main():
	global f_print
	while True:
		for e in pygame.event.get():
			os.system('clear')
			if e.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif e.type == pygame.MOUSEMOTION:
				m.set_motion(e.pos, e.rel, e.buttons)
			elif e.type == pygame.MOUSEBUTTONDOWN:
				m.set_mbtn_down(e.pos, e.button)
			elif e.type == pygame.MOUSEBUTTONUP:
				m.set_mbtn_up(e.pos, e.button)
			print(m)

if __name__ == '__main__':
	pygame.init()
	gameDisplay = pygame.display.set_mode((800, 600))
	pygame.display.set_caption('mouse_test_1')
	main()