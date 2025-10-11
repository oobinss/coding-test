n = int(input())
num_set = set(map(int,input().split()))
sorted_nums = sorted(num_set)

print(*sorted_nums)