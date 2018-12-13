from pathFind import PathFind
from timer import Timer

class Ghost(object):
	pathFindingAlgorithms = [
		'bestFirstSearch',
		'aStar',
		'breadthFirstSearch',
		'dfs',
		'dijkstra',
	]

	RED = (255, 0, 0)
	GREEN = (0, 204, 0)
	YELLOW = (255, 204, 0)
	BLUE = (0, 0, 204)
	PURPLE = (255, 0, 204)
	BLACK = (0, 0, 0)

	def __init__(self, position, walls, level, pathFindingAlgorithm='random', colorNum=0, speed_divider=3):
		self.position = position
		self.pathFind = PathFind(walls, level)
		self.initial_position = position
		self.counter = 0
		self.timer = Timer(pathFindingAlgorithm)

		self.colors = [
			self.RED,
			self.YELLOW,
			self.BLUE,
			self.PURPLE,
			self.GREEN,
			self.BLACK
		]
		self.color_num = colorNum

		self.colour = self.colors[self.color_num]

		self.dirs = [
			(0, -1),
			(0, 1),
			(1, 0),
			(-1, 0),
		]
		self.stay_dead = True
		self.pathFindingAlgorithm = pathFindingAlgorithm

	def die(self):
		self.position = self.initial_position
		self.colour = self.BLACK
		self.counter = 255

	def is_dead(self):
		if self.counter > 0:
			if self.stay_dead:
				if not self.timer.average_pathfind_time:
					self.timer.stop_search()
				return True

			self.colour = (255-self.counter, 0, 0)
			self.counter -= 1
			return True
		else:
			self.colour = self.colors[self.color_num]
			return False

	def move(self, player):
		if self.is_dead():
			return

		if not self.timer.start_time:
			self.timer.start_search()

		self.timer.start_pathfind()
		self.move_pos(player)
		self.timer.stop_pathfind()

	def move_pos(self, player):
		# if player.super_mode_counter > 0:
		# 	player_pos = self.initial_position
		# else:
		# 	player_pos = player.position
		player_pos = player.position

		# Best First
		if self.pathFindingAlgorithm == self.pathFindingAlgorithms[0]:
			self.position = self.pathFind.best_first_search(player_pos, self.position)
		# a Star
		elif self.pathFindingAlgorithm == self.pathFindingAlgorithms[1]:
			self.position = self.pathFind.a_star_search(player_pos, self.position)
		# BFS
		elif self.pathFindingAlgorithm == self.pathFindingAlgorithms[2]:
			self.position = self.pathFind.breadth_first_search(player_pos, self.position)
		# DFS
		elif self.pathFindingAlgorithm == self.pathFindingAlgorithms[3]:
			self.position = self.pathFind.dfs_random(player_pos, self.position)
		# DIJKSTRA
		elif self.pathFindingAlgorithm == self.pathFindingAlgorithms[4]:
			self.position = self.pathFind.djikstra(player_pos, self.position)

