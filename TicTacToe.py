"""TicTacToe"""
def check(point, board):
    """winpattern"""
    win = False
    zip_board = list(zip(board[0], board[1], board[2]))
    for i in range(3):
        if board[i] == [point, point, point]:
            win = True
        elif zip_board[i] == (point, point, point):
            win = True
    if [board[0][0], board[1][1], board[2][2]] == [point, point, point]:
        win = True
    elif [board[0][2], board[1][1], board[2][0]] == [point, point, point]:
        win = True
    return win
def main():
    """Demo"""
    board = [list(input()) for _ in range(3)]
    if check("X", board):
        print("X WIN")
    elif check("O", board):
        print("O WIN")
    else:
        print("DRAW")
main()
