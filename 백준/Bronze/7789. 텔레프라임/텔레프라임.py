phone , digit = input().split()
original = int(phone)
new_number = int(digit + phone)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if is_prime(original) and is_prime(new_number):
    print("Yes")
else:
    print("No")