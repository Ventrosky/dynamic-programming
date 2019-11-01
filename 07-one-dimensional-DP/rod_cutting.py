import sys

from one_dimensional.util.stop_watch import start_watch, stop_watch_print


def max_profit(l, p):
    if l == 0:
        return 0
    max_p = -sys.maxsize
    for i in range(0, l):
        max_p = max(max_p, p[i] + max_profit(l - i - 1, p))
    return max_p


def max_profit_memo(l, p, cache):
    if l == 0:
        return 0
    if cache[l] != -1:
        return cache[l]
    max_p = -sys.maxsize
    for i in range(0, l):
        max_p = max(max_p, p[i] + max_profit(l - i - 1, p))
    cache[l] = max_p
    return max_p


def max_profit_dp(L, p):
    dp = [0 for _ in range(0, L + 1)]
    for l in range(1, L + 1):
        dp[l] = -sys.maxsize
        for i in range(0, l):
            dp[l] = max(dp[l], p[i] + dp[l - i - 1])
    return dp[L]


def max_profit_dp_reconstruct(L, p):
    dp = [0 for _ in range(0, L + 1)]
    cuts = [i for i in range(0, L+1)]
    for l in range(1, L + 1):
        dp[l] = -sys.maxsize
        for i in range(0, l):
            if p[i] + dp[l - i - 1] > dp[l]:
                dp[l] = p[i] + dp[l - i - 1]
                cuts[l] = i+1

    l = L
    cut = cuts[L]
    while cut != 0:
        print(str(cut)+',',end='')
        l = l-cut
        cut = cuts[l]
    return dp[L]


profits_table = [1, 5, 8, 9, 10, 13, 17, 20, 24, 30]

l = 8
start_watch()
res = max_profit(l, profits_table)
print(res)
stop_watch_print("Recursion {} milli seconds")

cache = [-1 for _ in range(0, l + 1)]
start_watch()
res = max_profit_memo(l, profits_table, cache)
print(res)
stop_watch_print("Memoization {} milli seconds")

start_watch()
res = max_profit_dp(l, profits_table)
print(res)
stop_watch_print("Bottom up {} milli seconds")

res = max_profit_dp_reconstruct(l,profits_table)
print(res)
