def max_fun(N, memo={}):
    if N == 1:
        return 0
    if N in memo:
        return memo[N]

    max_value = 0
    for i in range(1, N):
        left = i
        right = N - i
        value = left * right + max_fun(left, memo) + max_fun(right, memo)
        max_value = max(max_value, value)

    memo[N] = max_value
    return max_value

N = int(input())
print(max_fun(N))
