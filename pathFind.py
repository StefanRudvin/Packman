import random
import copy
from queue import PriorityQueue


def add_tuples(tuple1, tuple2):
    return tuple1[0] + tuple2[0], tuple1[1] + tuple2[1]


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


class PathFind(object):
    def __init__(self, walls):
        self.walls = walls
        self.dirs = [
            (0, -1),
            (0, 1),
            (1, 0),
            (-1, 0),
        ]
        self.path = []
        self.counter = 0
        self.speedDivider = 5
        self.nodes = self.make_nodes()
        self.playerPos = None

    def breadth_first_search(self, player_pos, ghost_pos):
        if not self.wait():
            return ghost_pos
        if player_pos == ghost_pos:
            return ghost_pos

        goal = tuple(player_pos)
        start = tuple(ghost_pos)
        visited = [start]
        q = [[start]]

        while q:
            path = q.pop(0)
            node = path[-1]

            if node == goal:
                self.path = path
                return path[1]

            for dir in self.dirs:
                next_node = (dir[0] + node[0], dir[1] + node[1])

                if [next_node[0], next_node[1]] not in self.walls and next_node not in visited:
                    visited.append(next_node)
                    new_path = copy.deepcopy(path)
                    new_path.append(next_node)
                    q.append(new_path)
        return ghost_pos

    def djikstra(self):
        pass

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
        # print(dir_copy)
        # sorted(dir_copy, key=lambda tuple: self.heuristic(tuple, goal))
        ok = {}
        for direction in dir_copy:
            ok[heuristic(direction, goal)] = direction

        for direction in dir_copy:
            next_node = add_tuples(direction, current_node)
            if (list(next_node) not in self.walls and
                    next_node not in visited and
                    next_node in self.nodes):
                visited.append(next_node)
                # print(next_node)
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
            if (list(next_node) not in self.walls and
                    next_node not in visited and
                    next_node in self.nodes):
                visited.append(next_node)
                if self.dfs_random_recurse(next_node, goal, visited, path):
                    path.append(next_node)
                    return path
        return None

    def random(self, player_pos, ghost_pos):
        if not self.wait():
            return ghost_pos
        running = True

        while running:
            dir_num = random.randint(0, len(self.dirs) - 1)
            dir = self.dirs[dir_num]
            next_node = add_tuples(ghost_pos, dir)
            if [next_node[0], next_node[1]] not in self.walls and next_node[0] > 0 and next_node[1] > 0 and next_node[
                1] < 18:
                running = False
        return next_node

    def wait(self):
        if self.counter == self.speedDivider:
            self.counter = 0
            return True
        self.counter += 1
        return False

    def make_nodes(self):
        # Width: 18 Height: 20
        ar = []
        for x in range(18):
            for y in range(20):
                if [x, y] not in self.walls:
                    ar.append((x, y))
        return ar

    def brute_force(self, ghost_pos, player_pos):
        (a, b) = ghost_pos
        self.visited.append((a, b))

        if (a + 1, b) in self.nodes and (a + 1, b) not in self.visited:
            self.brute_force((a + 1, b), player_pos)
        if (a - 1, b) in self.nodes and (a - 1, b) not in self.visited:
            self.brute_force((a - 1, b), player_pos)
        if (a, b + 1) in self.nodes and (a, b + 1) not in self.visited:
            self.brute_force((a, b + 1), player_pos)
        if (a, b - 1) in self.nodes and (a, b - 1) not in self.visited:
            self.brute_force((a, b - 1), player_pos)

    def a_star_search(self, graph, start, goal):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break  # Found the goal

            for (x, y) in isNeighbour(current, graph):
                new_cost = cost_so_far[current] + cost(current, (x, y))

                if (x, y) not in cost_so_far or new_cost < cost_so_far[x, y]:
                    # If next (x,y) that isNeighbours provides is not in the dictionary of (x,y + cost) of past locations
                    # OR
                    # The newcost
                    cost_so_far[x, y] = new_cost
                    priority = new_cost + heuristic(goal, (x, y))
                    frontier.put((x, y), priority)
                    came_from[x, y] = current

        # return came_from, cost_so_far
        return frontier.get()
