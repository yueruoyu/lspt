
import random

VALID_CHOICE = ['r', 'p', 's', 'l', 'k']
INPUT_MES = "Please input your choice rpslk(rock/paper/scissors/lizard/spock): "
ERROR_MES = "Invalid choice, please input again"

WINNDER_DICT = {
    'r': ['s', 'l'],
    'p': ['k', 'r'],
    's': ['l', 'p'],
    'l': ['p', 'k'],
    'k': ['r', 's'],
}

def prompt(message):
    print(f'===> {message}')

def player_wins(player1, player2):
    return player2 in WINNDER_DICT[player1]

def computer_wins(player1, player2):
    return player1 in WINNDER_DICT[player2]

player_score = 0
computer_score = 0

while True:
    prompt(INPUT_MES)
    player_choice = input()
    while player_choice not in VALID_CHOICE:
        prompt(ERROR_MES)
        player_choice = input()

    computer_choice = random.choice(VALID_CHOICE)

    prompt(f"Player's choice is {player_choice},\
    Computer's choice is {computer_choice}")

    if player_wins(player_choice, computer_choice):
        player_score += 1
        prompt("player wins")
    elif computer_wins(player_choice, computer_choice):
        computer_score += 1
        prompt("computer wins")
    else:
        prompt("it's a tie")
    
    if player_score == 3:
        prompt("Game over. Player won!")
        break
    elif computer_score == 3:
        prompt("Game over. Computer won!")
        break





