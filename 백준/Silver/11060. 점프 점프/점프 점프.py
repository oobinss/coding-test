from collections import deque

N = int(input().strip())
A = list(map(int, input().split()))

visited = [False] * N
queue = deque([(0, 0)])
visited[0] = True

while queue:
    pos, jumps = queue.popleft()

    if pos == N - 1:
        print(jumps)
        break

    for step in range(1, A[pos] + 1):
        next_pos = pos + step
        if next_pos < N and not visited[next_pos]:
            visited[next_pos] = True
            queue.append((next_pos, jumps + 1))
else:
    print(-1)
