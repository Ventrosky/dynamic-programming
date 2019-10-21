from optimization.util.stop_watch import start_watch, stop_watch_print

RED = 0
BLUE = 1
GREEN = 2


def min_cost(costs, i, color):
    if i == len(costs):
        return 0
    if color == RED:
        cost_blue = min_cost(costs, i + 1, BLUE)
        cost_green = min_cost(costs, i + 1, GREEN)
        return costs[i][RED] + min(cost_blue, cost_green)
    elif color == BLUE:
        cost_red = min_cost(costs, i + 1, RED)
        cost_green = min_cost(costs, i + 1, GREEN)
        return costs[i][BLUE] + min(cost_red, cost_green)
    elif color == GREEN:
        cost_red = min_cost(costs, i + 1, RED)
        cost_blue = min_cost(costs, i + 1, BLUE)
        return costs[i][GREEN] + min(cost_red, cost_blue)


def min_cost_memo(costs, i, color, cache):
    if i == len(costs):
        return 0
    if cache[i][color] != -1:
        return cache[i][color]
    if color == RED:
        cost_blue = min_cost_memo(costs, i + 1, BLUE, cache)
        cost_green = min_cost_memo(costs, i + 1, GREEN, cache)
        cache[i][RED] = costs[i][RED] + min(cost_blue, cost_green)
        return cache[i][RED]
    elif color == BLUE:
        cost_red = min_cost_memo(costs, i + 1, RED, cache)
        cost_green = min_cost_memo(costs, i + 1, GREEN, cache)
        cache[i][BLUE] = costs[i][BLUE] + min(cost_red, cost_green)
        return cache[i][BLUE]
    elif color == GREEN:
        cost_red = min_cost_memo(costs, i + 1, RED, cache)
        cost_blue = min_cost_memo(costs, i + 1, BLUE, cache)
        cache[i][GREEN] = costs[i][GREEN] + min(cost_red, cost_blue)
        return cache[i][GREEN]


def min_cost_dp(costs):
    n = len(costs)
    dp = [[0 for _ in range(0, 3)] for _ in range(0, n + 1)]
    for i in range(1, n + 1):
        dp[i][RED] = costs[i - 1][RED] + min(dp[i - 1][BLUE], dp[i - 1][GREEN])
        dp[i][BLUE] = costs[i - 1][BLUE] + min(dp[i - 1][RED], dp[i - 1][GREEN])
        dp[i][GREEN] = costs[i - 1][GREEN] + min(dp[i - 1][RED], dp[i - 1][BLUE])
    return min(dp[n][RED], min(dp[n][BLUE], dp[n][GREEN]))


def min_cost_dp_reconstruct(costs):
    n = len(costs)
    dp = [[0 for _ in range(0, 3)] for _ in range(0, n + 1)]
    decision = [[0 for _ in range(0, 3)] for _ in range(0, n + 1)]
    for i in range(1, n + 1):
        if dp[i - 1][BLUE] < dp[i - 1][GREEN]:
            decision[i][RED] = BLUE
            dp[i][RED] = costs[i - 1][RED] + dp[i - 1][BLUE]
        else:
            decision[i][RED] = GREEN
            dp[i][RED] = costs[i - 1][RED] + dp[i - 1][GREEN]

        if dp[i - 1][RED] < dp[i - 1][GREEN]:
            decision[i][BLUE] = RED
            dp[i][BLUE] = costs[i - 1][BLUE] + dp[i - 1][RED]
        else:
            decision[i][BLUE] = GREEN
            dp[i][BLUE] = costs[i - 1][BLUE] + dp[i - 1][GREEN]

        if dp[i - 1][RED] < dp[i - 1][BLUE]:
            decision[i][GREEN] = RED
            dp[i][GREEN] = costs[i - 1][GREEN] + dp[i - 1][RED]
        else:
            decision[i][GREEN] = BLUE
            dp[i][GREEN] = costs[i - 1][GREEN] + dp[i - 1][BLUE]

    result = min(dp[n][RED], min(dp[n][BLUE], dp[n][GREEN]))
    i = n
    if result == dp[n][RED]:
        c = RED
    elif result == dp[n][BLUE]:
        c = BLUE
    else:
        c = GREEN

    while i > 0:
        print("House {} is painted with color {} ".format(i, color(c)))
        c = decision[i][c]
        i -= 1
    return result


def color(c):
    if c == RED:
        return "RED"
    elif c == BLUE:
        return "BLUE"
    else:
        return "GREEN"


painting_cost = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
start_watch()
paint_red = min_cost(painting_cost, 0, RED)
paint_blue = min_cost(painting_cost, 0, BLUE)
paint_green = min_cost(painting_cost, 0, GREEN)
min_cost = min(paint_red, min(paint_blue, paint_green))
print(min_cost)
stop_watch_print("Recursive solution {} millis")

cache = [[-1 for _ in range(0, 3)] for _ in range(0, len(painting_cost))]
start_watch()
paint_red = min_cost_memo(painting_cost, 0, RED, cache)
paint_red = min_cost_memo(painting_cost, 0, BLUE, cache)
paint_red = min_cost_memo(painting_cost, 0, GREEN, cache)
min_cost = min(paint_red, min(paint_blue, paint_green))
print(min_cost)
stop_watch_print("Memoization solution {} millis")

start_watch()
print(min_cost_dp(painting_cost))
stop_watch_print("Bottom up solution {} millis")
