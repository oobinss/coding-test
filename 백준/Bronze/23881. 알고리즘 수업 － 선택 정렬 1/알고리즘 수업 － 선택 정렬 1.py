n, k = map(int, input().split())
a = list(map(int, input().split()))
count = 0

for last in range(n-1, 0, -1):
    max_idx = 0
    for i in range(1, last+1):
        if a[i] > a[max_idx]:
            max_idx = i

    if max_idx != last:
        a[max_idx], a[last] = a[last], a[max_idx]
        count += 1
        if count == k:
            sorted_pair = sorted([a[max_idx], a[last]])
            print(sorted_pair[0], sorted_pair[1])
            break
else:
    print(-1)
