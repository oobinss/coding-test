n, b, h, w = map(int, input().split())

price = float('inf')

for _ in range(h):
    hotel_price = int(input())
    week = list(map(int, input().split()))
    for j in week:
        if j >= n:
            total = hotel_price * n
            if total <= b:
                price = min(price, total)
            break
            
if price == float('inf'):
    print("stay home")
else:
    print(price)

