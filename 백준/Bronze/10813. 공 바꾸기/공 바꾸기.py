n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    i -= 1
    j -= 1

    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

print(*arr)
