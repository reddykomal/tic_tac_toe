#board
#display board
#handle turn
#swap
#check who is the winner

#global variables:
current_player="x"
gameisgoing=True
winner=None

board=["-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,]

def display_board():
    print(board[0] + " | " + board[1] + " | "+ board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def handle_turn():
    global current_player
    print(current_player +"'s turn:")
    position=int(input("Enter the position between 1to 9:"))

    #while position not in ["1","2","3","4","5","6","7","8","9"]:
     #   position=int(input("Invalid input choose a position between 1- 9:"))

    position = position - 1
    if position <= 8:
        board[position]=current_player
       # display_board()
    if position > 8:
        position=int(input("Enter the position between 1 to 9 only:"))

        board[position]=current_player


def swap_player():
    global current_player

    if current_player=="x":
        current_player="o"
    elif current_player=="o":
        current_player="x"

def check_who_winnes():
    global winner

    rowwinner=check_row()
    colwinner=check_col()
    digwinner=check_dig()
    check_tie()


    if rowwinner:
        winner=rowwinner
    elif colwinner:
        winner=colwinner
    else:
        winner=digwinner


def check_row():
    global gameisgoing
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        gameisgoing=False


    if row1:
        return board[0]
    elif row2:
        return board[4]
    elif row3:
        return board[7]


def check_col():
    global gameisgoing
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"

    if col1 or col2 or col3:
        gameisgoing = False

    if col1:
        return board[0]
    elif col2:
        return board[4]
    elif col3:
        return board[7]


def check_dig():
    global gameisgoing
    dig1 = board[0] == board[4] == board[8] != "-"
    dig2 = board[2] == board[4] == board[6] != "-"


    if dig1 or dig2 :
        gameisgoing = False

    if dig1:
        return board[0]
    elif dig2:
        return board[4]


def check_tie():
    global gameisgoing
    if "-" not in board:
        gameisgoing=False
        print("Match is draw :)")


def play_game():
    while gameisgoing:
        display_board()
        handle_turn()
        swap_player()
        check_who_winnes()


        if winner=="x":
            print("X is the  winner")
        elif winner=="o":
            print("O is the winner")


play_game()