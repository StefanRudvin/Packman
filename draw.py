import pygame as pg
import random
from ghost import Ghost


class Draw:
    """Draw class for OOP pacman"""

    def __init__(self):

        self.cell_size = 40
        self.size = self._width, self._height = 760, 840
        self._display_surface = None
        self._flags = pg.HWSURFACE | pg.DOUBLEBUF
        self.draw_path_bool = True

        self.BG_COLOR = (42, 45, 52)
        self.DARK_GRAY = (40, 40, 40)
        self.WHITE = (255, 255, 255)

        self.pointColour = (255, 100, 0)
        self.superPointColour = (255, 40, 255)
        self.playerColour = (255, 255, 0)
        self.wallColour = (40, 40, 40)

        self.wallColours = [
            (73, 73, 71),
            # (70,73,71),
            # (65,73,71),
            # (60,73,71),
        ]

        pg.init()
        self._display_surface = pg.display.set_mode(self.size, self._flags)
        pg.display.set_caption("Pacman")

        print("Draw class initialized.")

    def update(self, pg):
        self._display_surface.fill(self.BG_COLOR)
        # self.drawGrid(pg)

    def draw_grid(self, pg):
        for x in range(0, self._width, self.cell_size):
            pg.draw.line(self._display_surface,
                         self.DARK_GRAY, (x, 0), (x, self._height))

        for y in range(0, self._height, self.cell_size):
            pg.draw.line(self._display_surface,
                         self.DARK_GRAY, (0, y), (self._width, y))

    def draw_score(self, score):
        pg.draw.rect(self._display_surface, self.BG_COLOR,
                     (0, 0, 150, 40))

        BASICFONT = pg.font.Font('freesansbold.ttf', 22)
        scoreSurf = BASICFONT.render('Score: %s' % (score), True, self.WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (10, 10)
        self._display_surface.blit(scoreSurf, scoreRect)

    def draw_walls(self, wall):
        for i, (x, y) in enumerate(wall):
            randomInt = random.randint(0, len(self.wallColours) - 1)
            self.draw_rect(*self.convert_to_pixel(*wall[i]), self.wallColours[randomInt])

    def draw_points(self, p):
        for i, (x, y) in enumerate(p):
            self.draw_circle(*self.convert_to_pixel(*p[i]), self.pointColour)

    def draw_super_points(self, p):
        for i, (x, y) in enumerate(p):
            self.draw_circle(*self.convert_to_pixel(*p[i]), (200, 40, 40))

    def draw_player(self, player_pos):
        self.draw_player_items(*self.convert_to_pixel(*player_pos))

    def draw_player_items(self, x, y):
        self.draw_circle(x, y, self.playerColour, 2.5)

        i = self.cell_size
        pg.draw.circle(self._display_surface, self.BG_COLOR, (int(x + i / 1.5), int(y + i / 3)), int(i / 7))

        pg.draw.arc(
            self._display_surface,
            self.BG_COLOR,
            (100, 0, 100, 200),
            90,
            45)

    def draw_path(self, path, ghost):
        if not self.draw_path_bool:
            return
        for node in path:
            if ghost.colour == Ghost.PURPLE:
                pos = self.convert_to_pixel(node[0], node[1])
                self.draw_circle(pos[0] + 12, pos[1] + 12, ghost.colour, 7)
            elif ghost.colour == Ghost.YELLOW:
                pos = self.convert_to_pixel(node[0], node[1])
                self.draw_circle(pos[0] - 12, pos[1] + 12, ghost.colour, 7)
            elif ghost.colour == Ghost.BLUE:
                pos = self.convert_to_pixel(node[0], node[1])
                self.draw_circle(pos[0] - 12, pos[1] - 12, ghost.colour, 7)
            elif ghost.colour == Ghost.RED:
                pos = self.convert_to_pixel(node[0], node[1])
                self.draw_circle(pos[0] + 12, pos[1] - 12, ghost.colour, 7)

    def draw_ghosts(self, ghosts):
        for ghost in ghosts:
            if ghost.pathFind.path:
                self.draw_path(ghost.pathFind.path[1:], ghost)
            self.draw_circle(*self.convert_to_pixel(ghost.position[0], ghost.position[1]), ghost.colour, 2.5)

    def draw_rect(self, x, y, colour):
        i = self.cell_size
        pg.draw.rect(self._display_surface, colour, (x, y, i, i), 0)
        pg.draw.rect(self._display_surface, self.WHITE, (x, y, i, i), 2)

    def draw_circle(self, x, y, colour, size=4.2):
        i = self.cell_size
        pg.draw.circle(self._display_surface, colour, (int(x + i / 2), int(y + i / 2)), int(i / size))

    def draw_half_rect(self, x, y, colour):
        i = self.cell_size
        b = i / 3
        pg.draw.rect(self._display_surface, colour, (x + b, y + b, b, b), 0)
        pg.draw.rect(self._display_surface, self.WHITE,
                     (x + b, y + b, b, b), 2)

    def convert_to_pixel(self, x, y):
        return int(x * self.cell_size), int(y * self.cell_size)

    def _get_half_width(self):
        return self._width / 2

    def _get_half_height(self):
        return self._height / 2
