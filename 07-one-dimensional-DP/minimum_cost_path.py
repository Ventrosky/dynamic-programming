import sys


from one_dimensional.util.stop_watch import start_watch, stop_watch_print


def min_cost_path(i, C, X):
    if i == 0:
        return 0
    min_cost = sys.maxsize
    for j in range(1, min(X, i) + 1):
        min_cost = min(min_cost, C[i] + min_cost_path(i - j, C, X))
    return min_cost


def min_cost_path_memo(i, C, X, cache):
    if i == 0:
        return 0
    if cache[i] != 0:
        return cache[i]
    min_cost = sys.maxsize
    for j in range(1, min(X, i) + 1):
        min_cost = min(min_cost, C[i] + min_cost_path(i - j, C, X))
    cache[i] = min_cost
    return min_cost


def min_cost_dp(C, X):
    N = len(C)
    dp = [sys.maxsize for _ in range(0, N)]
    dp[0] = 0
    for i in range(0, N):
        for j in range(1, min(X, i) + 1):
            dp[i] = min(dp[i], dp[i - j] + C[i])
    return dp[N - 1]


def min_cost_dp_reconstruct(C, X):
    N = len(C)
    dp = [sys.maxsize for _ in range(0, N)]
    jump = [0 for _ in range(0, N)]
    dp[0] = 0
    for i in range(0, N):
        for j in range(1, min(X, i) + 1):
            if dp[i - j] + C[i] < dp[i]:
                dp[i] = dp[i - j] + C[i]
                jump[i] = i - j
    i = N - 1
    print(str(i) + " -> ", end='')
    while i > 0:
        i = jump[i]
        print(str(i) + " -> ", end='')
    return dp[N - 1]


C = [0, 20, 30, 40, 25, 15, 20, 28]
X = 3
N = len(C)

start_watch()
ret = min_cost_path(N - 1, C, X)
stop_watch_print("Recursive {} milli seconds")
print(ret)

cache = [0 for _ in range(0, N)]
start_watch()
ret = min_cost_path_memo(N - 1, C, X, cache)
stop_watch_print("Memoization {} milli seconds")
print(ret)

start_watch()
ret = min_cost_dp(C, X)
stop_watch_print("DP {} milli seconds")
print(ret)

min_cost_dp_reconstruct(C, X)
