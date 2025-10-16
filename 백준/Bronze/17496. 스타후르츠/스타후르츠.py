def calculate_profit(N, T, C, P):
    harvest_count = 0
    day = 1
    while day + T <= N:
        harvest_count += 1
        day += T
    return harvest_count * C * P

N, T, C, P = map(int, input().split())
print(calculate_profit(N, T, C, P))
