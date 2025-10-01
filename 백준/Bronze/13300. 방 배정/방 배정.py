import math

n, k = map(int, input().split())

students = [[0]*7 for _ in range(2)]

for _ in range(n):
    s, y = map(int, input().split())
    students[s][y] += 1
        
room_count = 0
for gender in range(2):
    for grade in range(1, 7):
        count = students[gender][grade]
        room_count += math.ceil(count / k)

print(room_count)