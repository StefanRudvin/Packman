import pygame as pg
from pygame.locals import *
import random


class Draw():
    """Draw class for OOP pacman"""

    def __init__(self):

        self._cellsize = 40
        self.size = self._width, self._height = 760, 840
        self._display_surface = None
        self._flags = pg.HWSURFACE | pg.DOUBLEBUF

        self.BGCOLOR = (42,45,52)
        self.DARKGRAY = (40, 40, 40)
        self.WHITE = (255, 255, 255)

        self.pointColour = (255, 153, 0)
        self.superPointColour = (255, 40, 255)
        self.playerColour = (255, 255, 0)
        self.wallColour = (40, 40, 40)

        self.wallColours = [
            (73,73,71),
            (70,73,71),
            (65,73,71),
            (60,73,71),
            ]

        pg.init()
        self._display_surface = pg.display.set_mode(self.size, self._flags)
        pg.display.set_caption("Pacman")

        print("Draw class initialized.")

    def update(self, pg):
        self._display_surface.fill(self.BGCOLOR)
        # self.drawGrid(pg)

    def drawGrid(self, pg):
        for x in range(0, self._width, self._cellsize):
            pg.draw.line(self._display_surface,
                         self.DARKGRAY, (x, 0), (x, self._height))

        for y in range(0, self._height, self._cellsize):
            pg.draw.line(self._display_surface,
                         self.DARKGRAY, (0, y), (self._width, y))

    def drawScore(self, score):
        pg.draw.rect(self._display_surface, self.WHITE,
                     (0, 0, 120, 40))

        BASICFONT = pg.font.Font('freesansbold.ttf',18)
        scoreSurf = BASICFONT.render('Score: %s' % (score), True, self.BGCOLOR)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (10,10)
        self._display_surface.blit(scoreSurf,scoreRect)

    def drawWalls(self, wall):
        for i, (x, y) in enumerate(wall):
            randomInt = random.randint(0, len(self.wallColours) - 1)
            self.drawRect(*self.convertToPixel(*wall[i]), self.wallColours[randomInt])

    def drawPoints(self, p):
        for i, (x, y) in enumerate(p):
            self.drawCircle(*self.convertToPixel(*p[i]), self.pointColour)

    def drawSuperPoints(self, p):
        for i, (x, y) in enumerate(p):
            self.drawCircle(*self.convertToPixel(*p[i]), (random.randint(200, 250), 40, 40))

    def colourRange(self):
        return

    def drawPlayer(self, playerPos):
        self.drawPlayerItems(*self.convertToPixel(*playerPos))

    def drawPlayerItems(self, x, y):
        self.drawCircle(x, y, self.playerColour, 2.5)

        i = self._cellsize
        pg.draw.circle(self._display_surface, self.BGCOLOR, (int(x+i/1.5), int(y + i/3)), int(i/7))

        pg.draw.arc(
        self._display_surface,
        self.BGCOLOR,
        (100,0,100,200),
        90,
        45)

    def drawGhosts(self, ghosts):
        for ghost in ghosts:
            self.drawRect(*self.convertToPixel(ghost.position[0], ghost.position[1]), ghost.colour)

    def drawRect(self, x, y, colour):
        i = self._cellsize
        pg.draw.rect(self._display_surface, colour, (x, y, i, i), 0)
        pg.draw.rect(self._display_surface, self.WHITE, (x, y, i, i), 2)

    def drawCircle(self, x, y, colour, size = 4.2):
        i = self._cellsize
        pg.draw.circle(self._display_surface, colour, (int(x+i/2), int(y + i/2)), int(i/size))

    def drawHalfRect(self, x, y, colour):
        i = self._cellsize
        b = i / 3
        pg.draw.rect(self._display_surface, colour, (x + b, y + b, b, b), 0)
        pg.draw.rect(self._display_surface, self.WHITE,
                     (x + b, y + b, b, b), 2)

    def convertToPixel(self, x, y):
        return int(x * self._cellsize), int(y * self._cellsize)

    def _get_half_width(self):
        return self._width / 2

    def _get_half_height(self):
        return self._height / 2
