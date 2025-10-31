A, B, C = input().split()
A = int(A)
B = int(B)

if int(C[-1]) % 2 == 1:
    print(A ^ B)
else:
    print(A)