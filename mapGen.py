import os


class Map():
    """This class opens Level.txt, creates an array out of it and variables for
    player, ghost, walls, points, superpoints. Also provides getter functions for
    each of the previous."""

    def __init__(self):
        self._filename = "Level.txt"
        self.level = []
        self.playerPos = (0, 0)
        self.ghosts = []
        self.walls = []
        self.points = []
        self.super_points = []

        print("MapGen class initialized.")

    def get_level(self):
        assert os.path.exists(
            self._filename), 'Cant find the level file: %s' % self._filename
        map_file = open(self._filename, 'r')
        content = map_file.readlines() + ['\r\n']
        map_file.close()

        level = []
        map_obj = []

        for line_num in range(len(content)):
            line = content[line_num].rstrip('\r\n')

            if line != '':
                level.append(line)

        for x in range(len(level[0])):
            map_obj.append([])
        for y in range(len(level)):
            for x in range(len(level[0])):
                map_obj[x].append(level[y][x])

        self.level = map_obj

    def make_level_variables(self):

        self.get_level()

        for x in range(len(self.level)):
            for y in range(len(self.level[0])):
                point = self.level[x][y]
                if point == "#":
                    self.walls.append([x, y])
                elif point == "@":
                    self.playerPos = (x, y)
                elif point == "1":
                    self.ghosts.append([x, y])
                elif point == "o":
                    self.points.append([x, y])
                elif point == "z":
                    self.super_points.append([x, y])
