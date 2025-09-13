n = int(input())
s = 1
sum = 0
while True:
    sum += s
    if sum > n:
        break
    else:
        s += 1
print(s - 1)
