n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

if arr[1]-arr[0] == arr[2]-arr[1]:
    print(arr[-1] + (arr[1]-arr[0]))
else:
    print(int(arr[-1] * (arr[1]/arr[0])))
    