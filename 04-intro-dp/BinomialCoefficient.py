from introduction.util.stop_watch import start_watch, stop_watch_print


def binomial_coefficient(n, k):
    if n == k or k == 0: return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)


def binomial_coefficient_mem(n, k):
    mem = [[0 for i in range(0, k + 1)] for i in range(0, n + 1)]
    return binomial_coefficient_memoization(n, k, mem)


def binomial_coefficient_memoization(n, k, mem):
    if n == k or k == 0: return 1
    if mem[n][k] != 0: return mem[n][k]
    res = binomial_coefficient_memoization(n - 1, k - 1, mem) + binomial_coefficient_memoization(n - 1, k, mem)
    mem[n][k] = res
    return res


def binomial_coefficient_dp(n, k):
    dp = [[0 for i in range(0, k + 1)] for i in range(0, n + 1)]
    for i in range(0, n + 1):
        dp[i][0] = 1
        if i <= k:
            dp[i][i] = 1
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    return dp[n][k]

N=6
K=4

start_watch()
print(binomial_coefficient(N,K))
stop_watch_print("Recursive solution {} milli seconds")


start_watch()
print(binomial_coefficient_mem(N,K))
stop_watch_print("Memoization solution {} milli seconds")


start_watch()
print(binomial_coefficient_dp(N,K))
stop_watch_print("Bottom up solution {} milli seconds")
