def max_lucky_ticket_length(s):
    n = len(s)
    max_len = 0

    for length in range(2, n + 1, 2):
        for start in range(n - length + 1):
            mid = start + length // 2
            left = s[start:mid]
            right = s[mid:start + length]
            if sum(map(int, left)) == sum(map(int, right)):
                max_len = max(max_len, length)

    return max_len

s = input().strip()
print(max_lucky_ticket_length(s))
