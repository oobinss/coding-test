n, m = map(int, input().split())
time = list(map(int, input().split()))

result = sum(time) - n

if m > result:
    print("OUT")
else:
    print("DIMI")
