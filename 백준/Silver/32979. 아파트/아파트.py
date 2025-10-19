from collections import deque

N = int(input())
T = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

q = deque(a)

for bj in b:
    for _ in range((bj - 1) % len(q)):
        q.append(q.popleft())
    loser = q[0]
    print(loser, end=' ')
