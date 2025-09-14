from collections import deque
import sys
input = sys.stdin.readline

def bfs(start_x, start_y, w, h, graph, visited):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    
    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i, j, w, h, graph, visited)
                count += 1
                
    print(count)
