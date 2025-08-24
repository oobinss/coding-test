n = input()

sum = 0
pos = n.index('*')

for i in range(12):
    if i == pos:
        continue
    num = int(n[i])
    
    if i % 2 == 0:
        sum += num
    else:
        sum += num * 3

for i in range(10):
    if ((sum + (i if pos % 2 == 0 else i * 3)) + int(n[12])) % 10 == 0:
        print(i)
        break