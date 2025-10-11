def count_plates(format_str):
    total = 1
    prev = ''
    for ch in format_str:
        if ch == 'c':
            if prev == 'c':
                total *= 25
            else:
                total *= 26
        elif ch == 'd':
            if prev == 'd':
                total *= 9
            else:
                total *= 10
        prev = ch
    return total

format_str = input().strip()
print(count_plates(format_str))
