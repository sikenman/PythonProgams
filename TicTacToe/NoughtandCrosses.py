import random
random.seed()

X_SIGN = "X"
O_SIGN = "O"

board = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9']
]

def welcome():
    boardClean = [
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9']
    ]
    print('Welcome to the "Tic-tac-toe" game.')
    print("The board layout is shown below:")
    print("")
    draw_board(boardClean)
    print("When prompted, enter the number corresponding to the square you want.")
    print("")

def initialise_board(board):
    for row in range(0, 3):
        for col in range(0, 3):
            board[row][col] = " "
    return board

def draw_board(board):
    for row in range(0, 3):
        output = "-------------\n| "
        for col in range(0, 3):
            output = output + board[row][col] + " | "
        print(output)
    print("-------------")
    print()

def get_player_move(board):
    while True:
        try:
            cell = int(input("Choose your square [1 to 9]: "))
            if (cell >= 1) and (cell <= 9):
                row = (cell // 3)
                col = (cell % 3) - 1
                if (cell % 3) == 0:
                    row = row - 1
                if board[row][col] == " ":
                    break
            else:
                print("Please enter a valid number.")
        except:
            print("Please enter a valid number.")
    board[row][col] = X_SIGN
    return row, col

def choose_computer_move(board):
    spaces = []
    for row in range(0, 3):
        for col in range(0, 3):
            if board[row][col] == " ":
                spaces.append((row, col))
    try:
        row, col = random.choice(spaces)
    except IndexError:
        board[row][col] = X_SIGN
    board[row][col] = O_SIGN

    square = (row*3)+(col+1)
    print("The computer has chosen square", square)
    print()
    return row, col

def check_for_win(board, mark):
    if board[0][0] == mark and board[0][1] == mark and board[0][2] == mark:
        return True
    if board[1][0] == mark and board[1][1] == mark and board[1][2] == mark:
        return True
    if board[2][0] == mark and board[2][1] == mark and board[2][2] == mark:
        return True
    if board[0][0] == mark and board[1][0] == mark and board[2][0] == mark:
        return True
    if board[0][1] == mark and board[1][1] == mark and board[2][1] == mark:
        return True
    if board[0][2] == mark and board[1][2] == mark and board[2][2] == mark:
        return True
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
    if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return True
    else:
        return False

def check_for_draw(board):
    for row in range(0, 3):
        for col in range(0, 3):
            if board[row][col] == " ":
                return False
    return True

def play_game(board):
    welcome()
    initialise_board(board)
    draw_board(board)
    mark = X_SIGN
    while check_for_win(board, mark) == False and check_for_draw(board) == False:

        get_player_move(board)
        draw_board(board)
        mark = X_SIGN
        check_for_win(board, mark)

        if check_for_win(board, mark) == True:
            draw_board(board)
            print("Player WINS")
            print("End of game!")
            print()
            return 1
        elif check_for_win(board, mark) == False:
            check_for_draw(board)
            if check_for_draw(board) == True:
                draw_board(board)
                print("*** DRAW ***")
                print("End of game!")
                print()
                return 0

        choose_computer_move(board)
        draw_board(board)
        mark = O_SIGN
        check_for_win(board, mark)
        if check_for_win(board, mark) == True:
            draw_board(board)
            print("Computer WINS")
            print(" End of game!")
            print()
            return -1
        elif check_for_win(board, mark) == False:
            check_for_draw(board)
            if check_for_draw(board) == True:
                draw_board(board)
                print("*** DRAW ***")
                print("End of game!")
                print()
                return 0
