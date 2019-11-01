from one_dimensional.util.stop_watch import start_watch, stop_watch_print


def count_ways(i, S, D):
    if i == -1:
        return 1
    count = 0
    for j in range(i, -1, -1):
        if S[j:i + 1] in D:
            count += count_ways(j - 1, S, D)
    return count


def count_ways_memo(i, S, D, cache):
    if i == -1:
        return 1
    if cache[i] != -1:
        return cache[i]
    count = 0
    for j in range(i, -1, -1):
        if S[j:i + 1] in D:
            count += count_ways_memo(j - 1, S, D,cache)
    cache[i] = count
    return count


def count_ways_dp(i, S, D):
    N = len(S)
    dp = [0 for _ in range(0, N + 1)]
    dp[0] = 1
    for i in range(1, N + 1):
        for j in range(i, 0, -1):
            if S[j-1:i] in D:
                dp[i] += dp[j-1]
    return dp[N]


# S = "pineapplepenapple"
# D = {"apple", "pen", "applepen", "pine", "pineapple"}

S="aaaaaaaaaaaaaaaaaaaaaaa"
D={"a","aaa","aa","aaaa"}
N = len(S)

start_watch()
ret = count_ways(N - 1, S, D)
stop_watch_print("Recursive {} milli seconds")
print(ret)

cache = [-1 for _ in range(0, N)]
start_watch()
ret = count_ways_memo(N - 1, S, D, cache)
stop_watch_print("Memoization {} milli seconds")
print(ret)


start_watch()
ret = count_ways_dp(N - 1, S, D)
stop_watch_print("DP {} milli seconds")
print(ret)
