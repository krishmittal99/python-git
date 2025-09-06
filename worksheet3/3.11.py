# 11. Goal reached
def is_goal_reached(path):
    x, y = 0, 0
    for move in path:
        if move == "up":
            y += 1
        elif move == "down":
            y -= 1
        elif move == "left":
            x -= 1
        elif move == "right":
            x += 1
    return (x, y) == (2, 0)
