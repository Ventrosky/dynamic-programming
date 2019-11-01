

from one_dimensional.util.stop_watch import start_watch, stop_watch_print


def lis(i, A):
    if i == 0:
        return 1
    max_l = 1
    for j in range(0, i):
        l = lis(j, A)
        if A[j] < A[i]:
            l += 1
        max_l = max(max_l, l)
    return max_l


def lis_memo(i, A, cache):
    if i == 0:
        return 1
    if cache[i] != 0:
        return cache[i]
    max_l = 1
    for j in range(0, i):
        l = lis(j, A)
        if A[j] < A[i]:
            l += 1
        max_l = max(max_l, l)
    cache[i] = max_l
    return max_l


def lis_dp(A):
    N = len(A)
    dp = [1 for _ in range(0, N)]
    for i in range(0, N):
        for j in range(0, i):
            l = dp[j]
            if A[j] < A[i]:
                l += 1
            dp[i] = max(dp[i], l)
    return dp[N - 1]


A = [5, 2, 4, 7, 3, 8]
N = len(A)
start_watch()
res = lis(N - 1, A)
print(res)
stop_watch_print("Recursion {} milli seconds")

cache = [0 for _ in range(0, N)]
start_watch()
res = lis_memo(N - 1, A, cache)
print(res)
stop_watch_print("Memoization {} milli seconds")

start_watch()
res = lis_dp(A)
print(res)
stop_watch_print("DP {} milli seconds")
