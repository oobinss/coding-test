while 1:
    B = list(map(int, input().split()))
    if B == [0]:
        break
    
    for i in range(B[0]//4):
        A = [2*i+1, 2*i+2, B[0]-2*i-1, B[0]-2*i]
        if B[1] in A:
            A.remove(B[1])
            print(*A)