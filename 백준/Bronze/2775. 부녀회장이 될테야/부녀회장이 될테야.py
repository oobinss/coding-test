T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())

    residents = [i for i in range(1, n+1)]

    for floor in range(1, k+1):
        for room in range(1, n):
            residents[room] += residents[room-1]

    print(residents[-1])
