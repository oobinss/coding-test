import math

R, C, N = map(int, input().split())

result = math.ceil(R / N) * math.ceil(C / N)
print(result)