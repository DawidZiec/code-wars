# i: 3x3 board, 0 means empty, 1 means X, 2 means O
# o: -1 means game not finished, 1 means X won, 2 means O won, 0 means draw


def is_won_by_x(board):
    # condition for horizontal X win
    if board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1:
        return 1
    elif board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1:
        return 1
    elif board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1:
        return 1
    # condition for vertical X win
    elif board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1:
        return 1
    elif board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1:
        return 1
    elif board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1:
        return 1
    # condition for diagonal X win
    elif board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
        return 1
    elif board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1:
        return 1


def is_won_by_o(board):
    # condition for horizontal X win
    if board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 2:
        return 2
    elif board[1][0] == 2 and board[1][1] == 2 and board[1][2] == 2:
        return 2
    elif board[2][0] == 2 and board[2][1] == 2 and board[2][2] == 2:
        return 2
    # condition for vertical X win
    elif board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2:
        return 2
    elif board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2:
        return 2
    elif board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 2:
        return 2
    # condition for diagonal X win
    elif board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
        return 2
    elif board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2:
        return 2


def is_drawn(board):
    sum = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                sum += 1
    if sum == 0:
        return 5


def is_solved(board):

    # Firstly we check if the game is won either by X or O
    if is_won_by_x(board) == 1:
        return 1
    if is_won_by_o(board) == 2:
        return 2

    # If the game was not won, we check, if it was drawn
    if is_drawn(board) == 5:
        return 0

    return -1
