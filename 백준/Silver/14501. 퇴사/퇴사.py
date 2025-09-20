N = int(input())
schedules = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (N + 2)

for i in range(N, 0, -1):
    Ti, Pi = schedules[i - 1]
    if i + Ti > N + 1:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], Pi + dp[i + Ti])

print(dp[1])