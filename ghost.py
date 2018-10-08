from player import Player
import random, sys, copy
from pathFind import PathFind


class Ghost(object):

    pathFindingAlgorithms = [
        'random',
        'breadthFirstSearch',
        'dfsRandom',
        'dfsHeuristic'
    ]

    RED = (255, 0, 0)
    GREEN = (0, 204, 0)
    YELLOW = (255, 204, 0)
    BLUE = (0, 0, 204)

    def __init__(self, position, walls, pathFindingAlgorithm='random', colorNum = 0):
        self.position = position
        self.pathFind = PathFind(walls)

        self.colors = [
            self.GREEN,
            self.RED,
            self.YELLOW,
            self.BLUE
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
            # self.position = self.pathFind.random(playerPos, self.position)
            pass
        elif self.pathFindingAlgorithm == self.pathFindingAlgorithms[1]:
            # self.position = self.pathFind.breadthFirstSearch(playerPos, self.position)
            pass
        elif self.pathFindingAlgorithm == self.pathFindingAlgorithms[2]:
            # self.position = self.pathFind.dfsRandom(playerPos, self.position)
            pass
        elif self.pathFindingAlgorithm == self.pathFindingAlgorithms[3]:
            self.position = self.pathFind.dfs_heuristic(playerPos, self.position)
