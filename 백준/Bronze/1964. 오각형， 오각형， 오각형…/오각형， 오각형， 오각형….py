n = int(input())
start = 5
add = 7

for i in range(1,n):
    start += add
    add += 3

print(start%45678)
    