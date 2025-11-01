def is_reverse_defeat(w_scores, s_scores):
    w_total = 0
    s_total = 0
    reversed = False

    for i in range(9):
        w_total += w_scores[i]
        if w_total > s_total:
            reversed = True
        s_total += s_scores[i]

    return "Yes" if reversed else "No"

w_scores = list(map(int, input().split()))
s_scores = list(map(int, input().split()))

print(is_reverse_defeat(w_scores, s_scores))