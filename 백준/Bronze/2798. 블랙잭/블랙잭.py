from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0

for combo in combinations(cards, 3):
    total = sum(combo)
    if total <= M and total > max_sum:
        max_sum = total

print(max_sum)
