# .......Author: macunox
# .......Python Version: 3.10.2
# .......Date: 5 June 2022

# --------------Import Block

from random import randrange

# --------------Function Block


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    # Board construct
    for i in board:
        for x in i:
            print(f"{x}\t", end="")
        print("\n")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.

    board_status = make_list_of_free_fields(board)

    print(f"[!] Player move...")

    free_fields = True
    while free_fields is True:
        user_input = int(input("[!] Please make move: "))
        # check if userinput is an Integer
        if isinstance(user_input, int):
            # check if userinput is between 1 and 9
            if 0 < user_input < 10:
                row = 0
                for i in board_status:
                    column = 0
                    for x in i:
                        # check if in for loop if userinput is equal Fieldnumber
                        if x == user_input:
                            board[row][column] = "O"
                            print(f"[!] User play'{user_input}'")
                            free_fields = False
                        column += 1
                    row += 1
            else:
                print("[!] input not in range 1-9")
        else:
            print("[!] input not int")

        if free_fields is True:
            print(f"[!] Please select a free field")


    return board


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

    # list for free Fields
    free_squares = []
    # check if "O" or "X" in Board
    for i in board:
        for x in i:
            # Fieldnumber added to list if no entry "O" or "X"
            if x == "O":
                pass
            elif x == "X":
                pass
            else:
                free_squares.append(x)
    return board


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game

    cross_right = False
    cross_left = False
    horizontal_up = False
    horizontal_middle = False
    horizontal_down = False
    vertical_left = False
    vertical_middle = False
    vertical_right = False

    # winning combination
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        cross_right = True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        cross_left = True
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        horizontal_up = True
    if board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        horizontal_middle = True
    if board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        horizontal_down = True
    if board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        vertical_left = True
    if board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        vertical_middle = True
    if board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        vertical_right = True

    # check winning combination
    if cross_right is True or \
            cross_left is True or \
            horizontal_up is True or \
            horizontal_middle is True or \
            horizontal_down is True or \
            vertical_left is True or \
            vertical_middle is True or \
            vertical_right is True:
        print(f"[!] Player {sign} has won!!")
        return True


def draw_move(board):
    # The function draws the computer's move and updates the board.

    print(f"[!] Computer move...")
    if board[1][1] == "X":
        free_fields = True
        while free_fields is True:
            # Random number
            random_number = randrange(0, 10)
            # get free Field list
            board_status = make_list_of_free_fields(board)
            row = 0
            for i in board_status:
                column = 0
                for x in i:
                    if random_number == x:
                        board[row][column] = "X"
                        print(f"[!] Computer play '{x}'")
                        free_fields = False
                    column += 1
                row += 1
    else:
        board[1][1] = "X"
        print(f"[!] Computer play '5'")

    return board


# --------------Field Constructor Block

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# --------------Variables Block

result_X = False
result_O = False


# --------------ACTION BLOCK
print(f"*******************************************************************************")
print("""
 #######                #######                     #######               
    #    #  ####           #      ##    ####           #     ####  ###### 
    #    # #    #          #     #  #  #    #          #    #    # #      
    #    # #      #####    #    #    # #      #####    #    #    # #####  
    #    # #               #    ###### #               #    #    # #      
    #    # #    #          #    #    # #    #          #    #    # #      
    #    #  ####           #    #    #  ####           #     ####  ######
""")
print(f"*******************************************************************************")
print(f"Board:")
print(f"[1]\t[2]\t[3]\n[4]\t[5]\t[6]\n[7]\t[8]\t[9]")
print("")

# Start Game
start_game_status = True
while start_game_status:
    start_game = input("Please press enter to start Game:")
    if start_game != "":
        start_game_status = True
    else:
        start_game_status = False

# Main Loop
while True:
    # computers move
    board = draw_move(board)
    display_board(board)
    result_X = victory_for(board, "X")

    # check winner
    if result_X is True or result_O is True:
        break

    # users move
    board = enter_move(board)
    display_board(board)
    result_O = victory_for(board, "O")

    # check winner
    if result_X is True or result_O is True:
        break
