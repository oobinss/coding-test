from collections import deque
import sys
input = sys.stdin.readline

def bfs(start_x, start_y, field, visited, M, N):
    moves = [(1,0), (-1,0), (0,1), (0,-1)]
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_y][start_x] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N:
                if not visited[ny][nx] and field[ny][nx] == 1:
                    visited[ny][nx] = True
                    queue.append((nx, ny))

def count_worms(M, N, cabbage_positions):
    field = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]

    for x, y in cabbage_positions:
        field[y][x] = 1

    worm_count = 0
    for y in range(N):
        for x in range(M):
            if field[y][x] == 1 and not visited[y][x]:
                bfs(x, y, field, visited, M, N)
                worm_count += 1

    return worm_count

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    cabbages = [tuple(map(int, input().split())) for __ in range(K)]
    print(count_worms(M, N, cabbages))
