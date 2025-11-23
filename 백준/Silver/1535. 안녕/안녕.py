N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

dp = [0] * 100

for i in range(N):
    loss, joy = L[i], J[i]
    for h in range(99, loss - 1, -1):
        dp[h] = max(dp[h], dp[h - loss] + joy)

print(max(dp))
