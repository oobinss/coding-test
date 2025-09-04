def main():
    N = int(input())
    responses = input().strip()

    count_b = 0
    count_s = 0
    count_a = 0

    for ch in responses:
        if ch == 'B':
            count_b += 1
        elif ch == 'S':
            count_s += 1
        elif ch == 'A':
            count_a += 1

    max_count = max(count_b, count_s, count_a)
    max_fields = []

    if count_b == max_count:
        max_fields.append('B')
    if count_s == max_count:
        max_fields.append('S')
    if count_a == max_count:
        max_fields.append('A')

    if len(max_fields) == 3:
        print("SCU")
    else:
        print("".join(max_fields))

if __name__ == "__main__":
    main()
