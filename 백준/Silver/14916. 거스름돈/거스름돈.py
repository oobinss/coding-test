n = int(input())

result = -1
for five in range(n // 5, -1, -1):
    rest = n - five * 5
    if rest % 2 == 0:
        result = five + rest // 2
        break

print(result)
