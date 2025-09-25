import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(x, y, n, graph, visited):
    dx = [-1, 0, 0, 1]
    dy = [0, 1, -1, 0]
    count = 1
    visited[x][y] = True
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0<= ny < n:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                count += dfs(nx, ny, n, graph, visited)
    return count
    
n = int(input())
graph = [list(map(int,input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

complexes = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            complexes.append(dfs(i, j, n, graph, visited))
            
print(len(complexes))
for count in sorted(complexes):
    print(count)
