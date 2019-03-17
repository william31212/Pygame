import pygame, sys, os

PATH = os.path.join('..', 'assets', 'img')

screen = None

img = None
img_w = 0
img_h = 0

def main():
	while True:
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		screen.fill((128, 128, 128))
		# normal
		screen.blit(img, (0, 0))
		# x-way
		screen.blit(pygame.transform.flip(img, True, False), (img_w, 0))
		# y-way
		screen.blit(pygame.transform.flip(img, False, True), (2*img_w, 0))
		# x and y-way
		screen.blit(pygame.transform.flip(img, True, True), (3*img_w, 0))

		# Rotate
		screen.blit(pygame.transform.rotate(img, 45.), (4*img_w, 0))

		rot = pygame.transform.rotate(img, 45.)
		screen.blit(pygame.transform.scale(rot, (rot.get_width()//2, rot.get_height()//2)), (5*img_w, 0))

		############################################
		# Scale
		screen.blit(pygame.transform.scale(img, (2*img_w, 2*img_h)), (0, 2*img_h))
		# scale2x (AdvanceMAME Scale2X algorithm)
		screen.blit(pygame.transform.scale2x(img), (2*img_w, 2*img_h))
		# smoothScale
		screen.blit(pygame.transform.smoothscale(img, (2*img_w, 2*img_h)), (4*img_w, 2*img_h))

		pygame.display.update()

if __name__ == "__main__":
	pygame.init()

	# Load image
	img = pygame.image.load(os.path.join(PATH, 'attackA000.png'))
	img = img.convert(32)
	img_w = img.get_width()
	img_h = img.get_height()
	print(img_w, img_h)
	print(img.get_bitsize())

	screen = pygame.display.set_mode((800, 600))
	main()