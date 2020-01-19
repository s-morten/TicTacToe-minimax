


board = [[0] * 3 for n in range(3)]

def check_won(board):
    won = False
    for x in range(3):
        local_value_row = board[x][0]
        local_value_col = board[0][x]
        if (local_value_row != 0 and local_value_row == board[x][1]):
            if (local_value_row == board[x][2]):
                won = True
                return won
        if (local_value_col != 0 and local_value_col == board[1][x]):
            if (local_value_col == board[2][x]):
                won = True
                return won

    if (board[0][0] != 0 and board[0][0] == board[1][1]):
        if(board[0][0] == board[2][2]):
            won = True
            return won
    if (board[0][2] != 0 and board[0][2] == board[1][1]):
        if(board[0][2] == board[2][0]):
            won = True
            return won
    return won

def get_char(i):
    if (i == 0):
        return " "
    if (i == -1):
        return "O"
    if (i == 1):
        return "X"

def draw_board(board):
    for x in range(3):
        print(f"{get_char(board[x][0])}|{get_char(board[x][1])}|{get_char(board[x][2])}")
        print(f"-----")

def ask_for_input(player):
    print("Where to go next? 0,0")
    user_in = input()
    user_in = user_in.split(",")
    x = int(user_in[0])
    y = int(user_in[1])
    board[x][y] = player

player = 0
while(True):
    if (player % 2):
        ask_for_input(-1)
    else:
        ask_for_input(1)
    draw_board(board)
    if(check_won(board)):
        print("Someone Won!!!")

    player = player + 1
