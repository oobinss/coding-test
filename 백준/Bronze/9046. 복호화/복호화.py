import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    line = input().strip()
    freq = [0] * 26
    
    for ch in line:
        if ch != ' ':
            freq[ord(ch) - ord('a')] += 1
    
    max_freq = max(freq)
    candidates = [i for i, f in enumerate(freq) if f == max_freq]
    
    if len(candidates) == 1:
        print(chr(candidates[0] + ord('a')))
    else:
        print('?')
