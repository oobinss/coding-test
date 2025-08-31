n = int(input())
for _ in range(n):
    expr = input()

    result = None
    for ch in expr:
        if ch in '01':
            result = int(ch)
            break

    a = 0
    for ch in expr:
        if ch == '!':
            a += 1
        elif ch in '01':
            break

    b = len(expr) - a - 1

    if b > 0:
        result = 1

    for _ in range(a):
        result = 1 if result == 0 else 0

    print(result)
