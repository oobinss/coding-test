n = int(input())
ans = float('inf') 

for _ in range(n):
    a, b = map(int, input().split())
    if a <= b:
        ans = min(ans, b)

print(ans if ans != float('inf') else -1)
