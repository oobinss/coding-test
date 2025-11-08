n = int(input())
nums = [float(input()) for _ in range(n)]

max_product = nums[0]
current_product = nums[0]

for i in range(1, n):
    current_product = max(nums[i], current_product * nums[i])
    max_product = max(max_product, current_product)

print(f"{max_product:.3f}")
