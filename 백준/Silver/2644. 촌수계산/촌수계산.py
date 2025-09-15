from collections import deque
import sys
input = sys.stdin.readline

def bfs(n, a, b, relations):
    graph = [[] for _ in range(n + 1)]

    for x, y in relations:
        graph[x].append(y)
        graph[y].append(x)

    visited = [False] * (n + 1)
    distance = [-1] * (n + 1)

    queue = deque([a])
    visited[a] = True
    distance[a] = 0

    while queue:
        current = queue.popleft()
        if current == b:
            return distance[current]

        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)

    return -1


if __name__ == "__main__":
    n = int(input())
    a, b = map(int, input().split())
    m = int(input())
    relations = [list(map(int, input().split())) for _ in range(m)]

    result = bfs(n, a, b, relations)
    print(result)
