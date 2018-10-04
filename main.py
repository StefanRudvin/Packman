import pygame
import sys
from pygame.locals import *

class Game:

    def __init__(self):
        self._running = True
        self._clock = pygame.time.Clock()
        self.FPS = 20

        self.score = 0
        self.ghostPositions = []

    def on_init(self):
        self.level = map.make()
        self.level.makeLevelVariables()

        self.draw = Draw()

        self.playerPosition = self.level.playerPos
        self.ghostPositions = self.level.ghosts

        self.player = Player(self.playerPosition, self.level.walls)
        self.ghost1 = Ghost(self.ghostPositions[0], self.level.walls)


