T = int(input())

for _ in range(T):
    expr = input().split()
    a = int(expr[0])
    op = expr[1]
    b = int(expr[2])
    result = int(expr[4])

    if op == '+':
        correct = a + b
    elif op == '-':
        correct = a - b
    elif op == '*':
        correct = a * b
    elif op == '/':
        correct = a // b

    if correct == result:
        print("correct")
    else:
        print("wrong answer")
