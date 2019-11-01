

from two_dimensional.util.stop_watch import start_watch, stop_watch_print


def lcs(i, j, A, B):
    if i == -1 or j == -1:
        return 0
    if A[i] == B[j]:
        return lcs(i - 1, j - 1, A, B) + 1
    else:
        return max(lcs(i - 1, j, A, B), lcs(i, j - 1, A, B))


def lcs_memo(i, j, A, B, cache):
    if i == -1 or j == -1:
        return 0
    if cache[i][j] != -1:
        return cache[i][j]
    if A[i] == B[j]:
        cache[i][j] = lcs_memo(i - 1, j - 1, A, B, cache) + 1
        return cache[i][j]
    else:
        cache[i][j] = max(lcs_memo(i - 1, j, A, B, cache), lcs_memo(i, j - 1, A, B, cache))
        return cache[i][j]


def lcs_dp(A, B):
    M = len(A)
    N = len(B)
    dp = [[0 for _ in range(0, N + 1)] for _ in range(0, M + 1)]
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[M][N]


A = "ACHEFMGLP"
B = "XYCEPQMLG"
M = len(A)
N = len(B)
start_watch()
ret = lcs(M - 1, N - 1, A, B)
stop_watch_print("Recursive {} milli seconds")
print(ret)

cache = [[-1 for _ in range(0, N)] for _ in range(0, M)]
start_watch()
ret = lcs_memo(M - 1, N - 1, A, B, cache)
stop_watch_print("Memoization {} milli seconds")
print(ret)

start_watch()
ret = lcs_dp(A, B)
stop_watch_print("DP {} milli seconds")
print(ret)
