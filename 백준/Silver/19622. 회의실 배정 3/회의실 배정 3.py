import sys
import bisect

def solve():
    input = sys.stdin.readline
    N_line = input().strip()
    while N_line == '':
        N_line = input().strip()
    N = int(N_line)

    meetings = []
    for _ in range(N):
        line = input().strip()
        while line == '':
            line = input().strip()
        s, e, p = map(int, line.split())
        meetings.append((s, e, p))

    meetings.sort(key=lambda x: x[1])

    ends = [m[1] for m in meetings]

    dp = [0] * (N + 1)

    for i in range(1, N + 1):
        s, e, p = meetings[i - 1]
        j = bisect.bisect_right(ends, s)
        dp[i] = max(dp[i - 1], dp[j] + p)

    print(dp[N])

if __name__ == "__main__":
    solve()
