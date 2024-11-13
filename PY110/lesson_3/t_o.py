import random

SUITS = ['♠', '♥', '♣', '♦']
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']


def shuffle(deck):
    random.shuffle(deck)

def total(participant_cards):
    total_cards = [card[1] for card in participant_cards]
    total_value = 0
    for string in total_cards:
        if string in '2345678910':
            total_value += int(string)
        elif string in 'JackQueenKing':
            total_value += 10
        else:
            total_value += 11
    ace_counts = total_cards.count('Ace')
    while total_value > 21 and ace_counts:
        total_value -= 10
        ace_counts -= 1
    return total_value

def deal_a_card(player, cards):
    player.append(cards.pop())

def inital_deal_cards(player1, player2, cards):
    for _ in range(2):
        player1.append(cards.pop())
        player2.append(cards.pop())

def prompt(message):
    print(f"==>{message}")

def busted(player):
    return total(player) > 21

def display_card(player):
    all_cards =[card[0] + card[1] for card in player]
    return ", ".join(all_cards)

def dealer_play(current_cards, cards):
    score = total(current_cards)
    while score < 17:
        prompt("Dealer hits!")
        deal_a_card(current_cards, cards)
        score = total(current_cards)
        prompt(f"Dealer now has cards: {display_card(current_cards)}")
    if score <= 21:
        prompt(f"Dealer stays at {score}")
        return score
    return False

def play_again():
    print("-----------")
    answer = input("do you want to play again? (y/n)").casefold().strip()
    if answer.startswith('n'):
        return False
    return True

def display_player_result(player, score):
    prompt(f"Player has {display_card(player)}, "
           f"for a total of: {score}")


def display_result(player1, player2, score1, score2):
    print("=================")
    prompt(f"Player has {display_card(player1)}, total of {score1}")
    prompt(f"Dealer has {display_card(player2)}, total of {score2}")
    print("=================")

def game():
    prompt("Welcome to the Twenty-One Game!")
    while True:
        deck = [[suit, value] for suit in SUITS for value in VALUES]
        shuffle(deck)
        player_cards = []
        dealer_cards = []
        inital_deal_cards(player_cards, dealer_cards, deck)
        player_score = total(player_cards)
        display_player_result(player_cards, player_score)
        prompt(f"Dealer has {display_card(dealer_cards[1:])}")

        while True:
            while True:
                answer = input("==>player: (h)it or (s)tay? ")
                if answer in ['h', 's']:
                    break
                prompt("Sorry, you need to input 'h' or 's'")
            if answer == 's':
                break
            deal_a_card(player_cards, deck)
            player_score = total(player_cards)
            display_player_result(player_cards, player_score)
            if player_score > 21:
                print("*****Player Busted! Dealer wins!*****")
                break
        if player_score > 21:
            if play_again():
                continue
            break

        prompt("It's dealer's turn...")
        dealer_score = dealer_play(dealer_cards, deck)
        if dealer_score:
            if dealer_score < player_score:
                display_result(player_cards, dealer_cards, player_score, dealer_score)
                print("*****Player won!*****")
            elif dealer_score > player_score:
                display_result(player_cards, dealer_cards, player_score, dealer_score)
                print("*****Dealer won!*****")
            else:
                display_result(player_cards,dealer_cards, player_score,
                    dealer_score)
                print("*****It's a draw!*****")
        else:
            prompt("*****Dealer busted! Player wins!*****")
            display_result(player_cards, dealer_cards)
        if play_again():
            continue
        break

game()
