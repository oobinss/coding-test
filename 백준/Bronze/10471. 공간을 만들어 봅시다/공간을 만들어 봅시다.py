w, p = map(int, input().split())
partitions = list(map(int, input().split()))

positions = [0] + partitions + [w]
result = set()

for i in range(len(positions)):
    for j in range(i + 1, len(positions)):
        result.add(positions[j] - positions[i])

print(*sorted(result))