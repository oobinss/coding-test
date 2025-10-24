A, a, B, b, P = map(int, input().split())

def solve(A, a, B, b, P):
    if A > P or B > P:
        return "No"
    if A + B <= P:
        return "Yes"
    if a >= B:
        return "Yes"
    if b >= A:
        return "Yes"
    return "No"

print(solve(A, a, B, b, P))
