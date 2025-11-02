import sys
from collections import Counter

N = int(sys.stdin.readline())
schedule = list(map(int, sys.stdin.readline().split()))
    
count = Counter(schedule)
max_count = max(count.values())
    
if max_count > (N + 1) // 2:
    print("NO")
else:
    print("YES")

