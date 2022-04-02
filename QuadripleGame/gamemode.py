import pygame, maps
from pygame.locals import *
from loader import load_image
from random import randint

HALF_TILE = 500
FULL_TILE = 1000

COUNTDOWN_FULL = 3600
COUNTDOWN_EXTEND = 750

PENALTY_COOL = 180
FLAG_SCORE = 15
CRASH_PENALTY = 2


class Finish(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = load_image('finish.png', False)
		self.rect = self.image.get_rect()
		self.x = 5
		self.y = 5
		self.penalty_cool = PENALTY_COOL
		self.generate_finish()
		self.rect.topleft = self.x, self.y
		self.score = 0
		self.timeleft = COUNTDOWN_FULL


	def generate_finish(self):
		x = randint(0, 9)
		y = randint(0, 9)
		while maps.map_1[y][x] == 5:
			x = randint(0, 9)
			y = randint(0, 9)

		self.x = x * FULL_TILE + HALF_TILE
		self.y = y * FULL_TILE + HALF_TILE

		self.rect.topleft = self.x, self.y

	def reset(self):
		self.timeleft = COUNTDOWN_FULL
		self.score = 0
		self.generate_finish()

	def update(self, cam_x, cam_y):
		self.rect.topleft = self.x, self.y

		if self.penalty_cool > 0:
			self.penalty_cool -= 1

		if self.timeleft > 0:
			self.timeleft -= 1
