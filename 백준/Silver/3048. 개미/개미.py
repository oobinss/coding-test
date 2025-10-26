N1, N2 = map(int, input().split())
group1 = input().strip()
group2 = input().strip()
T = int(input())

ants = [(ch, 'R') for ch in reversed(group1)] + [(ch, 'L') for ch in group2]

for _ in range(T):
    i = 0
    while i < len(ants) - 1:
        if ants[i][1] == 'R' and ants[i+1][1] == 'L':
            ants[i], ants[i+1] = ants[i+1], ants[i]
            i += 2
        else:
            i += 1

print(''.join(ch for ch, _ in ants))
