import itertools

N = int(input())
A = list(map(int, input().split()))

max_value = 0

for perm in itertools.permutations(A):
    total = 0
    for i in range(N-1):
        total += abs(perm[i] - perm[i+1])
    max_value = max(max_value, total)

print(max_value)
