import sys

from two_dimensional.util.stop_watch import start_watch, stop_watch_print


def min_path(i, j, G):
    if i == 0 and j == 0:
        return 0
    min_cost = sys.maxsize
    if i > 0:
        min_cost = min_path(i - 1, j, G) + G[i][j]
    if j > 0:
        min_cost = min(min_cost, min_path(i, j - 1, G) + G[i][j])

    return min_cost


def min_path_memo(i, j, G, cache):
    if i == 0 and j == 0:
        return 0
    if cache[i][j] != 0:
        return cache[i][j]

    min_cost = sys.maxsize
    if i > 0:
        min_cost = min_path(i - 1, j, G) + G[i][j]
    if j > 0:
        min_cost = min(min_cost, min_path(i, j - 1, G) + G[i][j])
    cache[i][j] = min_cost
    return min_cost


def min_path_dp(G):
    M = len(G)
    dp = [[0 for _ in range(0, M)] for _ in range(0, M)]
    for i in range(0, M):
        for j in range(0, M):
            if i == 0 and j == 0:
                continue
            dp[i][j] = sys.maxsize
            if i > 0:
                dp[i][j] = dp[i - 1][j] + G[i][j]
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + G[i][j])
    return dp[M - 1][M - 1]


def min_path_dp_reconstruct(G):
    M = len(G)
    dp = [[0 for _ in range(0, M)] for _ in range(0, M)]
    dir = [[0 for _ in range(0, M)] for _ in range(0, M)]
    for i in range(0, M):
        for j in range(0, M):
            if i == 0 and j == 0:
                continue
            dp[i][j] = sys.maxsize
            if i > 0:
                dp[i][j] = dp[i - 1][j] + G[i][j]
            if j > 0 and dp[i][j] > dp[i][j - 1] + G[i][j]:
                dp[i][j] = dp[i][j - 1] + G[i][j]
                dir[i][j] = 1

    i = M - 1
    j = M - 1
    while i > 0 or j > 0:
        print("("+(str(i) + "," + str(j))+")")
        if dir[i][j] == 0:
            print("Up")
            i -= 1
        else:
            print("Left")
            j -= 1
    return dp[M - 1][M - 1]


M = 5
G = [[0, 47, 8, 18, 1],
     [43, 25, 39, 36, 13],
     [22, 8, 13, 38, 46],
     [41, 41, 40, 25, 44],
     [29, 43, 22, 50, 10]]

start_watch()
ret = min_path(M - 1, M - 1, G)
stop_watch_print("Recursive {} milli seconds")
print(ret)

cache = [[0 for _ in range(0, M)] for _ in range(0, M)]
start_watch()
ret = min_path_memo(M - 1, M - 1, G, cache)
stop_watch_print("Memoization {} milli seconds")
print(ret)

start_watch()
ret = min_path_dp(G)
stop_watch_print("DP {} milli seconds")
print(ret)


ret = min_path_dp_reconstruct(G)
print(ret)
