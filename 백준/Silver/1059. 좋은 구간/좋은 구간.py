l = int(input())
s = list(map(int, input().split()))
n = int(input())

s.append(0)
s.append(1001)
s.sort()

if n in s:
    print(0)
else:
    for i in range(len(s) - 1):
        if s[i] < n < s[i + 1]:
            left = s[i]
            right = s[i + 1]
            break

    count = 0
    for a in range(left + 1, right):
        for b in range(a + 1, right):
            if a <= n <= b:
                count += 1

    print(count)
