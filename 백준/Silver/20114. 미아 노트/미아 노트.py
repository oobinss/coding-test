N, H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

result = []

for i in range(N):
    found = '?'
    for row in range(H):
        for col in range(i * W, (i + 1) * W):
            if grid[row][col] != '?':
                found = grid[row][col]
                break
        if found != '?':
            break
    result.append(found)

print(''.join(result))