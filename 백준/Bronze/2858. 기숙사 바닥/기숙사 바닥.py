R, B = map(int, input().split())

total = R + B

for L in range(3, total + 1):
    if total % L != 0:
        continue
    W = total // L
    if W < 3:
        continue
    border = 2 * L + 2 * W - 4
    inner = (L - 2) * (W - 2)
    if border == R and inner == B:
        print(max(L, W), min(L, W))
        break
