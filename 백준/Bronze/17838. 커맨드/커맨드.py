def is_favorite_command(s: str) -> int:
    if len(s) != 7:
        return 0
    
    if len(set(s)) != 2:
        return 0

    if s[0] == s[1] and s[2] == s[3] and s[4] == s[0] and s[5] == s[6] and s[0] != s[2]:
        return 1
    return 0


T = int(input().strip())
for _ in range(T):
    s = input().strip()
    print(is_favorite_command(s))
