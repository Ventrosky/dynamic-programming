def print_star(n):
    if n == 0:
        print("")
    else:
        print("*", end=" ")
        print_star(n - 1)


def print_pattern(n, limit, decreasing):
    print_star(n)
    if n == 1:
        print_pattern(n + 1, limit, False)
    elif n < limit or decreasing:
        if decreasing:
            print_pattern(n - 1, limit, True)
        else:
            print_pattern(n + 1, limit, False)

n=5
print_pattern(n, n, True)