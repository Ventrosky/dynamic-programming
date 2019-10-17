def nqueens(n):
    board = [0 for i in range(0, n)]
    if not helper(board, 0):
        print("No solution")


def helper(board, i):
    n = len(board)
    if i == n:
        for c in board:
            for r in range(0, n):
                if r == c:
                    print("O", end=" ")
                else:
                    print("X", end=" ")
            print("")

        return True

    for c in range(0, n):
        flag = False
        for rc in range(0, i):
            if c == board[rc] or abs(board[rc] - c) == i - rc:
                flag = True
                break
        if flag:
            continue

        board[i] = c
        if helper(board, i + 1):
            return True

    return False

nqueens(8)