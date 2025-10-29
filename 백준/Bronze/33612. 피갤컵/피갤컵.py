n = int(input())

year = 2024
month = 8

months_passed = (n - 1) * 7

month += months_passed

year += (month - 1) // 12
month = (month - 1) % 12 + 1

print(year, month)
