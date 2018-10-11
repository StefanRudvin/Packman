import pygame as pg
import sys
from pygame.locals import *

from level import Level
from collision import Collision
from draw import Draw
from ghost import Ghost
from player import Player


def on_terminate():
	pg.quit()
	sys.exit()


class Game:
	def __init__(self):
		self._running = True
		self._clock = pg.time.Clock()
		self.FPS = 24

		self.ghosts = []
		self.player = None
		self.score = 0

		self._running = True
		self._pause = False

		self.level = Level()
		self.level.make_level_variables()
		self.draw = Draw()
		self.collision = Collision()

	def on_init(self):
		# Get player and ghost variables from level class
		player_pos = self.level.playerPos
		ghost_pos = self.level.ghosts

		self.player = Player(player_pos, self.level.walls)

		self.ghosts = []
		for i in range(0, len(ghost_pos)):
			self.ghosts.append(Ghost(ghost_pos[i], self.level.walls, Ghost.pathFindingAlgorithms[i], i, i * 2))

	def on_event(self, event):
		self.system_keys(event)
		self.player.user_input(event)

	def on_loop(self, events):
		self.player.move()

		for ghost in self.ghosts:
			ghost.move(self.player.position)

		self.collision.update(self.level.points, self.player.position, self.level.super_points)

		self.ghosts = self.collision.check_ghost_collision(self.player.position, self.ghosts)
		# Get variables
		self.score = self.collision.score
		self.level.points = self.collision.points
		self.level.superPoints = self.collision.superPoints

	def on_render(self):
		self.draw.update(pg)
		self.draw.draw_walls(self.level.walls)
		self.draw.draw_points(self.level.points)
		self.draw.draw_super_points(self.level.super_points)
		self.draw.draw_ghosts(self.ghosts)
		self.draw.draw_score(self.score)
		self.draw.draw_player(self.player.position)
		pg.display.flip()

	def system_keys(self, event):
		if event.type == KEYUP and event.key == K_p:
			self._pause = not self._pause
		elif event.type == KEYUP and event.key == K_ESCAPE:
			on_terminate()

	def run(self):
		if self.on_init() is False:
			self._running = False

		while self._running:
			if self._pause:
				for event in pg.event.get(): self.system_keys(event)
				continue

			self._clock.tick(self.FPS)

			filtered_events = []
			for event in pg.event.get():
				self.on_event(event)
				if self._running:
					filtered_events.append(event)
			self.on_loop(filtered_events)
			self.on_render()
		on_terminate()


if __name__ == '__main__':
	app = Game()
	app.run()
