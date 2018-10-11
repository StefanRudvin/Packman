import os


class Level:
	"""This class opens Level1.txt, creates an array out of it and variables for
	player, ghost, walls, points, superpoints. Also provides getter functions for
	each of the previous."""

	def __init__(self):
		self._filename = "Level1.txt"
		self.level = []
		self.playerPos = (0, 0)
		self.ghosts = []
		self.walls = []
		self.points = []
		self.super_points = []
		self.height = 0
		self.width = 0
		print("Level class initialized.")

	def create_level(self):
		if self.level:
			return self.level
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
		self.height = len(map_obj)
		self.width = len(map_obj[0])

	def make_level_variables(self):
		self.create_level()
		for x in range(self.height):
			for y in range(self.width):
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
