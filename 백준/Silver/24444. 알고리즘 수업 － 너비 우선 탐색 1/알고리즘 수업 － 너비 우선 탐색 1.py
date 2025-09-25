from collections import deque
import sys
input = sys.stdin.readline

def bfs(n, graph, start):
    visited = [0] * (n + 1)
    order = 1
    queue = deque([start])
    visited[start] = order
    
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if visited[v] == 0:
                order += 1
                visited[v] = order
                queue.append(v)
    return visited
    
n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

for adj in graph:
    adj.sort()
        
visited = bfs(n, graph, r)

for i in range(1, n+1):
    print(visited[i])
