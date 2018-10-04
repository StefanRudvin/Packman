from player import Player
import random, sys, copy


class Ghost(object):

    pathFindingAlgorithms = [
        'random',
        'breadthFirstSearch',
        'random',
        'random'
    ]

    def __init__(self, position, walls, pathFindingAlgorithm='random', colorNum = 0):
        self.walls = walls
        self.position = position
        self.nodes = self.makeNodes()
        self.found = 0
        self.visited = []
        self.debug = False

        self.colors = [
            (255, 0, 0),
            (0, 204, 0),
            (255, 204, 0),
            (0, 0, 204)
        ]

        self.colour = self.colors[colorNum]
        print("Ghost class initialized.")

        self.dirs = [
            (0, -1),
            (0, 1),
            (1, 0),
            (-1, 0),
        ]

        self.pathFindingAlgorithm = pathFindingAlgorithm

    def move(self, playerPos):
        if self.pathFindingAlgorithm == self.pathFindingAlgorithms[0]:
            self.position = self.random(playerPos)
        elif self.pathFindingAlgorithm == self.pathFindingAlgorithms[1]:
            self.position = self.breadthFirstSearch(playerPos)
        return self.position

    def bruteForce(self, ghostPos, playerPos):
            (a, b) = ghostPos
            self.visited.append((a,b))

            if (a + 1, b) in self.nodes and (a+1, b) not in self.visited:
                self.bruteForce((a + 1, b), playerPos)
            if (a - 1, b) in self.nodes and (a-1, b) not in self.visited:
                self.bruteForce((a - 1, b), playerPos)
            if (a, b + 1) in self.nodes and (a, b+1) not in self.visited:
                self.bruteForce((a, b + 1), playerPos)
            if (a, b - 1) in self.nodes and (a, b-1) not in self.visited:
                self.bruteForce((a, b - 1), playerPos)

    def random(self, playerPos):
        running = True
        ghostPos = self.position
        while running:
            dirNum = random.randint(0, len(self.dirs) - 1)
            dir = self.dirs[dirNum]
            nextNode = (ghostPos[0] + dir[0], ghostPos[1] + dir[1])
            if [nextNode[0], nextNode[1]] not in self.walls and nextNode[0] > 0 and nextNode[1] > 0 and nextNode[1] < 18:
                running = False
        return nextNode


    def breadthFirstSearch(self, playerPos):
        ghostPos = self.position
        goal = tuple(playerPos)
        start = tuple(ghostPos)
        visited = [start]

        q = [[start]]

        if playerPos == self.position:
            return self.position

        while q:
            path = q.pop(0)
            node = path[-1]

            if node == goal:
                return path[1]

            for dir in self.dirs:
                nextNode = (dir[0] + node[0], dir[1] + node[1])

                if [nextNode[0], nextNode[1]] not in self.walls and nextNode not in visited:
                    visited.append(nextNode)
                    newPath = copy.deepcopy(path)
                    newPath.append(nextNode)
                    q.append(newPath)
        return ghostPos

    def makeNodes(self):
        # Witdth: 18 Height: 20
        ar = []
        for x in range(18):
            for y in range(20):
                if [x, y] not in self.walls:
                    ar.append((x, y))
        return ar

    # Heuristics function takes 2 tuples of inputs, finds the heuristic distance between them.
    def heuristic(a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)

    def a_star_search(graph, start, goal):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break # Found the goal

            for (x,y) in isNeighbour(current,graph):
                new_cost = cost_so_far[current] + cost(current, (x,y))

                if (x,y) not in cost_so_far or new_cost < cost_so_far[x,y]:
                    # If next (x,y) that isNeighbours provides is not in the dictionary of (x,y + cost) of past locations
                    # OR
                    # The newcost
                    cost_so_far[x,y] = new_cost
                    priority = new_cost + heuristic(goal, (x,y))
                    frontier.put((x,y), priority)
                    came_from[x,y] = current

        #return came_from, cost_so_far
        return frontier.get()
