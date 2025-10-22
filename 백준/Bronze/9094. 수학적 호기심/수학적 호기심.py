MAX = 101
answers = [[0] * MAX for _ in range(MAX)]

for n in range(1, MAX):
    for m in range(1, MAX):
        count = 0
        for a in range(1, n):
            for b in range(a + 1, n):
                if (a * a + b * b + m) % (a * b) == 0:
                    count += 1
        answers[n][m] = count

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(answers[n][m])
