S = input()
result = []
for c in S:
    if 'A' <= c <= 'Z':
        result.append(chr((ord(c) - ord('A') + 13) % 26 + ord('A')))
    elif 'a' <= c <= 'z':
        result.append(chr((ord(c) - ord('a') + 13) % 26 + ord('a')))
    else:
        result.append(c)
print(''.join(result))
