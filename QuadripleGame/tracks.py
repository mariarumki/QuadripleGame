import os,sys,pygame
from pygame.locals import *
from loader import load_image
LIFETIME =300


def rot_center(image,rect,angle):
	rot_image = pygame.transform.rotate(image,angle)
	rot_rect = rot_image.get_rect(center = rect.center)
	return rot_image,rot_rect


def initialize():
	global tracks_img


	tracks_img =load_image('tracks.png',False)

class Track(pygame.sprite.Sprite):
	def __init__(self,car_x,car_y,angle):
		self.image, self.rect = rot_center(tracks_img, tracks_img.get_rect(),angle)
		self.lifetime = LIFETIME

		self.screen =pygame.display.get_surface()
		self.x = car_x+3
		self.y = car_y+20

		self.rect.topleft = self.x,self.y

	def update(self,cam_x,cam_y):
		self.rect.topleft = self.x-cam_x,self.y-cam_y
		self.lifetime = self.lifetime-1

		if self.lifetime<1:
			pygame.sprite.Sprite.kill(self)




