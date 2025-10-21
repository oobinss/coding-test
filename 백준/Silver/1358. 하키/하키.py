import sys
input = sys.stdin.readline

W, H, X, Y, P = map(int, input().split())
R = H / 2
count = 0

for _ in range(P):
    px, py = map(int, input().split())

    if X <= px <= X + W and Y <= py <= Y + H:
        count += 1
    elif (px - X)**2 + (py - (Y + R))**2 <= R**2:
        count += 1
    elif (px - (X + W))**2 + (py - (Y + R))**2 <= R**2:
        count += 1

print(count)
