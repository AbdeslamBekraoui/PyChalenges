# ----------------------------------------
# ------------ Tic Tac Toe ---------------
# ----------------------------------------
"""
This code is a simple implementation of the well known 
Tic Tac Toe game, that every programmer had to make at point!
"""
# Inporant vairables

board = ["-","-","-",
         "-","-","-",
         "-","-","-",]
GAME_RUNNING = True
current_player = "X"
winner = None

# Game board

def game_board(board) :
    """
    print the game board!
    """

    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("-" * 9)
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("-" * 9)
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Player Input

def player_input(board) :
    """
    takes player input & checks if it's valid or not.
    if valid it changes the board[player-1] to an X or an O.
    """

    player = int(input("Chose a number form 1 => 9 :".strip()))
    if player >= 1 and player <= 9 and board[player-1] == "-" :
        board[player-1] = current_player
        return board
    else :
        print("Invalid input!")

# switch players

def players() :
    """
    switches the players!
    """
    global current_player
    if current_player == "X" :
        current_player = "O"
    else :
        current_player = "X"
# Check for win or lose

def check_result(board) :

    global winner

    # Check win

    # - horizontal

    if board[0] == board[1] == board[2] == current_player :
        print(f"Congrats {current_player}, you won")
        winner = current_player

    if board[3] == board[4] == board[5] == current_player :
        print(f"Congrats {current_player}, you won")
        winner = current_player

    if board[6] == board[7] == board[8] == current_player :
        print(f"Congrats {current_player}, you won")
        winner = current_player

    # - vertical

    if board[0] == board[3] == board[6] == current_player :
        print(f"Congrats {current_player}, you won")
        winner = current_player

    if board[1] == board[4] == board[7] == current_player :
        print(f"Congrats {current_player}, you won")
        winner = current_player

    if board[2] == board[5] == board[8] == current_player :
        print(f"Congrats {current_player}, you won")
        winner = current_player

    # - diagonal

    if board[0] == board[4] == board[8] == current_player :
        print(f"Congrats {current_player}, you won")
        winner = current_player

    elif board[2] == board[4] == board[6] == current_player :
        print(f"Congrats {current_player}, you won")
        winner = current_player

    # check tie

    if "-" not in board :
        print("It's a tie!")

# put the hall thing together

while GAME_RUNNING :

    if "-" not in board or winner :
        game_board(board)
        GAME_RUNNING = False
    else :
        game_board(board)
        a = player_input(board)
        check_result(board)
        if a :
            players()
        else :
            continue
