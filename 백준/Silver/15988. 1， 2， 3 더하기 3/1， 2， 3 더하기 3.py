import sys

MOD = 1000000009

def solve():
    input = sys.stdin.readline

    T = int(input().strip())
    nums = [int(input().strip()) for _ in range(T)]
    max_n = max(nums)

    dp = [0] * (max_n + 1)
    dp[0] = 1
    if max_n >= 1:
        dp[1] = 1
    if max_n >= 2:
        dp[2] = 2
    for i in range(3, max_n + 1):
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MOD

    print("\n".join(str(dp[n]) for n in nums))

if __name__ == "__main__":
    solve()
