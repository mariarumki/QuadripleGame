# load images
import os, sys, pygame
from pygame import *


def load_image(file, transparent=True):
	fullname = os.path.join('mediaofrace', file)

	image = pygame.image.load(fullname)
	if transparent == True:
		image = image.convert()
		colorkey = image.get_at((0, 0))
		image.set_colorkey(colorkey, RLEACCEL)
	else:
		image = image.convert_alpha()

	return image
