import pygame as pg
import sys
from pygame.locals import *

import mapGen
from collision import Collision
from draw import Draw
from ghost import Ghost
from player import Player


class Game:
    def __init__(self):
        self._running = True
        self._clock = pg.time.Clock()
        self.FPS = 10

        self.ghosts = []
        self.score = 0

    def on_init(self):
        self._running = True

        self.level = mapGen.Map()
        self.level.makeLevelVariables()
        self.draw = Draw()
        self.collision = Collision()

        # Get player and ghost variables from level class
        self.playerPos = self.level.playerPos
        ghostPos = self.level.ghosts

        self.player = Player(self.playerPos, self.level.walls)

        self.ghosts = []
        for i in range(0, len(ghostPos)):
            self.ghosts.append(Ghost(ghostPos[i], self.level.walls, Ghost.pathFindingAlgorithms[i], i))

    def on_event(self, event):
        if event.type == QUIT or \
           (event.type == KEYUP and event.key == K_ESCAPE):
            self._running = False

        self.player.userInput(event)

    def on_loop(self, events):

        self.playerPos = self.player.movePlayer()

        for ghost in self.ghosts:
            ghost.move(self.playerPos)

        self.collision.update(self.level.points, self.playerPos, self.level.superpoints)

        self.ghosts = self.collision.checkGhostCollision(self.playerPos, self.ghosts)
        # Get variables
        self.score = self.collision.score
        self.level.points = self.collision.points
        self.level.superpoints = self.collision.superPoints

    def on_render(self):
        # Draw() class renders everything.
        self.draw.update(pg)
        self.draw.drawWalls(self.level.walls)
        self.draw.drawPoints(self.level.points)
        self.draw.drawSuperPoints(self.level.superpoints)
        self.draw.drawPlayer(self.playerPos)
        self.draw.drawGhosts(self.ghosts)
        self.draw.drawScore(self.score)

        pg.display.flip()

    def on_terminate(self):
        pg.quit()
        sys.exit()

    def run(self):
        if self.on_init() is False:
            self._running = False

        while self._running:
            self._clock.tick(self.FPS)

            filtered_events = []
            for event in pg.event.get():
                self.on_event(event)
                if self._running:
                    filtered_events.append(event)
            self.on_loop(filtered_events)
            self.on_render()
        self.on_terminate()


if __name__ == '__main__':
    app = Game()
    app.run()
