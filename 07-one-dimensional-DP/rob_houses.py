

from one_dimensional.util.stop_watch import start_watch, stop_watch_print


def max_profit(i, S):
    if i == 0:
        return S[0]
    if i < 0:
        return 0
    return max(S[i] + max_profit(i - 2, S), max_profit(i - 1, S))


def max_profit_memo(i, S, cache):
    if i == 0:
        return S[0]
    if i < 0:
        return 0
    if cache[i] != 0:
        return cache[i]
    profit = max(S[i] + max_profit_memo(i - 2, S, cache), max_profit_memo(i - 1, S, cache))
    cache[i] = profit
    return profit


def max_profit_dp(S):
    N = len(S)
    dp = [0 for _ in range(0, N + 1)]
    dp[1] = S[0]
    for i in range(2, N + 1):
        dp[i] = max(S[i - 1] + dp[i - 2], dp[i - 1])
    return dp[N]


def max_profit_dp_reconstruct(S):
    N = len(S)
    dp = [0 for _ in range(0, N + 1)]
    rob = [False for _ in range(0, N)]
    rob[0] = True
    dp[1] = S[0]

    for i in range(2, N + 1):
        if S[i - 1] + dp[i - 2] > dp[i - 1]:
            rob[i - 1] = True
            dp[i] = S[i - 1] + dp[i - 2]
        else:
            dp[i] = dp[i - 1]
            rob[i - 1] = False
    i = N - 1
    while i >= 0:
        if rob[i]:
            print("{} = {}".format(i, S[i]))
            i -= 2
        else:
            i -= 1
    return dp[N]


S = [20, 25, 30, 15, 10, 5, 12, 32, 25, 8, 15, 18]
N = len(S)
start_watch()
res = max_profit(N - 1, S)
print(res)
stop_watch_print("Recursion {} milli seconds")

cache = [0 for _ in range(0, N)]
start_watch()
res = max_profit_memo(N - 1, S, cache)
print(res)
stop_watch_print("Memoization {} milli seconds")

start_watch()
res = max_profit_dp(S)
print(res)
stop_watch_print("DP {} milli seconds")

start_watch()
res = max_profit_dp_reconstruct(S)
print(res)
stop_watch_print("DP {} milli seconds")
