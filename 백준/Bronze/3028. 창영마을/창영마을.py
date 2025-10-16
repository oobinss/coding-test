moves = input().strip()

cups = [True, False, False]

for move in moves:
    if move == 'A':
        cups[0], cups[1] = cups[1], cups[0]
    elif move == 'B':
        cups[1], cups[2] = cups[2], cups[1]
    elif move == 'C':
        cups[0], cups[2] = cups[2], cups[0]

print(cups.index(True) + 1)
