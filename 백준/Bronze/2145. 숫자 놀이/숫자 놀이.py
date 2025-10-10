def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

while True:
    num = input()
    if num == "0":
        break
    print(digital_root(int(num)))

