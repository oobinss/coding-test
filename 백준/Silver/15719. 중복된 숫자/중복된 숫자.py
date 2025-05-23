import sys

n = int(input())
sum_total = 0
numbers = sys.stdin.read()
temp = ""

for num in numbers:
    if num.isdigit():
        temp += num
    elif num == " ":
        sum_total += int(temp)
        temp = ""

sum_total += int(temp)

expected = (n - 1) * n // 2
print(sum_total - expected)