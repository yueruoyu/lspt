
import random

VALID_CHOICE = ['rock', 'paper', 'scissors']
INPUT_MES = "Please input your choice (rock/paper/scissors): "
ERROR_MES = "Invalid choice, please input again"

def prompt(message):
    print(f'===> {message}')

def return_winner(player1, player2):
    if ((player1 == 'rock' and player2 == 'scissors') or
       (player1 == 'scissors' and player2 == 'paper') or
       (player1 == 'paper' and player2 == 'rock')):
       return 'player'
    elif ((player2 == 'rock' and player1 == 'scissors') or
       (player2 == 'scissors' and player1 == 'paper') or
       (player2 == 'paper' and player1 == 'rock')):
       return 'computer'
    else:
        return None

while True:
    prompt(INPUT_MES)
    player_choice = input()
    while player_choice not in VALID_CHOICE:
        prompt(ERROR_MES)
        player_choice = input()

    computer_choice = random.choice(VALID_CHOICE)

    prompt(f"Player's choice is {player_choice},\
    Computer's choice is {computer_choice}")

    if return_winner(player_choice, computer_choice):
        prompt(f"it's {return_winner(player_choice, computer_choice)} that wins")
    else:
        prompt("it a tie!")
    prompt("Do you want to play again? y/n")
    repeat_answer = input().lower()
    while True:
        if repeat_answer.startswith('n') or repeat_answer.startswith('y'): 
            break
        else:
            prompt("invalid input")
            repeat_answer = input()
    if repeat_answer.startswith('n'):
        break




