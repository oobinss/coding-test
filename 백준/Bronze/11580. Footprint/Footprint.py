def count_footprints(commands):
    x, y = 0, 0
    visited = set()
    visited.add((x, y))

    direction = {
        'E': (1, 0),
        'W': (-1, 0),
        'S': (0, -1),
        'N': (0, 1)
    }

    for cmd in commands:
        dx, dy = direction[cmd]
        x += dx
        y += dy
        visited.add((x, y))

    return len(visited)

L = int(input())
commands = input().strip()
print(count_footprints(commands))
