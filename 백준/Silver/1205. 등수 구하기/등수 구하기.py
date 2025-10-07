n, score, p = map(int, input().split())

if n == 0:
    print(1)
else:
    scores = list(map(int, input().split()))
    rank = 1

    for s in scores:
        if s > score:
            rank += 1
        else:
            break

    if n == p and score <= scores[-1]:
        print(-1)
    else:
        print(rank)
