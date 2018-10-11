from pathFind import PathFind


class Ghost(object):
	pathFindingAlgorithms = [
		'random',
		'dfsRandom',
		'aStar',
		'breadthFirstSearch',
		'dijkstra'
	]

	RED = (255, 0, 0)
	GREEN = (0, 204, 0)
	YELLOW = (255, 204, 0)
	BLUE = (0, 0, 204)
	PURPLE = (255, 0, 204)

	def __init__(self, position, walls, level, pathFindingAlgorithm='random', colorNum=0, speed_divider=5):
		self.position = position
		self.pathFind = PathFind(walls, level)

		self.colors = [
			self.GREEN,
			self.RED,
			self.YELLOW,
			self.BLUE,
			self.PURPLE
		]

		self.colour = self.colors[colorNum]

		self.dirs = [
			(0, -1),
			(0, 1),
			(1, 0),
			(-1, 0),
		]
		self.pathFindingAlgorithm = pathFindingAlgorithm

	def move(self, playerPos):
		if self.pathFindingAlgorithm == self.pathFindingAlgorithms[0]:
			self.position = self.pathFind.random(playerPos, self.position)
			pass
		elif self.pathFindingAlgorithm == self.pathFindingAlgorithms[1]:
			self.position = self.pathFind.breadth_first_search(playerPos, self.position)
			pass
		elif self.pathFindingAlgorithm == self.pathFindingAlgorithms[2]:
			self.position = self.pathFind.dfs_random(playerPos, self.position)
			pass
		elif self.pathFindingAlgorithm == self.pathFindingAlgorithms[3]:
			self.position = self.pathFind.a_star_search(playerPos, self.position)
			pass
		elif self.pathFindingAlgorithm == self.pathFindingAlgorithms[4]:
			self.position = self.pathFind.djikstra(playerPos, self.position)
			pass
