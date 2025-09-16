def transform(A, B):
    count = 1
    while B != A:
        if B < A:
            return -1
        if B % 2 == 0:
            B //= 2
        elif str(B).endswith('1'):
            B = int(str(B)[:-1])
        else:
            return -1
        count += 1
    return count

if __name__ == "__main__":
    A, B = map(int, input().split())
    print(transform(A, B))
