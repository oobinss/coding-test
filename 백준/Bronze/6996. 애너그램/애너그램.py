def are_anagrams(a, b):
    return sorted(a) == sorted(b)

t = int(input())
for _ in range(t):
    a, b = input().split()
    if are_anagrams(a, b):
        print(f"{a} & {b} are anagrams.")
    else:
        print(f"{a} & {b} are NOT anagrams.")