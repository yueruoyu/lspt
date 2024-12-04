import random

class Deck():
    SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Deck.SUITS
                                       for rank in Deck.RANKS]
        self.shuffle()
    def shuffle(self):
        random.shuffle(self.cards)

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"***{self.suit} {self.rank}***"

class Participant():
    def __init__(self):
        self.hand = Hand()
    def __str__(self):
        return self.hand.__str__()

class Hand():
    VALUE_DICT ={
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
    'Ace': 11
    }

    def __init__(self):
        self.status = []

    def get_a_card(self, card):
        self.status.append(card)

    def __str__(self):
        hand_list = [f"{card.suit} {card.rank}" for card in self.status]
        return ", ".join(hand_list)
    def value(self):
        total = 0
        ace_card = 0
        for card in self.status:
            total += Hand.VALUE_DICT[card.rank]
            if card.rank == "Ace":
                ace_card += 1
        while total > Game.BUSTED_LIMIT and ace_card > 0:
            total -= 10
            ace_card -= 1
        return total 


class Player(Participant):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return "Player"

class Dealer(Participant):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return "Dealer"


class Game():
    BUSTED_LIMIT = 21
    DEALER_LIMIT = BUSTED_LIMIT - 4
    def __init__(self):
        self.dealer = Dealer()
        self.player = Player()
        self.deck = Deck()

    def play(self):
        self.display_welcome_message()
        while True:
            self.__init__()
            self.play_one_game()
            if not self.play_again():
                break
        self.display_goodbye_message()

    def play_again(self):
        prompt = "Do you want to play again(y/n)?: "
        while True:
            answer = input(prompt).casefold().strip()
            if answer[0] in ['y', 'n']:
                break
            print("Sorry, invalid selection!")
        return answer.startswith('y')

    def play_one_game(self):
        self.initial_deal_cards()
        self.show_cards(self.player)
        self.show_cards(self.dealer)
        self.player_run()
        if not self.is_busted(self.player):
            self.dealer_run()
        self.display_result()

    def display_welcome_message(self):
        print("Welcome to the Twenty-One Game!")

    def display_goodbye_message(self):
        print("Thank you! Goodbye!")

    def display_result(self):
        winner = self.who_won()
        if winner:
            print(f"{winner} won!")
        else:
            print("It's a tie!")

    def who_won(self):
        if (self.is_busted(self.player) or
            ((not self.is_busted(self.dealer)) and
                self.player.hand.value() < self.dealer.hand.value())):
            return "Dealer"
        if (self.is_busted(self.dealer) or
            ((not self.is_busted(self.player)) and
                self.player.hand.value() > self.dealer.hand.value())):
            return "Player"
        else:
            return None

    def initial_deal_cards(self):
        for _ in range(2):
            self.deal_a_card(self.player)
        for _ in range(2):
            self.deal_a_card(self.dealer)

    def deal_a_card(self, participant):
        participant.hand.get_a_card(self.deck.cards.pop())

    def show_cards(self, participant):
        print(f"==>{participant} has cards:")
        for card in participant.hand.status:
            print(card)

    def show_dealer_initial_cards(self):
        print(f"==>Dealer has card:")
        print(f"{self.dealer.hand.status[0]}")

    def show_points(self, participant):
        print(f"{participant} has points of {participant.hand.value()}")
    def is_game_over(self):
        return is_busted(self.player) or is_busted(self.dealer)

    def is_busted(self, participant):
        return participant.hand.value() > Game.BUSTED_LIMIT

    def hit(self):
        prompt = "Do you want hit or stay(h/s)?: "
        while True:
            answer = input(prompt).casefold().strip()
            if answer[0] in ['h', 's']:
                break
            print("Sorry, invalid selection")
        return answer.startswith('h')


    def player_run(self):
        self.show_points(self.player)
        while self.hit():
            self.deal_a_card(self.player)
            self.show_cards(self.player)
            self.show_points(self.player)
            if self.is_busted(self.player):
                print("You busted!")
                break

    def dealer_run(self):
        while self.dealer.hand.value() < Game.DEALER_LIMIT:
            self.deal_a_card(self.dealer)
        self.show_cards(self.dealer)
        self.show_points(self.dealer)


game = Game()
game.play()

