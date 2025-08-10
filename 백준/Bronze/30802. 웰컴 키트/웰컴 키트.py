n = int(input())
arr = list(map(int, input().split()))
t, p = map(int, input().split())

t_cnt = 0
for count in arr:
    if count % t == 0:
        t_cnt += count // t
    else:
        t_cnt += count // t + 1
        
pen_bundle = n // p
pen_single = n % p

print(t_cnt)
print(pen_bundle, pen_single)
