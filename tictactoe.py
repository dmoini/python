import random
import os

inputs = ["#", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
players = ["X", "O"]


def display_board(board, inputs):
    print()
    print(f" {inputs[7]} | {inputs[8]} | {inputs[9]}        {board[7]} | {board[8]} | {board[9]} ")
    print("- - - - - -      - - - - - -")
    print(f" {inputs[4]} | {inputs[5]} | {inputs[6]}        {board[4]} | {board[5]} | {board[6]} ")
    print("- - - - - -      - - - - - -")
    print(f" {inputs[1]} | {inputs[2]} | {inputs[3]}        {board[1]} | {board[2]} | {board[3]} ")
    print()


def clear_screen():
    os.system('clear')


def player_input():
    letter = ""
    while not (letter == "X" or letter == "O"):
        letter = input("Player 1: Do you want to be X or O? ").upper()
    if letter == "X":
        return ("X", "O")
    else:
        return ("O", "X")


def place_marker(inputs, board, marker, position):
    board[position] = marker
    inputs[position] = " "


def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or (board[3] == board[6] == board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or (board[3] == board[5] == board[7] == mark))


def random_start():
    return random.randint(0, 1)


# Checks to see if space is available
def open_space_check(board, position):
    return board[position] == " "


# Checks to see if board is full
def full_board_check(board):
    return " " not in board


def player_choice(board, player):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not open_space_check(board, position):
        position = int(input(f"Player {player} choose a position (1-9): "))
    return position


def replay():
    return input("Do you want to play again? Y/N: ").upper().startswith("Y")


# TIC TAC TOE
def play_tic_tac_toe(board, inputs, players):
    while True:
        clear_screen()
        print('Welcome to Tic Tac Toe!')
        xo = random_start()
        player = players[xo]
        print(f"Player {player} will go first.")
        in_progress = True
        while in_progress:
            display_board(board, inputs)
            position = player_choice(board, player)
            place_marker(inputs, board, player, position)
            if win_check(board, player):
                display_board(board, inputs)
                print(f"Congratulations Player {player}. YOU WON!!!")
                in_progress = False
            else:
                if full_board_check(board):
                    display_board(board, inputs)
                    print("It's a DRAW...")
                    break
                else:
                    xo += 1
                    player = players[xo % 2]
                    clear_screen()
        board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        inputs = ["#", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if not replay():
            break


play_tic_tac_toe(board, inputs, players)
