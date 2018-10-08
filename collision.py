class Collision:
    def __init__(self):
        print("Collision class initialized.")
        self.score = 0
        self.points = None
        self.superPoints = None
        self.playerPos = None

    def update(self, points, player_pos, super_points):
        self.points = points
        self.superPoints = super_points
        self.playerPos = player_pos

        for i, (j, k) in enumerate(points):
            if (player_pos[0], player_pos[1]) == (j, k):
                del self.points[i]
                self.score += 1

        for i, (j, k) in enumerate(super_points):
            if (player_pos[0], player_pos[1]) == (j, k):
                del self.superPoints[i]
                self.score += 10

    def check_ghost_collision(self, player_pos, ghosts):
        for ghost in ghosts:
            if ghost.position == player_pos:
                self.score -= 100
                ghosts.remove(ghost)
        return ghosts
