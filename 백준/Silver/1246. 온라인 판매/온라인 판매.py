n, m = map(int, input().split())
price = [int(input()) for _ in range(m)]

price.sort()
max_profit = 0
best_price = 0

for i in range(m):
    sell_price = price[i]
    egg_num = min(n, m-i)
    profit = sell_price * egg_num
    
    if profit > max_profit:
        max_profit = profit
        best_price = sell_price

print(best_price, max_profit)