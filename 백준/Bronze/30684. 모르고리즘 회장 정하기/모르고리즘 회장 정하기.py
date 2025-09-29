import sys
input = sys.stdin.readline

n = int(input())
names = [input().strip() for _ in range(n)]

result = [ name for name in names if len(name) == 3 ]

print(min(result))