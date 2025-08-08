import math

n = int(input())
dp = [0] * (n + 1)

for i in range(1, n + 1):
    min_count = float('inf')
    j = 1
    while j * j <= i:
        min_count = min(min_count, dp[i - j * j] + 1)
        j += 1
    dp[i] = min_count

print(dp[n])