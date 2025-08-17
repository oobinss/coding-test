t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    
    result = 1
    while True:
        if data[0] < max(data):
            data.append(data.pop(0))
            if m == 0:
                m = len(data) - 1
            else:
                m -= 1
        else:
            if m == 0:
                print(result)
                break
            else:
                data.pop(0)
                result += 1
                m -= 1
