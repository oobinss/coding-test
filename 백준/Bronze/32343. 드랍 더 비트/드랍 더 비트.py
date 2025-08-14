N = int(input().strip())
a, b = map(int, input().split())

diff_count = min(a, N - b) + min(b, N - a)

max_xor = (1 << N) - (1 << (N - diff_count)) if diff_count > 0 else 0

print(max_xor)