keyboard = [
    ['q','w','e','r','t','y','u','i','o','p'],
    ['a','s','d','f','g','h','j','k','l'],
    ['z','x','c','v','b','n','m']
]

key_pos = {}
for i, row in enumerate(keyboard):
    for j, key in enumerate(row):
        key_pos[key] = (i, j)

left_keys = set('qwertasdfgzxcv')
right_keys = set('yuiophjklbnm')

def distance(a, b):
    x1, y1 = key_pos[a]
    x2, y2 = key_pos[b]
    return abs(x1 - x2) + abs(y1 - y2)

time = 0
left_pos, right_pos = input().strip().split()
word = input().strip()

for c in word:
    if c in left_keys:
        time += distance(left_pos, c) + 1
        left_pos = c
    else:
        time += distance(right_pos, c) + 1
        right_pos = c

print(time)
