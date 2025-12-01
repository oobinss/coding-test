from collections import deque

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

visited = [[False] * N for _ in range(M)]

directions = [(-1,0),(1,0),(0,-1),(0,1),
              (-1,-1),(-1,1),(1,-1),(1,1)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < M and 0 <= ny < N:
                if not visited[nx][ny] and board[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

count = 0
for i in range(M):
    for j in range(N):
        if board[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            count += 1

print(count)
