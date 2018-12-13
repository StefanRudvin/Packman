import random
import copy
import heapq


def add_tuples(tuple1, tuple2):
	return tuple1[0] + tuple2[0], tuple1[1] + tuple2[1]


def heuristic(a, b):
	(x1, y1) = a
	(x2, y2) = b
	return abs(x1 - x2) + abs(y1 - y2)


class PathFind(object):
	def __init__(self, walls, level, speed_divider=1):
		self.walls = walls
		self.level = level
		self.dirs = [
			(0, -1),
			(0, 1),
			(1, 0),
			(-1, 0),
		]
		self.path = []
		self.counter = 0
		self.speedDivider = speed_divider
		self.nodes = self.make_nodes()
		self.playerPos = None
		self.two_previous = []

	def breadth_first_search(self, player_pos, ghost_pos):
		if not self.wait():
			return ghost_pos
		if player_pos == ghost_pos:
			return ghost_pos

		goal = tuple(player_pos)
		start = tuple(ghost_pos)
		visited = set()
		visited.add(start)
		q = [[start]]

		while q:
			path = q.pop(0)
			node = path[-1]

			if node == goal:
				self.path = path
				return path[1]

			for dir in self.available_dirs(node):
				next_node = (dir[0] + node[0], dir[1] + node[1])

				if next_node not in visited:
					visited.add(next_node)
					new_path = copy.copy(path)
					new_path.append(next_node)
					q.append(new_path)
		return ghost_pos


	def dfs_heuristic(self, player_pos, ghost_pos):
		if not self.wait():
			return ghost_pos
		if self.path and player_pos == self.playerPos:
			return self.path.pop()

		self.playerPos = player_pos
		goal = tuple(player_pos)
		start = tuple(ghost_pos)
		visited = [start]
		path = self.dfs_heuristic_recurse(start, goal, visited, [])
		if path:
			self.path = path
			return self.path.pop()
		else:
			return ghost_pos

	def dfs_heuristic_recurse(self, current_node, goal, visited, path):
		if not current_node:
			return None
		if current_node == goal:
			return current_node

		dir_copy = copy.copy(self.dirs)
		random.shuffle(dir_copy)

		for direction in self.available_dirs(current_node):
			next_node = add_tuples(direction, current_node)
			if next_node not in visited:
				visited.append(next_node)
				if self.dfs_heuristic_recurse(next_node, goal, visited, path):
					path.append(next_node)
					return path
		return None

	def dfs_random(self, player_pos, ghost_pos):
		if not self.wait():
			return ghost_pos
		if self.path and player_pos == self.playerPos:
			return self.path.pop()

		self.playerPos = player_pos
		goal = tuple(player_pos)
		start = tuple(ghost_pos)
		visited = [start]
		path = self.dfs_random_recurse(start, goal, visited, [])
		if path:
			self.path = path
			return self.path.pop()
		else:
			return ghost_pos

	def dfs_random_recurse(self, current_node, goal, visited, path):
		if not current_node:
			return None
		if current_node == goal:
			return current_node

		dir_copy = copy.copy(self.dirs)
		random.shuffle(dir_copy)
		for direction in dir_copy:
			next_node = add_tuples(direction, current_node)
			if next_node not in visited and next_node in self.nodes:
				visited.append(next_node)
				if self.dfs_random_recurse(next_node, goal, visited, path):
					path.append(next_node)
					return path
		return None

	def random(self, player_pos, ghost_pos):
		if not self.wait():
			return ghost_pos
		running = True
		final = None

		if len(self.two_previous) > 1:
			self.two_previous.pop(0)

		while running:
			available_dirs = self.available_dirs(ghost_pos)
			dir_num = random.randint(0, len(available_dirs) - 1)
			dir = available_dirs[dir_num]
			next_node = add_tuples(ghost_pos, dir)

			if next_node not in self.two_previous or len(available_dirs) == 1:
				running = False
				final = next_node

		self.two_previous.append(ghost_pos)

		if final:
			return final
		else:
			return ghost_pos

	def wait(self):
		if self.counter == self.speedDivider:
			self.counter = 0
			return True
		self.counter += 1
		return False

	def make_nodes(self):
		ar = []
		for x in range(self.level.height - 1):
			for y in range(self.level.width - 1):
				if [x, y] not in self.walls:
					ar.append((x, y))
		return ar

	def a_star_search(self, player_pos, ghost_pos):
		if not self.wait():
			return ghost_pos

		if player_pos == ghost_pos:
			return ghost_pos

		heap = []
		heapq.heappush(heap, (heuristic(ghost_pos, player_pos) + 0, ghost_pos, []))
		visited_set = set()
		ret = []

		while heap:
			heapq.heapify(heap)
			current_heap = heapq.heappop(heap)
			current_node = tuple(current_heap[1])
			current_path = current_heap[2]

			if current_node == player_pos:
				current_path.append(current_node)
				ret.append(current_path)
				self.path = current_path
				if len(current_path) > 1:
					return current_path[1]
				else:
					return current_path[0]

			if current_node in visited_set:
				continue
			visited_set.add(current_node)

			for direction in self.available_dirs(current_node):
				next_node = add_tuples(direction, current_node)
				cp = copy.copy(current_path)

				if next_node not in visited_set:
					cp.append(current_node)
					heapq.heappush(heap, (heuristic(next_node, player_pos) + len(cp), next_node, cp))
		return ghost_pos

	def best_first_search(self, player_pos, ghost_pos):
		if not self.wait():
			return ghost_pos

		if player_pos == ghost_pos:
			return ghost_pos

		heap = []
		heapq.heappush(heap, (heuristic(ghost_pos, player_pos), ghost_pos, []))
		visited_set = set()
		ret = []

		while heap:
			heapq.heapify(heap)
			current_heap = heapq.heappop(heap)
			current_node = tuple(current_heap[1])
			current_path = current_heap[2]

			if current_node == player_pos:
				current_path.append(current_node)
				ret.append(current_path)
				self.path = current_path
				if len(current_path) > 1:
					return current_path[1]
				else:
					return current_path[0]

			if current_node in visited_set:
				continue
			visited_set.add(current_node)

			for direction in self.available_dirs(current_node):
				next_node = add_tuples(direction, current_node)
				cp = copy.copy(current_path)

				if next_node not in visited_set:
					cp.append(current_node)
					heapq.heappush(heap, (heuristic(next_node, player_pos), next_node, cp))
		return ghost_pos

	def djikstra(self, player_pos, ghost_pos):
		if not self.wait():
			return ghost_pos
		if player_pos == ghost_pos:
			return ghost_pos

		heap = []
		heapq.heappush(heap, (0, ghost_pos, []))
		visited_set = set()
		visited_set.add(tuple(ghost_pos))

		while heap:
			heapq.heapify(heap)
			current_heap = heapq.heappop(heap)
			current_node = tuple(current_heap[1])
			current_path = current_heap[2]

			if current_node == player_pos:
				current_path.append(current_node)
				self.path = current_path
				if len(current_path) > 1:
					return current_path[1]
				else:
					return current_path[0]

			for direction in self.available_dirs(current_node):
				next_node = add_tuples(direction, current_node)
				cp = copy.copy(current_path)

				if next_node not in visited_set:
					visited_set.add(next_node)
					cp.append(current_node)
					heapq.heappush(heap, (len(cp), next_node, cp))
		return ghost_pos

	def available_dirs(self, current_node):
		ret = []
		for direction in self.dirs:
			next_node = add_tuples(direction, current_node)
			if next_node in self.nodes:
				ret.append(direction)
		return ret
