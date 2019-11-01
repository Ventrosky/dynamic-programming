from two_dimensional.util.stop_watch import start_watch, stop_watch_print


def matches(i, j, S, R):
    if (i == -1 and j == -1) or R[0:j + 1] == "*":
        return True
    if i == -1 or j == -1:
        return False
    if S[i] == R[j]:
        return matches(i - 1, j - 1, S, R)
    elif R[j] == '.':
        return matches(i - 1, j - 1, S, R)
    elif R[j] == '*':
        return matches(i - 1, j, S, R) or matches(i, j - 1, S, R)
    return False


def matches_memo(i, j, S, R, cache):
    if (i == -1 and j == -1) or R[0:j + 1] == "*":
        return True
    if i == -1 or j == -1:
        return False
    if cache[i][j] is not None:
        return cache[i][j]
    if S[i] == R[j]:
        cache[i][j] = matches_memo(i - 1, j - 1, S, R, cache)
        return cache[i][j]
    elif R[j] == '.':
        cache[i][j] = matches_memo(i - 1, j - 1, S, R, cache)
        return cache[i][j]
    elif R[j] == '*':
        cache[i][j] = matches_memo(i - 1, j, S, R, cache) or \
                      matches_memo(i, j - 1, S, R, cache)
        return cache[i][j]
    return False


def matches_dp(S, R):
    M = len(S)
    N = len(R)
    dp = [[False for _ in range(N + 1)] for _ in range(0, M + 1)]
    dp[0][0] = True
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if S[i - 1] == R[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif R[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif R[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    return dp[M][N]


# S = "ABBBAC"
# R = ".*A*"
S = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
R = ".*AAAAAAA***A"
M = len(S)
N = len(R)
start_watch()
ret = matches(M-1, N-1, S, R)
stop_watch_print("Recursive {} milli seconds")
print(ret)

cache = [[None for _ in range(0, N + 1)] for _ in range(0, M + 1)]
start_watch()
ret = matches_memo(M-1, N-1, S, R, cache)
stop_watch_print("Memoization {} milli seconds")
print(ret)

start_watch()
ret = matches_dp(S, R)
stop_watch_print("DP {} milli seconds")
print(ret)
