N = int(input())

dp = [False] * (N+1)

if N >= 1: dp[1] = False
if N >= 2: dp[2] = True
if N >= 3: dp[3] = False
if N >= 4: dp[4] = True

for i in range(5, N+1):
    if not dp[i-1] or not dp[i-3] or not dp[i-4]:
        dp[i] = True
    else:
        dp[i] = False

print("SK" if dp[N] else "CY")
