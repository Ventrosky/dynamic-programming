from two_dimensional.util.stop_watch import start_watch, stop_watch_print


def edit_distance(i, j, A, B):
    if i == -1:
        return j + 1
    if j == -1:
        return i + 1
    if A[i] == B[j]:
        return edit_distance(i - 1, j - 1, A, B)
    else:
        return min(edit_distance(i, j - 1, A, B),
                   min(edit_distance(i - 1, j - 1, A, B),
                       edit_distance(i - 1, j, A, B))) + 1


def edit_distance_memo(i, j, A, B, cache):
    if i == -1:
        return j + 1
    if j == -1:
        return i + 1
    if cache[i][j] != -1:
        return cache[i][j]
    if A[i] == B[j]:
        cache[i][j] = edit_distance(i - 1, j - 1, A, B)
        return cache[i][j]
    else:
        cache[i][j] = min(edit_distance_memo(i, j - 1, A, B, cache),
                          min(edit_distance_memo(i - 1, j - 1, A, B, cache),
                              edit_distance_memo(i - 1, j, A, B, cache))) + 1
        return cache[i][j]


def edit_distance_dp(A, B):
    M = len(A)
    N = len(B)
    dp = [[0 for _ in range(0, N + 1)] for _ in range(0, M + 1)]
    for i in range(0, M + 1):
        for j in range(0, N + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1])) + 1
    return dp[M][N]


A = "kitten"
B = "sitting"
M = len(A)
N = len(B)
start_watch()
ret = edit_distance(M-1, N-1, A, B)
stop_watch_print("Recursive {} milli seconds")
print(ret)

cache = [[-1 for _ in range(0, N + 1)] for _ in range(0, M + 1)]
start_watch()
ret = edit_distance_memo(len(A)-1, len(B)-1, A, B, cache)
stop_watch_print("Memoization {} milli seconds")
print(ret)

start_watch()
ret = edit_distance_dp(A, B)
stop_watch_print("DP {} milli seconds")
print(ret)
