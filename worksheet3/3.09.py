# 9. Move robot
def move_robot(x, y, direction):
    if direction == "up":
        return (x, y+1)
    elif direction == "down":
        return (x, y-1)
    elif direction == "left":
        return (x-1, y)
    elif direction == "right":
        return (x+1, y)
    else:
        return (x, y)
