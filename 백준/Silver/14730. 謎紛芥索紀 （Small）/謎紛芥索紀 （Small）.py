N = int(input())
result = 0

for _ in range(N):
    C, K = map(int, input().split())
    if K != 0:
        result += C * K

print(result)