from itertools import combinations

a, b, c = map(int, input().split())
drinks = [a, b, c]
max_odd = -1
max_even = -1

for r in range(1, 4):
    for combo in combinations(drinks, r):
        product = 1
        for num in combo:
            product *= num
        if product % 2 == 0:
            max_even = max(product, max_even)
        else:
            max_odd  = max(product, max_odd)
        
print(max_odd if max_odd != -1 else max_even)
    
        
