n, m, k = map(int, input().split())

result = min(m,k) + min(n-m, n-k)
print(result)