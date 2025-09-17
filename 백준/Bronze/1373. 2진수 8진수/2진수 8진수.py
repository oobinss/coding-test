binary_str = input().strip()

num = int(binary_str, 2)

oct_str = oct(num)[2:]
print(oct_str)