N = int(input().strip())
s = input().strip()

result = []
for ch in s:
    result.append(ch)
    if len(result) >= 3 and "".join(result[-3:]) in ("PS4", "PS5"):
        result.pop()

print("".join(result))