h, m = map(int, input().split())
if m >= 45:
    new_h = h
    new_m = m - 45
else:
    new_h = h - 1 if h > 0 else 23
    new_m = m + 15
print(new_h, new_m)