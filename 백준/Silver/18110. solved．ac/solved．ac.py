import sys
input = sys.stdin.readline

n = int(input())
if n == 0:
    print(0)
else:
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    cut = int(n * 0.15 + 0.5)
    trimmed = arr[cut:n-cut] if n - 2*cut > 0 else []
    if not trimmed:
        print(0)
    else:
        avg = sum(trimmed) / len(trimmed)
        print(int(avg + 0.5))
