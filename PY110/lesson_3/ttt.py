# Display the initial empty 3x3 board.
# Ask the user to mark a square.
# Computer marks a square.
# Display the updated board state.
# If it's a winning board, display the winner.
# If the board is full, display tie.
# If neither player won and the board is not full, go to #2
# Play again?
# If yes, go to #1
# Goodbye!

import random
import os

WINNER = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],
    [1, 4, 7], [2, 5, 8], [3, 6, 9],
    [1, 5, 9], [3, 5 ,7]
]

EMPTY_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER= 'O'
WINNING_MATCH_CRITERION = 3


def display_board(board):
    os.system('clear')
    print('')
    print('     |     |')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}')
    print('     |     |')
    print('')

def initialize_board():
    return {i: ' '  for i in range(1, 10)}

board = {
    1: ' ',
    2: ' ',
    3: ' ',
    4: ' ',
    5: ' ',
    6: ' ',
    7: ' ',
    8: ' ',
    9: ' ',
}

def prompt(message):
    print(f"==>{message}")

def player_choose_square(board):
    while True:
        prompt(f"please select your square ({join_or(available_square(board))}): ")
        player_choice = input().strip()
        if player_choice in available_square(board):
            break
        prompt("Sorry, it's not a valid input.")
    board[int(player_choice)] = HUMAN_MARKER

def computer_choose_square(board):
    if full_board(board):
        return 
    if find_winning_square(board):
        board[find_winning_square(board)] = COMPUTER_MARKER
    elif find_risky_square(board):
        board[find_risky_square(board)] = COMPUTER_MARKER
    elif board[5] == EMPTY_MARKER:
        board[5] = COMPUTER_MARKER
    else:
        board[int(random.choice(available_square(board)))] = COMPUTER_MARKER

def available_square(board):
    return [str(k) for k, v in board.items() if v == EMPTY_MARKER]

def full_board(board):
    return len(available_square(board)) == 0

def decide_winner(board):
    player_selection = [k for k, v in board.items() if v == HUMAN_MARKER]
    computer_selection = [k for k, v in board.items() if v == COMPUTER_MARKER]
    for winner_option in WINNER: 
        if all(num in player_selection for num in winner_option):
            return "player"
        if all(num in computer_selection for num in winner_option):
            return "computer"
    return

def find_risky_square(board):
    player_selection = [k for k, v in board.items() if v == HUMAN_MARKER]
    computer_selection = [k for k, v in board.items() if v == COMPUTER_MARKER]
    empty_selection = [k for k, v in board.items() if v == EMPTY_MARKER]
    for winner_option in WINNER: 
        if (len(set(winner_option) & set(player_selection)) == 2 and 
                len(set(winner_option) & set(empty_selection)) == 1):
            return list(set(winner_option) & set(empty_selection))[0]
    return

def find_winning_square(board):
    player_selection = [k for k, v in board.items() if v == HUMAN_MARKER]
    computer_selection = [k for k, v in board.items() if v == COMPUTER_MARKER]
    empty_selection = [k for k, v in board.items() if v == EMPTY_MARKER]
    for winner_option in WINNER: 
        if (len(set(winner_option) & set(computer_selection)) == 2 and 
                len(set(winner_option) & set(empty_selection)) == 1):
            return list(set(winner_option) & set(empty_selection))[0]
    return

def someone_won(board):
    return bool(decide_winner(board))

def join_or(lst, delimiter=', ', word='or'):
    if len(lst) == 0:
        return ''
    elif len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        return f"lst[0] {word} lst[1]"
    return delimiter.join(lst[:-1]) + f", {word} {lst[-1]}"

def display_score(player_score, computer_score):
    prompt(f"current score:")
    prompt(f"player: {player_score}")
    prompt(f"computer: {computer_score}")

def check_match_winner(player_score, computer_score):
    if player_score == WINNING_MATCH_CRITERION:
        prompt("***player wins the match!***")
        return True
    elif computer_score == WINNING_MATCH_CRITERION:
        prompt("***computer wins the match!***")
        return True
    return False    

def play_again():
    prompt("do you want to play again? y/n")
    cotinue_signal = input().strip()
    if cotinue_signal.casefold().startswith('n'):
        prompt("Bye!")
        return False
    prompt("Let's continue!")
    return True

def who_plays_first():
    prompt("who do you want to play first (player or computer)?: ")
    answer = input()
    return answer.casefold().strip()

def choose_square(board, current_player):
    if current_player == 'player':
        player_choose_square(board)
    else:
        computer_choose_square(board)

def alternate_player(current_player):
    if current_player == 'player':
        return 'computer'
    else:
        return 'player'



def ttt():
    player_score = 0
    computer_score = 0
    prompt("Welcome to Tic-Tac-Toe Game!")
    while True:
        board = initialize_board()
        current_player = who_plays_first()
        while True:
            display_board(board)
            choose_square(board, current_player)
            current_player = alternate_player(current_player)
            if full_board(board) or someone_won(board):
                break
        display_board(board)
        if someone_won(board):
            prompt(f"{decide_winner(board)} won!")
            if decide_winner(board) == 'player':
                player_score += 1
            else:
                computer_score += 1
            display_score(player_score, computer_score)
        else:
            prompt("it's a tie")
            display_score(player_score, computer_score)
        if check_match_winner(player_score, computer_score):
            if not play_again():
                break
            player_score = 0
            computer_score = 0
        elif not play_again():
            break


ttt()


