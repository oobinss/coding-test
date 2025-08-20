from collections import deque
import sys
input = sys.stdin.readline

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for nxt in graph[start]:
        if not visited[nxt]:
            dfs(graph, nxt, visited)

def bfs(graph, start):
    visited = [False] * (len(graph))
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for nxt in graph[v]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

visited = [False] * (N+1)
dfs(graph, V, visited)
print()
bfs(graph, V)