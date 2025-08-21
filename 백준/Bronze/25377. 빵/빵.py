n = int(input())
time = 999
for _ in range(n):
    a,b = map(int, input().split())
    if a <= b:
        if b < time:
            time = b
           
if time == 999:
    time = -1
print(time)            