import os, sys, pygame, random, array
from typing import Union

from pygame import Surface
from pygame.sprite import Group
from pygame.surface import SurfaceType

import player, camera, maps, tracks, gamemode, bounds,traffic
from pygame.locals import *
from loader import load_image

TRAFFIC_COUNT = 45
CENTER_W = -1
CENTER_H = -1


def main():
	clock = pygame.time.Clock()
	running = True
	font = pygame.font.Font(None, 24)
	car = player.Player()
	cam = camera.Camera()
	target = gamemode.Finish()
	bound_alert = bounds.Alert()

	map_s: Group = pygame.sprite.Group()
	player_s = pygame.sprite.Group()
	traffic_s = pygame.sprite.Group()
	tracks_s = pygame.sprite.Group()
	target_s = pygame.sprite.Group()
	pointer_s = pygame.sprite.Group()

	for tile_num in range(0, len(maps.map_tile)):
		maps.map_files.append(load_image(maps.map_tile[tile_num]))

	for x in range(0, 10):
		for y in range(0, 10):
			map_s.add(maps.Map(maps.map_1[x][y], x * 1000, y * 1000, maps.map_1_rot[x][y]))


	tracks.initialize()
	target_s.add(target)
	#pointer_s.add(pointer)
	traffic.initialize(CENTER_W, CENTER_H)
	for count in range(0, TRAFFIC_COUNT):
		traffic_s.add(traffic.Traffic())

	player_s.add(car)
	cam.set_pos(car.x, car.y)

	while running:
		for event in pygame.event.get():
			keys = pygame.key.get_pressed()
			if event.type == pygame.KEYUP:
				if keys[K_p]:
					car.reset()
					target.reset()

				if keys[K_q]:
					pygame.quit()
					sys.exit(0)

			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				running = False
				break

		keys = pygame.key.get_pressed()
		if target.timeleft > 0:
			if keys[K_LEFT]:
				car.steerleft()

			if keys[K_RIGHT]:
				car.steerright()

			if keys[K_UP]:
				car.accelerate()

			if keys[K_DOWN]:
				car.deaccelerate()
		cam.set_pos(car.x, car.y)

		screen.blit(background, (0, 0))
		map_s.update(cam.x, cam.y)
		map_s.draw(screen)

		tracks_s.update(cam.x, cam.y)
		tracks_s.draw(screen)
		player_s.update(cam.x, cam.y)
		player_s.draw(screen)

		target_s.update(cam.x, cam.y)
		target_s.draw(screen)

		pygame.display.flip()
	if pygame.sprite.spritecollide(car,traffic_s,False):
		car.impact()
	if pygame.sprite.spritecollide(car,traffic_s,True):
		target.generate_finish()
		target_s.add(target)

	clock.tick(65)


pygame.init()
screen: Union[Surface, SurfaceType] = pygame.display.set_mode(
	(pygame.display.Info().current_w, pygame.display.Info().current_h),
	pygame.FULLSCREEN)
pygame.display.set_caption("Road Race")
pygame.mouse.set_visible(False)

CENTER_W = int(pygame.display.Info().current_w / 2)
CENTER_H = int(pygame.display.Info().current_h / 2)

# new bg surface

background = pygame.Surface(screen.get_size())
background = background.convert_alpha()
background.fill((26, 26, 26))

main()
pygame.quit()
sys.exit(0)
