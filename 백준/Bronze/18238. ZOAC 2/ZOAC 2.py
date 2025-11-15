s = input().strip()

def dist(a, b):
    da = ord(a) - ord('A')
    db = ord(b) - ord('A')
    d = abs(da - db)
    return min(d, 26 - d)

cur = 'A'
ans = 0
for ch in s:
    ans += dist(cur, ch)
    cur = ch

print(ans)