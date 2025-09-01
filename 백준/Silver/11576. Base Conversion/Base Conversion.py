A, B = map(int, input().split())

m = int(input())
A_number = list(map(int, input().split()))
A_number.reverse()

result = []
number = 0
for i in range(m):
    number += A_number[i] * (A ** i)
    
while number//B:
    result.append(number%B)
    number = number//B
result.append(number)
    
result.reverse()
print(' '.join(map(str,result)))