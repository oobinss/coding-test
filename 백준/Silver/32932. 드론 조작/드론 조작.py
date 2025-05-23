n, k = map(int, input().split())
obstacles = set()

for _ in range(n):
    x, y = map(int, input().split())
    obstacles.add((x,y))
    
commands = input().strip()

x, y= 0,0

for cmd in commands:
    dx, dy = 0, 0
    if cmd == 'U':
        dy = 1
    elif cmd == 'D':
        dy = -1
    elif cmd == 'R':
        dx = 1
    elif cmd == 'L':
        dx = -1
        
    new_x = x + dx
    new_y = y + dy
    
    if (new_x, new_y) not in obstacles:
        x, y = new_x, new_y

print(x,y)
    