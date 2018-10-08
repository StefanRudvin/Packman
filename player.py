from pygame.locals import *

# Player class for pacmanOOP.
# Handles keyboard input & blocking.
# Returns players next move based on events.


class Player():

    def __init__(self, player_pos, walls):
        self.position = player_pos

        self.moveHor = 0
        self.moveVert = 0
        self.walls = walls
        self.debug = True

        if self.debug: print("Player class initialized.")

    def user_input(self, event):
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                self.moveHor = -1
                self.moveVert = 0
            elif (event.key == K_RIGHT or
                  event.key == K_d):
                self.moveHor = 1
                self.moveVert = 0

            elif (event.key == K_UP or
                  event.key == K_w):
                self.moveVert = 1
                self.moveHor = 0
            elif (event.key == K_DOWN or
                  event.key == K_s):
                self.moveVert = -1
                self.moveHor = 0

    def move(self):
        x = self.position
        h = self.moveHor
        v = self.moveVert

        if h != 0:
            if h == 1:
                x = (x[0] + 1, x[1])
            elif h == -1:
                x = (x[0] - 1, x[1])
            # h = 0
        elif v != 0:
            if v == 1:
                x = (x[0], x[1] - 1)
            elif v == -1:
                x = (x[0], x[1] + 1)
            # v = 0

        if not self.is_blocked(x[0], x[1]):
            if x[0] < 0:
                x = (18, x[1])
            elif x[0] > 18:
                x = (0, x[1])
            self.position = x

        self.moveHor = h
        self.moveVert = v

    def is_blocked(self, x, y):
        return [x, y] in self.walls
