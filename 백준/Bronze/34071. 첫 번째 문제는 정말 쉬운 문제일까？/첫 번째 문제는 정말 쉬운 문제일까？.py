N = int(input().strip())
X = [int(input().strip()) for _ in range(N)]

first = X[0]
if first == min(X):
    print("ez")
elif first == max(X):
    print("hard")
else:
    print("?")
