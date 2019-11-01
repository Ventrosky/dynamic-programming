

from two_dimensional.util.stop_watch import start_watch, stop_watch_print


def min_deletions(i, j, S):
    if i >= j:
        return 0
    if S[i] == S[j]:
        return min_deletions(i + 1, j - 1, S)
    else:
        return min(min_deletions(i + 1, j, S), min_deletions(i, j - 1, S)) + 1


def min_deletions_memo(i, j, S, cache):
    if i >= j:
        return 0
    if cache[i][j] != -1:
        return cache[i][j]
    if S[i] == S[j]:
        cache[i][j] = min_deletions_memo(i + 1, j - 1, S, cache)
        return cache[i][j]
    else:
        cache[i][j] = min(min_deletions_memo(i + 1, j, S, cache), min_deletions_memo(i, j - 1, S, cache)) + 1
        return cache[i][j]


def min_deletions_dp(S):
    N = len(S)
    dp = [[0 for _ in range(0,N)] for _ in range(0,N)]
    for l in range(1,N+1):
        for i in range(0,N-l+1):
            j = i+l-1
            if i == j:
                continue
            if S[i] == S[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = min(dp[i+1][j],dp[i][j-1])+1
    return dp[0][N-1]


S = "KAAKAZ"
N = len(S)
start_watch()
ret = min_deletions(0, N - 1, S)
stop_watch_print("Recursive {} milli seconds")
print(ret)


cache = [[-1 for _ in range(0,N)] for i in range(0,N)]
start_watch()
ret = min_deletions_memo(0, N - 1, S,cache)
stop_watch_print("Memoization {} milli seconds")
print(ret)

start_watch()
ret = min_deletions_dp(S)
stop_watch_print("DP {} milli seconds")
print(ret)
