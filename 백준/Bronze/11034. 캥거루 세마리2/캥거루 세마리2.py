while True:
    try:
        A, B, C = map(int, input().split())
        answer = max(B - A - 1, C - B - 1)
        print(answer)
    except EOFError:
        break
