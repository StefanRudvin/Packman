class Collision:
    def __init__(self):
        print("Collision class initialized.")
        self.score = 0
        self.points = None
        self.superPoints = None
        self.playerPos = None

    def update(self, points, player, super_points):
        player_pos = player.position
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
                player.super_mode_counter = 100
                self.score += 10

    def check_ghost_collision(self, player, ghosts):
        for ghost in ghosts:
            if ghost.position == player.position:
                if player.super_mode_counter > 0:
                    self.score += 100
                else:
                    self.score -= 100
                    player.lives -= 1
                ghosts.remove(ghost)
        return ghosts
